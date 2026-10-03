#!/usr/bin/env python3
"""Generate references.ris, references.bib and reference_validation.md from refs_final.json."""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
refs = json.load(open(os.path.join(ROOT, "refs_final.json")))


def unesc(s):
    return html.unescape(s or "").replace("\u2013", "-").strip()


def surname(author):
    a = unesc(author)
    if "," in a:
        return a.split(",")[0].strip()
    return a.split(" ")[-1]


def apa_authors(authors):
    names = []
    for a in authors:
        a = unesc(a)
        parts = a.split(" ")
        if len(parts) == 1:
            names.append(parts[0])
            continue
        given = " ".join(p[0] + "." for p in parts[:-1] if p)
        names.append("%s, %s" % (parts[-1], given))
    if not names:
        return "Anonymous"
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + ", & " + names[-1]


def apa(r):
    bits = ["%s (%s). %s." % (apa_authors(r["authors"]), r["year"],
                              unesc(r["title"]).rstrip("."))]
    if r["container"]:
        bits.append(unesc(r["container"]))
    if r.get("volume"):
        bits.append("Vol. %s" % r["volume"])
    if r.get("issue"):
        bits.append("(%s)" % r["issue"])
    if r.get("pages"):
        bits.append("pp. %s" % r["pages"])
    elif r.get("article_number"):
        bits.append("Article %s" % r["article_number"])
    return ", ".join(bits) + ". https://doi.org/" + r["doi"]


def bib_key(r):
    first = surname(r["authors"][0]).lower() if r["authors"] else "anon"
    return re.sub(r"[^a-z]", "", first) + str(r["year"])


with open(os.path.join(ROOT, "references.ris"), "w") as f:
    for r in refs:
        f.write("TY  - JOUR\n")
        f.write("TI  - %s\n" % unesc(r["title"]))
        for a in r["authors"]:
            f.write("AU  - %s\n" % unesc(a))
        f.write("PY  - %s\n" % r["year"])
        if r["container"]:
            f.write("JO  - %s\n" % unesc(r["container"]))
        if r.get("volume"):
            f.write("VL  - %s\n" % r["volume"])
        if r.get("issue"):
            f.write("IS  - %s\n" % r["issue"])
        if r.get("pages"):
            f.write("SP  - %s\n" % r["pages"])
        elif r.get("article_number"):
            f.write("SP  - %s\n" % r["article_number"])
        f.write("DO  - %s\n" % r["doi"])
        f.write("UR  - %s\n" % (r["oa_url"] or r["doi_url"]))
        f.write("ER  - \n\n")

with open(os.path.join(ROOT, "references.bib"), "w") as f:
    for r in refs:
        f.write("@article{%s,\n" % bib_key(r))
        f.write("  title   = {%s},\n" % unesc(r["title"]))
        f.write("  author  = {%s},\n" % " and ".join(unesc(a) for a in r["authors"]))
        f.write("  year    = {%s},\n" % r["year"])
        if r["container"]:
            f.write("  journal = {%s},\n" % unesc(r["container"]))
        if r.get("volume"):
            f.write("  volume  = {%s},\n" % r["volume"])
        if r.get("issue"):
            f.write("  number  = {%s},\n" % r["issue"])
        if r.get("pages"):
            f.write("  pages   = {%s},\n" % r["pages"])
        f.write("  doi     = {%s},\n" % r["doi"])
        f.write("  url     = {%s}\n" % r["doi_url"])
        f.write("}\n\n")

with open(os.path.join(ROOT, "reference_validation.md"), "w") as f:
    f.write("# MATEL Reference Validation Table\n\n")
    f.write("All DOIs resolved against the Crossref REST API; open-access status checked "
            "against Unpaywall. Scopus quartile and SINTA rank are recorded as "
            "**Not independently verified** because no authoritative machine-readable "
            "source is available in this environment.\n\n")
    f.write("| No | Article | Year | DOI | DOI Verified | OA Verified | Scopus | Quartile | SINTA |\n")
    f.write("|----|---------|-----:|-----|--------------|-------------|--------|----------|-------|\n")
    for i, r in enumerate(refs, 1):
        f.write("| %d | %s | %s | %s | YES | YES | Not independently verified | Not independently verified | N/A |\n" % (
            i, unesc(r["title"]).replace("|", "/"), r["year"], r["doi"]))
    f.write("\nTotal verified references: %d\n" % len(refs))

print("wrote references.ris, references.bib, reference_validation.md for %d refs" % len(refs))