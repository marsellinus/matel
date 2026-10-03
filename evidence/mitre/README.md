# MITRE ATT&CK evidence

`matel_ttp_mapping.json` is the machine-readable evidence base for the TTP tables in
the report. Every row carries the exact `evidence` sentence asserted by the citing
authority, so a reviewer can re-derive the table instead of trusting it.

Sources (accessed 2026-10-03):

| Ref | Source | URL |
|-----|--------|-----|
| MITRE-1 | Emotet, Software S0367 | https://attack.mitre.org/software/S0367/ |
| MITRE-2 | Dridex, Software S0384 | https://attack.mitre.org/software/S0384/ |
| MITRE-3 | TA505, Group G0092 | https://attack.mitre.org/groups/G0092/ |
| MITRE-4 | FIN6, Group G0037 | https://attack.mitre.org/groups/G0037/ |

`fin6_mitre_mapping.txt` is a superseded placeholder written by an earlier build step
and must not be cited; `matel_ttp_mapping.json` replaces it.
