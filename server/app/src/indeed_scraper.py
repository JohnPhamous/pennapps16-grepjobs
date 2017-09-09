# TODO : Check if last 2 pages of results are the same. If so, stop looking for new pages.
#       If we request too many results, we will get repeats
# TODO : Get Salary Information


from bs4 import BeautifulSoup
import requests
import json
from functools import *
import html5lib


def extract_text(el):
    if el:
        return el.text.strip()
    else:
        return ''


def get_company_from_result(result):
    return extract_text(result.find('span', {'class': 'company'}))


def get_location_from_result(result):
    """
    returns dictionary with keys: "zip_code", "city_state"
    """
    loc = extract_text(result.find('span', {'class': 'location'}))
    locs = {}
    possible_zip = int(loc.split()[-1]) if loc.split()[-1].isdigit() else 0
    if possible_zip > 10000 & possible_zip < 100000:
        locs['zip_code'] = str(possible_zip)
        locs['city_state'] = " ".join(loc.split()[:-1])
    else:
        locs['zip_code'] = ''
        locs['city_state'] = loc
    return locs


def get_summary_from_result(result):
    return extract_text(result.find('span', {'class': 'summary'}))


def get_title_from_result(result):
    return extract_text(result.find('a', {'data-tn-element': 'jobTitle'}))


def get_experience_from_result(result):
    return extract_text(result.find('span', {'class': 'experienceList'}))


def get_job_url_from_result(result):
    return "https://indeed.com" + result.find('a', {'data-tn-element': 'jobTitle'})['href']


def get_salary_from_result(result):
    salary_table = result.find('td', {'class' : 'snip'})
    if salary_table:
        snip = salary_table.find('nobr')
        if snip:
            return snip.text.strip()

    return None


def get_jobs(query, location, radius="15", number_of_pages=5):
    """
    Provide job query and location (optionally radius and number of pages with
        approximately 15 jobs per page)
    Return: Json list of dictionaries with each entry as an entry in the array.
        Elements in job listing: Query, Title, Company, Summary of job, Salary, Experience
    """

    url_template = "https://www.indeed.com/jobs?q={}&l={}&radius={}&start={}"

    # Replaces spaces with %20
    query_for_search = reduce(lambda x, y: x + "%20" + y, query.split())

    rows = []

    # Start begins at 0 and increments in steps of 10
    # E.g. Page 1 is start=0, page 2 is start=10, page 3 --> start=20, etc
    for start in range(0,number_of_pages*10, 10):
        r = requests.get(url_template.format(query_for_search, location, radius, start))
        # print url_template.format(query_for_search, location, radius, start)
        soup = BeautifulSoup(r.content, "html5lib")
        results = soup.findAll('div', { "class" : "result" })

        for i, result in enumerate(results):
            if result:
                row = {}
                row['query'] = query
                row['title'] = get_title_from_result(result)
                row['company'] = get_company_from_result(result)
                row['summary'] = get_summary_from_result(result)
                row['salary'] = get_salary_from_result(result)
                row['experience'] = get_experience_from_result(result)

                locs = get_location_from_result(result)
                row['zip_code'] = locs['zip_code']
                row['city_state'] = locs['city_state']

                rows.append(row)
    return rows

if __name__ == '__main__':
    import time
    t1 = time.time()
    print "Testing indeed_scraper.py"
    get_jobs(query="Software Developer", location="33146")
    t2 = time.time()
    print (t2-t1)
