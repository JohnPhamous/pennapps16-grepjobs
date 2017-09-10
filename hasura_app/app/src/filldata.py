import scraper
import json
#22455
#36384 Business - Kansas
# - Baltimore 38776
# - Chicago 53320
#   Dallas - 88596

CITY_NUMBER = 2


if __name__ == '__main__':
    city_state_list = ["San Francisco, California","San Jose, California", "Washington, D.C.", "Boston, Massachusetts", "Raleigh, North Carolina", "Durham, North Carolina", "Chapel Hill, North Carolina", "Seattle, Washington",  "Austin, Texas", "Denver, Colorado", "Boulder, Colorado", "San Diego, California", "Madison, Wisconsin", "Minneapolis, Minnesota", "St. Paul, Minnesota", "Baltimore, Maryland", "Oakland, California", "East Bay, California", "Portland, Oregon", "New York, New York", "Chicago, Illinois", "Atlanta, Georgia", "Los Angeles, California", "Columbus, Ohio", "Orange County, California", "Dallas, Texas", "Fort Worth, Texas", "Kansas City, Missouri", "Indianapolis, Indiana", "Salt Lake City, Utah", "Nashville, Tennessee"]

    jobs_list = ["Scrum master", "Network administrator", "User interface developer", "Php developer", "Data architect", "Information technology manager", "Business intelligence developer", "User interface designer","Product manager", "Technical account manager", "Systems administrator", "Mobile developer", "Quality assurance manager", "Software engineer", "Solutions architect", "User experience designer", "Database administrator", "Data engineer", "DevOps engineer", "Data scientist","Hardware Engineer", "Salesforce administrator","Cloud engineer"]

    counter = 0
    THE_DATA = []
    for job in jobs_list:
        for city in city_state_list[CITY_NUMBER-1:CITY_NUMBER]:
            jobs = scraper.get_jobs(job,city,25,10)
            for x in jobs:
                print(str(job) + " - " + str(city) + ": " + str(counter))
                counter = counter + 1
                THE_DATA.append(x)

    with open("./data/" + city + ".txt","w") as f:
        f.write(json.dumps(THE_DATA))
