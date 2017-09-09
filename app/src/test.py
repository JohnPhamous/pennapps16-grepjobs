from indeed_scraper import get_jobs
from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return json.dumps({"message":"Bye World!"})

@app.route("/home_query/")
def home_query():
    title = str(request.args.get("title", default=""))
    location = str(request.args.get("location", default=""))
    if title and location:
        return json.dumps(get_jobs(query=title, zip_code=int(location)))
    return json.dumps("you fucked up")

if __name__ == '__main__':
    app.run()
