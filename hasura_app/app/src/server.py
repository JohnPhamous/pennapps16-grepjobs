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
    location = str(request.args.get("location", default=""))
    if title and location:
        return database.find_insert_jobs(location_input=location, title_input=title)
    return json.dumps("missing parameter (title or location)")

