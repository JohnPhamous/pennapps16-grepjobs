from .indeed_scraper import get_jobs
from src import app
from flask import jsonify, request, render_template
import requests
import json


@app.route("/test")
def test():
    return json.dumps({"message": "Sup"})

@app.route("/")
def test():
    return render_template("index.html")

@app.route("/home_query/")
def home_query():
    title = str(request.args.get("title", default=""))
    location = str(request.args.get("location", default=""))
    if title and location:
        query_result = get_jobs(query=title, zip_code=int(location))
        return json.dumps(get_jobs(query=title, zip_code=int(location)))
    return json.dumps("missing parameter (title or location)")

# here, we take in the location and title,
# pass it into David's scraper,
# return it as json to John
# insert results in the database (if they don't exist)
# @app.route("/home_query", methods=['GET'])


