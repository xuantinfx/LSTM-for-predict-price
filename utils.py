import random
import json

global config

with open('config.json', 'r') as f:
    config = json.load(f)

def predict(data):
    actions = ['sell', 'buy']
    return actions[random.randrange(0,100) % 2]

def addNewCandleToData(candle):
    dataOut = ""
    for i in config["dataCol"]:
        dataOut += str(candle[i]) + ','
    dataOut += '\n'
    dataFile = open(config["dataName"], 'a')
    dataFile.write(dataOut)
    dataFile.close()