from flask import Flask, jsonify, request, render_template
import json
import database

app = Flask(__name__)

@app.route("/test")
def test():
    return json.dumps({"message": "Sup"})

@app.route("/")
def view():
    return render_template("index.html")

@app.route("/home_query/")
def home_query():
    # for both of these parameters we need to convert %20 to a space
    title = str(request.args.get("title", default="")).replace("%20", " ")
    location = str(request.args.get("location", default="")).replace("%20", " ")
    if title and location:
        return database.find_insert_jobs(location_input=location, title_input=title)
    return json.dumps("missing parameter (title or location)")

if __name__ == '__main__':
    app.run()
