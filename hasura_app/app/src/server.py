from src import app
from flask import jsonify, request, render_template
import json
from src import database


@app.route("/test")
def test():
    return json.dumps({"message": "Sup"})


@app.route("/")
def view():
    return render_template("index.html")


@app.route("/home_query/")
def home_query():
    title = str(request.args.get("title", default=""))
    location = str(request.args.get("location", default="")).lower()
    if title and location:
        return database.find_insert_jobs(location_input=location, title_input=title)
    return json.dumps("missing parameter (title or location)")

# here, we take in the location and title,
# pass it into David's scraper,
# return it as json to John
# insert results in the database (if they don't exist)
# @app.route("/home_query", methods=['GET'])
