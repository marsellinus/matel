# AlienVault OTX — partial use only

OTX was queried through its unauthenticated indicator endpoints, which are readable:

```
GET https://otx.alienvault.com/api/v1/indicators/domain/<domain>/general
```

The unauthenticated **pulse search** endpoint is not available, so a keyword-driven search
for Emotet, Dridex or FIN6 pulses could not be performed:

```
$ curl "https://otx.alienvault.com/api/v1/search/pulses?q=emotet&limit=2"
{"detail": "Authentication required"}
```

Because the report's IOC set is built from sources that carry full provenance for every row
(a government advisory and a sinkhole-derived blocklist), no OTX-derived row was added to
`ioc/`. Had one been added, it would have had to be labelled with the pulse name, the pulse
author and the observation date, none of which were retrievable here.

Consequence for the report: the IOC table cites CISA AA19-339A and abuse.ch Feodo Tracker
only. OTX is named in the methodology as a planned source that could not be used without
registration.
