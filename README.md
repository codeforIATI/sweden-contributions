# Sweden Contributions

Automatically generate list of IATI Identifiers grouped by contribution code for Swedish IATI data.

Runs daily on Github Actions.

NB contributions are not output for unrecognised ISO-3 countries, of which there are currently quite a lot!

## Rationale

Many Swedish projects are grouped together by "contribution code". This is visible in Sweden's IATI data, e.g. for Sweden's Budget Strengthening Initiative project in Liberia:

```xml
<sida:contribution xmlns:sida="http://sida.se/ns/contribution#" contributionid="11394"/>
```

For this same contribution code `11394` there are two activities:

* [SE-0-SE-6-11394A0101-LBR-15110](https://datastore.codeforiati.org/api/1/access/activity.xml?iati-identifier=SE-0-SE-6-11394A0101-LBR-15110)
* [SE-0-SE-6-11394A0102-LBR-15110](https://datastore.codeforiati.org/api/1/access/activity.xml?iati-identifier=SE-0-SE-6-11394A0102-LBR-15110)

This set of scripts makes it possible to look up all the IATI Identifiers for this contribution code.

We can find all relevant IATI Identifiers for a particular contribution code in a specific country in the following way:
https://codeforiati.org/sweden-contributions/{COUNTRY-CODE}/SE-0-SE-6-{CONTRIBUTION-CODE}.json

For example, we can find all IATI Identifiers for contribution `11394` in Liberia (`LR`) through the following URL:
https://codeforiati.org/sweden-contributions/LR/SE-0-SE-6-11394.json

There are also index files making the API easy to explore:

* [/index.json](https://codeforiati.org/sweden-contributions/index.json) lists countries with lists of contribution codes
* [/LR/index.json](https://codeforiati.org/sweden-contributions/LR/index.json) lists all the contribution code files for a specific country (in this case, Liberia)

