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
    _corrected_contrib = _contrib.split("A")
    if _corrected_contrib is not None:
        _contrib = _corrected_contrib[0]
    if _country not in contributions.keys():
        contributions[_country] = {}
    if _contrib not in contributions[_country].keys():
        contributions[_country][_contrib] = []
    contributions[_country][_contrib].append(iati_identifier)

index_countries = {}

for country_code, country_data in contributions.items():
    iso2_country_code = iso3_iso2.get(country_code)
    if not iso2_country_code:
        print("Not writing for country {}".format(country_code))
        continue
    with open('output/{}.json'.format(iso2_country_code), 'w') as outfile:
        json.dump(country_data, outfile)

    os.makedirs(os.path.join('output', iso2_country_code), exist_ok=True)
    for contribution_code, iati_identifiers in country_data.items():
        with open('output/{}/{}.json'.format(iso2_country_code, contribution_code), 'w') as outfile:
            json.dump(iati_identifiers, outfile)
    with open('output/{}/index.json'.format(iso2_country_code), 'w') as out_country_index:
        json.dump([f"{contribution_code}.json" for contribution_code in sorted(country_data.keys())], out_country_index)

    index_countries[iso2_country_code] = f"{iso2_country_code}/index.json"

with open('output/index.json', 'w') as index_file:
    json.dump(dict(sorted(index_countries.items())), index_file)
