import random
import json
import csv
import tensorflow as tf
from model.core.model import Model
from model.core.data_processor import DataLoader

global config
candles = []

with open('config_flask.json', 'r') as f:
    config = json.load(f)

with open(config["dataName"]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        i = 0
        candle = {}
        for key in config['dataCol']:
            candle[key] = row[i]
            i += 1
        candles.append(candle)

model = Model()
model.load_model(config["nameModel"])
global graph
graph = tf.get_default_graph()

dataLoader = DataLoader(
    config["dataName"],
    config['data']['train_test_split'],
    config['data']['columns']
)

def predict(datas):
    # Chỗ này sẽ load model lên và tiến hành predict
    transformed_data = dataLoader.transform_data(datas, config["data"]["columns"], normalise=config["data"]["normalise"])
    with graph.as_default():
        model_result = model.predict_point_by_point(transformed_data)

    model_result = model_result[0, 0]
    base_value = float(datas[0]['close'])
    last_value = float(transformed_data[0, -1, [0]])
    print(type(base_value), type(last_value), last_value)
    trend_by_percentage = 0
    if (model_result != last_value): trend_by_percentage = (model_result - last_value)/(last_value + 1)
    # if (model_result[0, 0] >= transformed_data[0, -1, [0]]):
    #     action = 'buy'
    # else: action = 'sell'
    return trend_by_percentage, (model_result*base_value + base_value)

def addNewCandleToData(candle):
    candles.append(candle)
    dataOut = ""
    for i in config["dataCol"]:
        dataOut += str(candle[i]) + ','
    dataOut += '\n'
    dataFile = open(config["dataName"], 'a')
    dataFile.write(dataOut)
    dataFile.close()

    # return 50 candles
    return candles[-(int(config["sequenceLen"]) - 1):]