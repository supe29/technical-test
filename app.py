#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, Response
from datetime import datetime
from time import time
from helpers import HelperService
from collections import Counter
import requests
from dateutil.parser import parse as parse_date

# Setting up Flask app
app = Flask(__name__)

# Utility functions
logs = []


def add_to_log(date: datetime, url: str):
    # TODO: add your code below...
    logs.append({"date": date, "url": url})

    pass


def count_break_links(links: list[str]) -> int:
    # TODO: add your code below...
    count = 0
    for link in links:
        start = time()
        res = requests.get(link)
        end = time() - start
        print(link, end)
        if res.status_code >= 400 or end > 60:
            count = count + 1

    return count


def load_logs(filename: str):
    print("loading, please wait...")
    start = time()
    with open(filename, 'r') as f:
        for line in f:
            splited = line.strip('\n').split('\t')
            date = datetime(
                *map(int, splited[0].replace(":", "-").replace(" ", "-").split("-")))
            url = splited[1]
            add_to_log(date, url)

    end = time()
    print("loaded in : " + str(round(end - start, 3)) + "s")


@app.route('/1/queries/count/<date_prefix>', methods=['GET'])
def count(date_prefix=None):
    if date_prefix is None:
        return Response('Missing date prefix', status=400)

    matching_logs = []

   
    for log in logs:
        if date_prefix in log["date"].strftime("%Y-%m-%d %H:%M:%S"):
            matching_logs.append(log)

    return jsonify({"count": len(matching_logs)})


@ app.route('/1/queries/popular/<date_prefix>', methods=['GET'])
def popular(date_prefix=None):
    if date_prefix is None:
        return Response('Missing date prefix in request', status=400)

    size = request.args.get('size', type=int, default=3)
    matchlog = [log for log in logs if log["date"].strftime(
        "%Y-%m-%d").startswith(date_prefix)]

    querycount = Counter(log["url"]for log in matchlog)

    topquerry = querycount.most_common(size)

    json = {"queries": []}
    for query, count in topquerry:
        json["queries"].append({"query": query, "count": count})

    

    return jsonify(json)


@ app.route('/break_links', methods=['POST'])
def get_break_links():
    links = HelperService.getListLinks(request.get_json(force=True))

    return jsonify({"count_links": count_break_links(links)})


# LOADING LOGS
load_logs("hn_logs.tsv")

if __name__ == '__main__':
    # LAUNCHING REST API
    app.run(host='0.0.0.0', port=8000, debug=False)
