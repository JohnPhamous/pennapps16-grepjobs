import scraper
import os
import json

CURRENT = 0



data_dir = "/Users/David/code/pennapps16-grepjobs/hasura_app/app/src/data/"
data_dir2 = "/Users/David/code/pennapps16-grepjobs/hasura_app/app/src/data2/"
city = os.listdir(data_dir)[CURRENT]

with open(data_dir + city, 'r') as f:
    ARR = json.loads(f.read())

dict_of_company_locations = {}

NEW_DATA = []

for entry in ARR:
    try:
        company_tag = entry['company'] + " " + entry['city_state']
        print company_tag
        lat_long = scraper.get_google_thingy_lat_long(company_tag)

        dict_of_company_locations[company_tag] = lat_long

        entry.update(lat_long)

        NEW_DATA.append(entry)
    except ValueError:
        print("shit went wrong for: " + company_tag)
    finally:
        entry.update({'lat':'', 'long':''})
        NEW_DATA.append(entry)

print dict_of_company_locations

with open(data_dir + city, 'w') as f:
    f.write(json.dumps(NEW_DATA))
