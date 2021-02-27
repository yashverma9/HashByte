from flask import Flask, jsonify, request
import json
import sys

original_stdout = sys.stdout
app = Flask(__name__)
app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'the random string'

test_data = [{"color": "red"},{"color": "blue"},{"color": "pink"}]


#print(sample_data[0]["selected"])

@app.route('/api/getAllItem')
def getAllJson():
    with open('sample-data.json') as f:
        sample_data = json.load(f)
    return jsonify(sample_data) 


@app.route('/api/saveItem', methods = ["POST"])
def saveItem():
    id_a = request.form.get('id')
    with open('sample-data.json') as f:
         sample_data = json.load(f)
    for inst in sample_data:
        if inst["id"] == id_a:
            inst["selected"] = "1"
    with open('sample-data.json', 'w') as f:
        json.dump(sample_data, f)
    return jsonify({"msg":"success"})


@app.route('/api/getCurrentItem')
def getCurrenItem():
    with open('sample-data.json') as f:
        sample_data = json.load(f)
    return jsonify(sample_data[1])

@app.route('/api/postNote',  methods = ["POST"])
def postNote():
    id_a = request.form.get('id')
    note = request.form.get('note')
    with open('sample-data.json') as f:
        sample_data = json.load(f)    
    for inst in sample_data:
        if inst["id"] == id_a:
            inst["note"] = note
    with open('sample-data.json', 'w') as f:
        json.dump(sample_data, f)
    return jsonify({"msg":"success"})
 
if __name__ == "__main__":
    app.run(debug=True)
