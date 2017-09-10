import scraper

#"Scrum master", "Network administrator", "User interface developer", "Php developer", 22455
#"Data architect", "Information technology manager", "Business intelligence developer", 36384 Business - Kansas
#"User interface designer", - Baltimore 38776
#"Product manager", "Technical account manager", "Systems administrator", "Mobile developer", - Chicago 53320
#  "Quality assurance manager", "Software engineer", "Solutions architect", "User experience designer", "Database administrator", "Data engineer", "DevOps engineer", "Data scientist","Hardware Engineer", "Salesforce administrator", Dallas - 88596
#"San Francisco, California","San Jose, California", "Washington, D.C.", "Boston, Massachusetts", "Raleigh, North Carolina", "Durham, North Carolina", "Chapel Hill, North Carolina", "Seattle, Washington",  89815

if __name__ == '__main__':
    city_state_list = ["Austin, Texas", "Denver, Colorado", "Boulder, Colorado", "San Diego, California", "Madison, Wisconsin", "Minneapolis, Minnesota", "St. Paul, Minnesota", "Baltimore, Maryland", "Oakland, California", "East Bay, California", "Portland, Oregon", "New York, New York", "Chicago, Illinois", "Atlanta, Georgia", "Los Angeles, California", "Columbus, Ohio", "Orange County, California", "Dallas, Texas", "Fort Worth, Texas", "Kansas City, Missouri", "Indianapolis, Indiana", "Salt Lake City, Utah", "Nashville, Tennessee"]

    jobs_list = [ "Cloud engineer"]

    file_object = open("./output.txt","a")
    counter = 89815
    for i in jobs_list:
        for j in city_state_list:
            jobs = scraper.get_jobs(i,j,25,10)
            for x in jobs:
                print(str(i) + " - " + str(j) + ": " + str(counter))
                file_object.write(str(x))
                counter = counter + 1


    file_object.close()
