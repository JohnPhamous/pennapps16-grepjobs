# Inserts new job search into database

import config
import indeed_scraper

def find_and_insert_job_search(query, location, radius="25", number_of_pages=10):
     jobs = indeed_scraper.get_jobs(query, location, radius, number_of_pages)
     return config.insert(table_name="jobs_update", objects=jobs)

if __name__ == '__main__':
    print(find_and_insert_job_search(query="User interface designer", location="San Francisco, CA"))
