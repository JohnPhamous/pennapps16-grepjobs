from src import app
from flask import jsonify, request
import requests
import json


@app.route("/")
def hello():
    return json.dumps({"message":"Hello World!"})

@app.route("/wassup")
def hello():
    return HttpResponse(
            json.dumps({"hello":"buddy"}),
            content_type = 'application/javascript; charset=utf8'
    )
