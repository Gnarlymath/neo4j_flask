from app import app
from flask import request, jsonify, Response, make_response
from .neosession import Neo4jSession
from .application import Query

import datetime
import json


@app.route("/names/request", methods=["POST"])
def name_request():
    data = request.form

    neo_driver = Neo4jSession()
    with neo_driver.driver.session() as dbsession:
        with Query(neo_driver, dbsession) as query:
            resp = query.execute(query_names(data["limit"]))
            if not resp:
                print("no results")
    return make_response(jsonify(resp), 200)


@app.route("/knowledge/request", methods=["POST"])
def knowledge_request():
    form_fields = []
    data = request.form

    for k, v in data.items():
        form_fields.append(v)

    neo_driver = Neo4jSession()

    with neo_driver.driver.session() as dbsession:
        with Query(neo_driver, dbsession) as query:
            resp = query.execute(knowledge_query(form_fields))

    return make_response(jsonify(resp), 200)


def knowledge_query(fields):
    return """
            MATCH(t:Topic {{source:"wef"}})<-[:RELATES_TO_TOPIC]-(k:Knowledge) WHERE k.time < {less_than} AND k.time > {more_than} RETURN k{.*, related_topics: collect(t.name)} as knowledg limit {limit};
            """.format(
        less_than=fields[0], more_than=fields[1], limit=fields[2]
    )


def query_names(req_limit):
    return "match(p:Person) return p limit {limit};".format(limit=req_limit)
