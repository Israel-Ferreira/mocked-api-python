from flask import Flask, jsonify
from services.user_service import get_all_data_from_jsonf


app =  Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({
        "msg": "Hello World"
    })


@app.route("/mocked-data", methods=["GET"])
def get_mocked_data():
    mocked_data =  get_all_data_from_jsonf()

    if(len(mocked_data) == 0):
        return jsonify(mocked_data)


    mocked_data_json = [mock_car.to_json_dict() for mock_car in mocked_data]

    return jsonify(mocked_data_json)


app.run(host='0.0.0.0')
