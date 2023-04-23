#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, Response
from datetime import datetime
from time import time
from helpers import HelperService

# Setting up Flask app
app = Flask(__name__)

# Utility functions


def add_to_log(date: datetime, url: str):
    # TODO: add your code below...
    pass


def count_break_links(links: list[str]) -> int:
    # TODO: add your code below...
    pass


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
    # TODO: add your code below...

    return jsonify({"count": 0})


@app.route('/1/queries/popular/<date_prefix>', methods=['GET'])
def popular(date_prefix=None):
    if date_prefix is None:
        return Response('Missing date prefix in request', status=400)

    size = request.args.get('size', type=int, default=3)
    json = {"queries": []}

    # TODO: add your code below

    json["queries"].append({"query": date_prefix, "count": size})
    return jsonify(json)


@app.route('/break_links', methods=['POST'])
def get_break_links():
    links = HelperService.getListLinks(request.get_json(force=True))

    return jsonify({"count_links": count_break_links(links)})


# LOADING LOGS
load_logs("hn_logs.tsv")

if __name__ == '__main__':
    # LAUNCHING REST API
    app.run(host='0.0.0.0', port=8000, debug=False)
