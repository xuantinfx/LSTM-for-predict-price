#!flask/bin/python
from flask import Flask, request, jsonify
import utils_flask_server as utils
import json
import joblib
import numpy as np

app = Flask(__name__)

global config
with open('config_flask.json', 'r') as f:
    config = json.load(f)

# Load RF model
global rf_model 
rf_model = joblib.load(config["rfModelName"])


@app.route('/advice', methods=['GET'])
def advice():
    try:
        if request.method == 'GET':
            dataGet = {}
            for i in config["dataCol"]:
                dataGet[i] = request.args.get(i)
            datas = utils.addNewCandleToData(dataGet)
            trend_by_percentage, predicted_value = utils.predict(datas)
            return jsonify({
                "trend_by_percentage": trend_by_percentage,
                "predicted_value": predicted_value
            })
        else:
            return jsonify({
                'message': 'Action is not defined!'
            }), 404
    except Exception as e:
        return repr(e), 500


@app.route('/rf_advice', methods=['GET'])
def rf_advice():
    try:
        if request.method == 'GET':
            data = []
            for i in config["dataCol"]:
                data.append(float(request.args.get(i)))
            data = (np.array(data)).reshape(1, -1)
            advice = rf_model.predict(data)[0]
            return jsonify({
                "advice": advice
            })
        else:
            return jsonify({
                'message': 'Action is not defined!'
            }), 404
    except Exception as e:
        return repr(e), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=12480)
