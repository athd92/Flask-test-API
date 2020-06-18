from flask import Flask, render_template, jsonify, request, make_response
import json
import os


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/city/", methods=["GET"])
def get_city():
    with open("cities.json", "r") as f:
        data = json.load(f)
    name = request.args["title"]
    cities = data.get("cities")
    if request.args.get("title", None):
        name = name.capitalize()
    result = []
    for city in cities:
        if city["title"] == name:
            result.append(city)
            return render_template("city.html", result=result)
    else:
        # (1) here we could log the request details further analysis
        return render_template("city.html")


@app.route("/send/", methods=["POST"])
def send():
    datas = request.form
    sent = "New entry sent"
    new_datas = json.dumps(dict(datas))

    with open("cities.json", "r") as f:
        data = json.load(f)
        data["cities"].append(dict(datas))

    with open("cities.json", "w") as f:
        f.write(json.dumps(data))
        # Here we could:
        # (1) add Celery task to send email notification to client
        # (2) add SMS task also with Celery and Twillo
        # (3) log the events
    return render_template("index.html", sent=sent)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)
