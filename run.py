import requests
import json
import re
import os
# Get codelists to convert ISO3 to ISO2 country codes
regionm49_url = "https://codelists.codeforiati.org/api/json/en/RegionM49.json"
regionm49_data = requests.get(regionm49_url).json()['data']
iso3_iso2 = dict([(cl['codeforiati:iso-alpha-3-code'], cl['codeforiati:iso-alpha-2-code']) for cl in regionm49_data])


identifiers_url = "https://stats.codeforiati.org/current/aggregated-publisher/sida/iati_identifiers.json"
identifiers_data = requests.get(identifiers_url).json()
iati_identifiers = list(identifiers_data.keys())

os.makedirs('output', exist_ok=True)
contributions = {}
for iati_identifier in iati_identifiers:
    matches = re.match('(.*)-(.*)-(.*)$', iati_identifier)
    if not matches:
        print("Cannot match for {}".format(iati_identifier))
        continue
    _contrib, _country, _sector = matches.groups()
    if _country not in contributions.keys():
        contributions[_country] = {}
    if _contrib not in contributions[_country].keys():
        contributions[_country][_contrib] = []
    contributions[_country][_contrib].append(iati_identifier)

for country_code, country_data in contributions.items():
    iso2_country_code = iso3_iso2.get(country_code)
    if not iso2_country_code:
        print("Not writing for country {}".format(country_code))
        continue
    with open('output/{}.json'.format(iso2_country_code), 'w') as outfile:
        json.dump(country_data, outfile)