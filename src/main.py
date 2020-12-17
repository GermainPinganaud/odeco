import json


def main ():
    sites, filters, output_fields = load_data()
    output = {}
    for site in sites :
        if apply_filters(site, filters):
            output = {
                site["nom"]: {
                    output_field : site[output_field] for output_field in output_fields
                }
            }
    write_result(filters, output)


def load_data():
    with open ("data/sites.json") as file:
        sites = json.load(file)
    with open ("data/filters.json") as file:
        filters = json.load(file)
    with open ("data/output_fields.json") as file:
        output_fields = json.load(file)
    return sites, filters, output_fields


def apply_filters(site, filters):
    if filters["dep"] in site["cp"][0:2]:
        if filters["type"] == site["site_sous_type"]:
            winds_dir = site["vent_favo"].split(";")
            if filters["wind"] in winds_dir:
                return True


def write_result(filters, output):
    result = {
        "filters" : filters,
        "ouput" : output
    }
    with open ("data/result.json", "w") as file:
        json.dump(result, file, indent=4)


if __name__ == "__main__":
    main()