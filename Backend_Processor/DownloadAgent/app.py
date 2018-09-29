from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/getConfig', methods=['GET'])
def getConfig():
    return jsonify(getConfigData()), 200

@app.route('/updateConfig',methods=['POST'])
def updateConfig():
    if request.method == 'POST':
        content = request.get_json()
        updateConfigFile(content)
        return jsonify(content), 201

def updateConfigFile(content):
    with open('config.json', 'w+') as configFile:
        configFile.write(json.dumps(content))
        configFile.close()

def getConfigData():
    with open('config.json', 'r') as configFile:
        data = json.load(configFile)
        configFile.close()
    return data