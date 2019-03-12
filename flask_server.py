#!flask/bin/python
from flask import Flask, request, jsonify
import utils_flask_server as utils
import json

app = Flask(__name__)

global config
with open('config_flask.json', 'r') as f:
    config = json.load(f)

@app.route('/advice', methods=['GET'])
def advice():
    try:
        if request.method == 'GET':
            dataGet = {}
            for i in config["dataCol"]:
                dataGet[i] = request.args.get(i)
            predict_len = int(request.args.get("predict_len"))
            datas = utils.addNewCandleToData(dataGet)
            results = utils.predict(datas, predict_len)
            return jsonify({
                "results": results
            })
        else:
            return jsonify({
                'message': 'Action is not defined!'
            }), 404
    except Exception as e:
        return repr(e), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=12480)