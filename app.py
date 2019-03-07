#!flask/bin/python
from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/advice', methods=['GET'])
def advice():
    try:
        if request.method == 'GET':
            #image_url = request.args.get('image_url')
            #filename = utils.download_image_from_url(image_url)
            utils.addNewCandleToData({ "c": 123, "a": 1, "b": 2})
            return jsonify({
                "hello": "ola"
            })
        else:
            return jsonify({
                'message': 'Action is not defined!'
            }), 404
    except Exception as e:
        return repr(e), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=12480)