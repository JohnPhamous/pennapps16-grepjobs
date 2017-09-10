import scraper
import os
import json

CURRENT = 0


data_dir = "./data/"
data_dir2 = "./data2/"
city = "Washington, D.C..txt"

with open(data_dir + city, 'r') as f:
    ARR = json.loads(f.read())

dict_of_company_locations = {}

NEW_DATA = []

for entry in ARR[:5]:
    try:
        company_tag = entry['company'] + " " + entry['city_state']
        print company_tag

        lat_long = None
        if company_tag in dict_of_company_locations:
            lat_long = dict_of_company_locations[company_tag]
        else:
            lat_long = scraper.get_google_thingy_lat_long(company_tag)
            dict_of_company_locations[company_tag] = lat_long

        print "lat_long :" + str(lat_long)
        entry.update(lat_long)
        print "Entry: " + str(entry)
        NEW_DATA.append(entry)
        print "NEW DATA: " + str(NEW_DATA)

    except ValueError:
        print("shit went wrong for: " + company_tag)
        entry.update({'lat':'', 'long':''})
        NEW_DATA.append(entry)

print dict_of_company_locations

with open(data_dir2 + city, 'a') as f:
    f.write(json.dumps(NEW_DATA))
