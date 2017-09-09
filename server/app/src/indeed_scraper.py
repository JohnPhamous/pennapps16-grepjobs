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
        locs['zip_code'] = possible_zip
        locs['city_state'] = loc.split()[:-1]
    else:
        locs['zip_code'] = None
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


def get_jobs(query, zip_code, radius="15", number_of_pages=5):
    """
    Provide job query and zip code (optionally radius and number of pages with
        approximately 15 jobs per page)
    Return: Json list of dictionaries with each entry as an entry in the array.
        Elements in job listing: Query, Title, Company
    """

    url_template = "https://www.indeed.com/jobs?q={}&l={}&radius={}&start={}"

    # Replaces spaces with %20
    query_for_search = reduce(lambda x, y: x + "%20" + y, query.split())

    rows = []

    # Start begins at 0 and increments in steps of 10
    # E.g. Page 1 is start=0, page 2 is start=10, page 3 --> start=20, etc
    for start in range(0,number_of_pages*10, 10):
        r = requests.get(url_template.format(query_for_search, zip_code, radius, start))
        soup = BeautifulSoup(r.content, "html5lib")
        results = soup.findAll('div', { "class" : "result" })

        for i, result in enumerate(results):
            if result:
                row = {}
                row['Query'] = query
                row['Title'] = get_title_from_result(result)
                row['Company'] = get_company_from_result(result)
                row['Summary'] = get_summary_from_result(result)
                row['Salary'] = get_salary_from_result(result)
                row['Experience'] = get_experience_from_result(result)

                locs = get_location_from_result(result)
                row['Zip_Code'] = locs['zip_code']
                row['City-State'] = locs['city_state']

                rows.append(row)
    return rows

if __name__ == '__main__':
    import time
    t1 = time.time()

    get_jobs(query="Software Developer", zip_code="33146")

    t2 = time.time()
    print (t2-t1)
