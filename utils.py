import random
import json
import csv

global config
candles = []

with open('config.json', 'r') as f:
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

def predict(datas):
    # Chỗ này sẽ load model lên và tiến hành predict
    actions = ['sell', 'buy']
    return actions[random.randrange(0,100) % 2]

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
    return candles[-int(config["sequenceLen"]):]