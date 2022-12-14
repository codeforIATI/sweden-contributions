# Sweden Contributions

Automatically generate list of IATI Identifiers grouped by contribution code for Swedish IATI data.

Runs daily on Github Actions.

NB contributions are not output for unrecognised ISO-3 countries, of which there are currently quite a lot!

## Rationale

Many Swedish activities (implemented through Sida) are grouped together by "contribution code". However, theese are broken down into multiple activities in Sweden's IATI data.

This set of scripts makes it possible to look up all the IATI Identifiers for this contribution code.


### Type 1, e.g. `11394`

e.g. for **Budget Strengthening Initiative** in Liberia:

```xml
<sida:contribution xmlns:sida="http://sida.se/ns/contribution#" contributionid="11394"/>
```

For this same contribution code `11394` there are two activities:

* [SE-0-SE-6-11394A0101-LBR-15110](https://datastore.codeforiati.org/api/1/access/activity.xml?iati-identifier=SE-0-SE-6-11394A0101-LBR-15110)
* [SE-0-SE-6-11394A0102-LBR-15110](https://datastore.codeforiati.org/api/1/access/activity.xml?iati-identifier=SE-0-SE-6-11394A0102-LBR-15110)


## Type 2, e.g. `52090011`

e.g. for **Markets & Value Chains in Agriculture Liberia**:

```xml
<sida:contribution xmlns:sida="http://sida.se/ns/contribution#" contributionid="52090011"/>
```

For this same contribution code `52090011` there are four activities:

* [SE-0-SE-6-5209001101-LBR-31120](https://datastore.codeforiati.org/api/1/access/activity.xml?iati-identifier=SE-0-SE-6-5209001101-LBR-31120)
* [SE-0-SE-6-5209001102-LBR-31120](https://datastore.codeforiati.org/api/1/access/activity.xml?iati-identifier=SE-0-SE-6-5209001102-LBR-31120)
* [SE-0-SE-6-5209001103-LBR-31120](https://datastore.codeforiati.org/api/1/access/activity.xml?iati-identifier=SE-0-SE-6-5209001103-LBR-31120)
* [SE-0-SE-6-5209001104-LBR-31120](https://datastore.codeforiati.org/api/1/access/activity.xml?iati-identifier=SE-0-SE-6-5209001104-LBR-31120)

---

## Using the API

We can find all relevant IATI Identifiers for a particular contribution code in a specific country in the following way:
https://codeforiati.org/sweden-contributions/{COUNTRY-CODE}/SE-0-SE-6-{CONTRIBUTION-CODE}.json

For example, we can find all IATI Identifiers for contribution `11394` in Liberia (`LR`) through the following URL:
https://codeforiati.org/sweden-contributions/LR/SE-0-SE-6-11394.json

There are also index files making the API easy to explore:

* [/index.json](https://codeforiati.org/sweden-contributions/index.json) lists countries with lists of contribution codes
* [/LR/index.json](https://codeforiati.org/sweden-contributions/LR/index.json) lists all the contribution code files for a specific country (in this case, Liberia)

## Why does Sweden break its activities down in this way?

From memory, the reason for this is that it allows Sweden to express country and sector allocations for `budget` elements. Currently in the IATI Standard, country and sector allocations can be expressed for transactions (e.g. commitments and disbursements), but not for budgets.

So there are good reasons for Sweden publishing the data the way it does; but it means that users need to know that there are multiple activities for each contribution, in order to get the complete set of data they are interested in.
