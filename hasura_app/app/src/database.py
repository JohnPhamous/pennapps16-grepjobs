# Inserts new job search into database
from src import indeed_scraper
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
    return json.loads(r.text)


def _select(table_name, objects, base=BASE_SELECT):
    base["args"]["table"] = table_name
    base["args"]["where"] = objects
    print(json.dumps(base))
    r = requests.post(url=ENDPOINT, data=json.dumps(base), headers=AUTH_HEADER)
    return json.loads(r.text)


def find_insert_jobs(location_input, title_input, radius="25", number_of_pages=5):
    # if the current query doesn't exist in the database
    if not exists_in_query_table(title_input=title_input, location_input=location_input):
        jobs = indeed_scraper.get_jobsget_jobs(title_input, location_input, radius, number_of_pages)
        input_queries = [{"title_input": title_input, "location_input": location_input}]
        a = _insert(table_name="jobs_update", objects=jobs)
        b = _insert(table_name="query_result", objects=input_queries)
        print("Data doesn't exist yet\n" + str(a) + "\n" + str(b))
        return json.dumps(jobs)
    else:
        print("Data exists and was fetched")
        return json.dumps(job_results_from_query(location_input, title_input))


def job_results_from_query(location_input, title_input):
    return _select(table_name="jobs_update", objects={"location_input": location_input, "title_input": title_input})


def exists_in_query_table(location_input, title_input):
    return len(_select(table_name="query_result", objects={"location_input": location_input, "title_input": title_input})) > 0

# if __name__ == '__main__':
    # print(find_insert_jobs(title_input="Software Developer", location_input="San Fransisco"))


