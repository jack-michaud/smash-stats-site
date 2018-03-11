import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    context = {}
    return render_template('index.html', context=context)

@app.route("/highcharts")
def highcharts():
    buffer = ""
    with open("dist/highcharts.js") as jq:
        buffer = jq.read()

    return buffer

@app.route("/jquery")
def jquery():
    buffer = ""
    with open("dist/jquery.js") as jq:
        buffer = jq.read()

    return buffer

@app.route("/data")
def fetch_data():
    csvfile = open('output.csv', 'rb')
    reader = csv.DictReader(csvfile, delimiter=',')
    context = []
    for row in reader:
        context.append({
            "count": row["count"],
            "stocks1": row["stocks1"],
            "stocks2": row["stocks2"],
            "percent2": row["percent2"],
            "percent1": row["percent1"]
       })

    csvfile.close()
    return jsonify(context)



