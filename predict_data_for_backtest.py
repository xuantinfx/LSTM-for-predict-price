import random
import json
import csv
import tensorflow as tf
from model.core.model import Model
from model.core.data_processor import DataLoader
import utils_flask_server as utils

global config
candles = []

with open('config_flask.json', 'r') as f:
    config = json.load(f)

with open("model/data/Data_Backtest.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    pass_header = False
    for row in csv_reader:
        if(pass_header):
            i = 0
            candle = {}
            for key in config['dataCol']:
                candle[key] = row[i]
                i += 1
            candles.append(candle)
        else: pass_header = True

model = Model()
model.load_model(config["nameModel"])
global graph
graph = tf.get_default_graph()

dataLoader = DataLoader(
    "model/data/Data_Backtest.csv",
    config['data']['train_test_split'],
    config['data']['columns']
)

def main():
    results = []
    for i in range(49, len(candles)):
        print(i)
        result = utils.predict(candles[i - 49:i], 5)
        for temp in range(len(result)):
            result[temp] = str(result[temp])
        results.append({
            "start": candles[i]["start"],
            "result": result,
        })
    outfile = open ('Result_Backtest.json', 'w')
    json.dump(results, outfile)
    

if __name__ == "__main__":
    main()