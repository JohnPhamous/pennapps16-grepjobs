from indeed_scraper import get_jobs
from flask import Flask, jsonify, request, render_template
import requests
import json
import os

template_dir = os.path.abspath('../frontend')
app = Flask(__name__, template_folder=template_dir)


@app.route("/test")
def test():
    return json.dumps({"message": "Sup"})


@app.route("/")
def view():
    return render_template("index.html")


@app.route("/home_query/")
def home_query():
    title = str(request.args.get("title", default=""))
    location = str(request.args.get("location", default=""))
    if title and location:
        query_result = get_jobs(query=title, zip_code=int(location))
        return json.dumps(get_jobs(query=title, zip_code=int(location)))
    return json.dumps("missing parameter (title or location)")

if __name__ == '__main__':
    app.run()
