#!/usr/bin/env python3
"""
MATEL IOC builder — passive / IOC-only threat intelligence.

Sources (metadata only, no malware execution, no C2 contact):
  * CISA AA19-339A advisory IOC CSV (Dridex / TA505 / Evil Corp)   -> official government publication
  * abuse.ch Feodo Tracker IP blocklist JSON (botnet C2 trackers)   -> passive sinkhole-derived telemetry

Nothing in this script downloads, executes, or contacts malware infrastructure.
"""
import csv
import json
import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
IOC_DIR = os.path.join(ROOT, "ioc")
EV = os.path.join(ROOT, "evidence")

CISA_CSV = os.path.join(EV, "vendor_reports", "CISA_AA19-339A_dridex_iocs.csv")
FEODO_JSON = os.path.join(EV, "vendor_reports", "feodotracker_ipblocklist.json")
CISA_URL = "https://www.cisa.gov/sites/default/files/publications/AA19-339A_WHITE.csv"
FEODO_URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.json"

FIELDS = ["actor", "malware", "ioc_type", "ioc_value", "first_seen", "last_seen",
          "source", "confidence", "context"]

HASH_LEN = {32: "md5", 40: "sha1", 64: "sha256"}
IPV4 = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")


def fetch(url, dest):
    if not os.path.exists(dest):
        req = urllib.request.Request(url, headers={"User-Agent": "matel-cti/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
            f.write(r.read())


def normalize_hash(value):
    v = value.strip().lower()
    return v if re.fullmatch(r"[a-f0-9]+", v) and len(v) in HASH_LEN else None


def normalize_domain(value):
    v = value.strip().lower().strip(".")
    v = re.sub(r"^https?://", "", v).split("/")[0].split(":")[0]
    return v if re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", v) else None


def normalize_ip(value):
    v = value.strip()
    return v if IPV4.match(v) else None


def cisa_rows():
    """Dridex IOCs from CISA advisory AA19-339A (FinCEN-reported, TLP:WHITE)."""
    rows = []
    with open(CISA_CSV, newline="") as f:
        for r in csv.DictReader(f):
            seen = "2019-12-03"           # advisory publication date; no finer timestamp published
            for col, kind in (("md5", "md5"), ("sha1", "sha1"), ("sha256", "sha256")):
                if r.get(col):
                    h = normalize_hash(r[col])
                    if h:
                        rows.append(dict(actor="TA505", malware="Dridex", ioc_type=kind,
                                         ioc_value=h, first_seen=seen, last_seen="2020-06-30",
                                         source="CISA AA19-339A",
                                         confidence="High",
                                         context="Dridex/BitPaymer sample hash reported by FinCEN to CISA"))
            if r.get("domain"):
                d = normalize_domain(r["domain"])
                if d:
                    rows.append(dict(actor="TA505", malware="Dridex", ioc_type="domain",
                                     ioc_value=d, first_seen=seen, last_seen="2020-06-30",
                                     source="CISA AA19-339A", confidence="Medium",
                                     context="Malicious domain from Dridex phishing/malspam activity"))
            if r.get("ipv4"):
                ip = normalize_ip(r["ipv4"])
                if ip:
                    rows.append(dict(actor="TA505", malware="Dridex", ioc_type="ipv4",
                                     ioc_value=ip, first_seen=seen, last_seen="2020-06-30",
                                     source="CISA AA19-339A", confidence="Medium",
                                     context="Malicious IP associated with Dridex infrastructure"))
            if r.get("email"):
                rows.append(dict(actor="TA505", malware="Dridex", ioc_type="email",
                                 ioc_value=r["email"].strip().lower(), first_seen=seen,
                                 last_seen="2020-06-30", source="CISA AA19-339A",
                                 confidence="Medium",
                                 context="Sender/return address used in Dridex phishing lures"))
    return rows


def feodo_rows():
    """Botnet C2 IPs from abuse.ch Feodo Tracker; Emotet entries only."""
    rows = []
    with open(FEODO_JSON) as f:
        data = json.load(f)
    for e in data:
        if e.get("malware") != "Emotet":
            continue
        rows.append(dict(
            actor="TA542", malware="Emotet", ioc_type="ipv4",
            ioc_value=e["ip_address"], first_seen=e.get("first_seen", "Not Available"),
            last_seen=e.get("last_online", "Not Available"),
            source="abuse.ch Feodo Tracker", confidence="High",
            context=("Botnet C2 endpoint (port %s, status %s, AS%d %s, %s) "
                     "tracked from sinkhole telemetry") % (
                e.get("port"), e.get("status"), e.get("as_number") or 0,
                e.get("as_name") or "unknown ASN", e.get("country"))))
    return rows


def mitre_rows():
    """Emotet network infrastructure techniques triangulated from MITRE ATT&CK."""
    return [
        dict(actor="TA542", malware="Emotet", ioc_type="technique",
             ioc_value="T1071.001", first_seen="2014-06", last_seen="2023",
             source="MITRE ATT&CK S0367", confidence="High",
             context="Application Layer Protocol: Web Protocols used for C2"),
        dict(actor="TA542", malware="Emotet", ioc_type="technique",
             ioc_value="T1571", first_seen="2019-01", last_seen="2023",
             source="MITRE ATT&CK S0367", confidence="High",
             context="HTTP over non-standard ports 20/22/443/7080/50000"),
        dict(actor="TA542", malware="Emotet", ioc_type="technique",
             ioc_value="T1573.001", first_seen="2014-06", last_seen="2023",
             source="MITRE ATT&CK S0367", confidence="High",
             context="Encrypted Channel: RSA-encrypted C2 traffic"),
        dict(actor="TA505", malware="Dridex", ioc_type="technique",
             ioc_value="T1090", first_seen="2015", last_seen="2020",
             source="MITRE ATT&CK S0384", confidence="High",
             context="Peer-to-peer/backconnect proxy C2 relay between infected peers"),
        dict(actor="TA505", malware="Dridex", ioc_type="technique",
             ioc_value="T1573.001", first_seen="2015", last_seen="2020",
             source="MITRE ATT&CK S0384", confidence="High",
             context="RC4-encrypted C2 channel"),
        dict(actor="FIN6", malware="FrameworkPOS", ioc_type="technique",
             ioc_value="T1048.003", first_seen="2016", last_seen="2019",
             source="MITRE ATT&CK G0037", confidence="High",
             context="Card data exfiltrated to remote servers via HTTP POST"),
    ]


def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main():
    os.makedirs(IOC_DIR, exist_ok=True)
    fetch(CISA_URL, CISA_CSV)
    fetch(FEODO_URL, FEODO_JSON)

    dridex = cisa_rows()
    emotet = feodo_rows() + mitre_rows()

    # FIN6 has no open authoritative binary/network feed we can legally query without
    # an API key, so the actor row set is left empty rather than fabricated.
    fin6 = []

    write_csv(os.path.join(IOC_DIR, "ta542_emotet_ioc.csv"), emotet)
    write_csv(os.path.join(IOC_DIR, "ta505_dridex_ioc.csv"), dridex)
    write_csv(os.path.join(IOC_DIR, "fin6_ioc.csv"), fin6)

    merged = emotet + dridex + fin6
    seen, deduped = set(), []
    for r in merged:
        key = (r["actor"], r["ioc_type"], r["ioc_value"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    deduped.sort(key=lambda r: (r["actor"], r["ioc_type"], r["ioc_value"]))
    write_csv(os.path.join(IOC_DIR, "all_ioc_normalized.csv"), deduped)

    print("emotet=%d dridex=%d fin6=%d merged=%d" %
          (len(emotet), len(dridex), len(fin6), len(deduped)))


if __name__ == "__main__":
    main()