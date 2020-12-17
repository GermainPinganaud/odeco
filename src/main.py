import json
from os import name
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open ("data/sites.json") as file:
    sites = json.load(file)
with open ("data/filters.json") as file:
    filters = json.load(file)
with open ("data/output_fields.json") as file:
    output_fields = json.load(file)


def main ():
    output = {}
    for site in sites :
        if apply_filters(site):
            site_name = site["nom"]
            output[site_name] = {}
            for output_field in output_fields :
                output[site_name][output_field] = site[output_field]


    result = {
        "filters" : filters,
        "ouput" : output
    }

    with open ("data/result.json", "w") as file:
        json.dump(result, file, indent=4)


def apply_filters(site):
    if filters["dep"] in site["cp"][0:2]:
        if filters["type"] == site["site_sous_type"]:
            winds_dir = site["vent_favo"].split(";")
            if filters["wind"] in winds_dir:
                return True

if __name__ == "__main__":
    main()