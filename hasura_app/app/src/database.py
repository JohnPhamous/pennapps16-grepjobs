# Inserts new job search into database

import config
import scraper
import requests
import json

AUTH_HEADER = {"Authorization": "Bearer jekxp6zm4xol71zqo1d34dqzmps39jtq", "Content-Type": "application/json"}
ENDPOINT = "https://data.howl77.hasura-app.io/v1/query"
BASE_INSERT = {
    "type": "insert",
    "args": {
        "table": None,
        "objects": None
    }
}

BASE_SELECT = {
    "type": "select",
    "args": {
        "columns": ["*"],
        "table": None,
        "where": None
    }
}


def _insert(table_name, objects, base=BASE_INSERT):
    base["args"]["table"] = table_name
    base["args"]["objects"] = objects
    print(json.dumps(base))
    r = requests.post(url=ENDPOINT, data=json.dumps(base), headers=AUTH_HEADER)
    return r.text


def _select(table_name, objects, base=BASE_SELECT):
    base["args"]["table"] = table_name
    base["args"]["where"] = objects
    print(json.dumps(base))
    r = requests.post(url=ENDPOINT, data=json.dumps(base), headers=AUTH_HEADER)
    return r.text


def find_insert_jobs(title_input, location_input, radius="25", number_of_pages=5):
    # if the current query doesn't exist in the database
    if not exists_in_query_table(title_input, location_input):
        print("Data doesn't exist yet")
        jobs = scraper.get_jobs(title_input, location_input, radius, number_of_pages)
        input_queries = [{"title_input": title_input, "location_input": location_input}]
        _insert(table_name="jobs_update", objects=jobs)
        _insert(table_name="query_result", objects=input_queries)
        return jobs
    else:
        print("Data exists and was fetched")
        return job_results_from_query(location_input, title_input)


def job_results_from_query(location_input, title_input):
    return _select(table_name="jobs_update", objects={"location_input": location_input, "title_input": title_input})


def exists_in_query_table(location_input, title_input):
    return _select(table_name="query_result", objects={"location_input": location_input, "title_input": title_input})

if __name__ == '__main__':
    # print(find_insert_jobs(title_input="Software", location_input="San Fransisco"))
    print(exists_in_query_table("developer", "San Fransisco"))
