#!/usr/bin/env python3
"""
MATEL reference validator.

For every candidate DOI this script:
  1. resolves it against the Crossref REST API (authoritative DOI registration metadata),
  2. refuses the record unless the metadata is complete and the DOI resolves to the *same* work,
  3. queries Unpaywall for a legal open-access location,
  4. writes the verified record plus the exact verification evidence.

Scopus quartile and SINTA rank are NOT derived here. There is no free, authoritative,
machine-readable source for either, so the script emits "Not independently verified"
and the report must not claim otherwise.

Usage:  python3 validate_references.py [--refresh]
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
CANDIDATES = os.path.join(ROOT, "refs_candidates.json")
OUT = os.path.join(ROOT, "refs_verified.json")
EV = os.path.join(ROOT, "evidence", "academic")
MAILTO = "matel.report@example.org"
UA = {"User-Agent": "MATEL-CTI/1.0 (mailto:%s)" % MAILTO}


def get_json(url, timeout=45):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def title_similar(a, b):
    """Token-set overlap; guards against a DOI that resolves to a different article."""
    ta, tb = set(norm_title(a).split()), set(norm_title(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / max(len(ta), len(tb))


def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    return get_json(url)["message"]


def unpaywall(doi):
    url = "https://api.unpaywall.org/v2/%s?email=%s" % (urllib.parse.quote(doi), MAILTO)
    return get_json(url)


def year_of(msg):
    for key in ("published-print", "published-online", "issued", "created"):
        parts = (msg.get(key) or {}).get("date-parts") or [[]]
        if parts and parts[0] and parts[0][0]:
            return parts[0][0]
    return None


def authors_of(msg):
    out = []
    for a in msg.get("author", []) or []:
        name = " ".join(x for x in (a.get("given"), a.get("family")) if x).strip()
        if name:
            out.append(name)
        elif a.get("name"):
            out.append(a["name"])
    return out


def container_of(msg):
    ct = msg.get("container-title") or []
    return ct[0] if ct else None


def verify(cand):
    doi = cand["doi"].strip()
    rec = {
        "id": cand["id"],
        "doi": doi,
        "doi_url": "https://doi.org/" + doi,
        "topic": cand.get("topic", ""),
        "doi_resolves": False,
        "crossref_match": False,
        "title": None, "authors": [], "year": None, "container": None,
        "publisher": None, "volume": None, "issue": None, "pages": None,
        "article_number": None,
        "open_access": False, "oa_status": None, "oa_url": None, "license": None,
        "scopus_indexed": "Not independently verified",
        "scopus_quartile": "Not independently verified",
        "sinta_indexed": "N/A",
        "sinta_rank": "N/A",
        "verification_source": "Crossref REST API + Unpaywall API",
        "verification_date": time.strftime("%Y-%m-%d"),
        "errors": [],
    }
    try:
        msg = crossref(doi)
        rec["doi_resolves"] = True
        rec["title"] = (msg.get("title") or [None])[0]
        rec["authors"] = authors_of(msg)
        rec["year"] = year_of(msg)
        rec["container"] = container_of(msg)
        rec["publisher"] = msg.get("publisher")
        rec["volume"] = msg.get("volume")
        rec["issue"] = msg.get("issue")
        rec["pages"] = msg.get("page")
        rec["article_number"] = msg.get("article-number")
        rec["type"] = msg.get("type")
    except Exception as e:                       # DOI does not resolve -> reject
        rec["errors"].append("crossref: %s" % e)
        return rec

    sim = title_similar(cand.get("expect_title"), rec["title"])
    rec["title_similarity"] = round(sim, 3)
    if sim < 0.8:
        rec["errors"].append(
            "DOI does not match expected article (similarity %.2f)" % sim)
    else:
        rec["crossref_match"] = True

    if not rec["container"]:
        rec["errors"].append("no journal/conference container title")
    if not rec["year"]:
        rec["errors"].append("no publication year")
    if not rec["authors"]:
        rec["errors"].append("no authors")

    try:
        up = unpaywall(doi)
        rec["oa_status"] = up.get("oa_status")
        best = up.get("best_oa_location") or {}
        if up.get("is_oa") and best:
            rec["open_access"] = True
            rec["oa_url"] = best.get("url_for_pdf") or best.get("url")
            rec["license"] = best.get("license")
        else:
            rec["errors"].append("no legal open-access location confirmed by Unpaywall")
    except Exception as e:
        rec["oa_status"] = "unknown"
        rec["errors"].append("unpaywall: %s" % e)

    return rec


def main():
    os.makedirs(EV, exist_ok=True)
    cands = json.load(open(CANDIDATES))
    if "--refresh" not in sys.argv and os.path.exists(OUT):
        have = {r["doi"]: r for r in json.load(open(OUT))}
    else:
        have = {}

    results = []
    for c in cands:
        if c["doi"] in have and not have[c["doi"]]["errors"]:
            results.append(have[c["doi"]])
            continue
        r = verify(c)
        results.append(r)
        flag = "OK " if (r["crossref_match"] and r["open_access"]) else "-- "
        print("%s%-9s %s | OA=%s | %s" % (
            flag, r["id"], (r["title"] or "?")[:58], r["open_access"],
            "; ".join(r["errors"])[:70]))
        time.sleep(0.4)

    json.dump(results, open(OUT, "w"), indent=2)
    ok = [r for r in results if r["crossref_match"] and r["open_access"]]
    print("\nverified usable: %d / %d" % (len(ok), len(results)))


if __name__ == "__main__":
    main()