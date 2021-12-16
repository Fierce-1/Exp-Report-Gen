import time
from pymongo import MongoClient

from flask import *


cluster = MongoClient(
    "mongodb+srv://<username>:<pass>@clusterh.lcaaf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["user"]
collection = db["user"]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/send_data', methods=['POST', 'GET'])
def login():
    username1 = request.form["username"]
    password1 = request.form["password"]

    result = collection.find_one({"username": username1, "pass": password1})

    if result:
        return render_template('main_menu.html')
    else:
        return render_template('login.html')

@app.route('/report.html', methods=['POST', 'GET'])
def report():
    cluster1 = MongoClient(
        "mongodb+srv://<username>:<pass>@clusterh.lcaaf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db1 = cluster1["test"]
    collection1 = db1["test"]

    date1 = "2021-12-09"
    select = request.form.get('report of all')

    res = collection1.find({"Date": date1})

    data = []

    for x in res:
        data.append(x)

    return render_template('report.html', len=len(data), rows=data, start_date=date1, report=select)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)

