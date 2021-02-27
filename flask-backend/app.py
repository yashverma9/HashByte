from flask import Flask, jsonify, request
import json
import sys

original_stdout = sys.stdout
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


@app.route('/api/saveItem', )
def saveItem():
    id_a = request.args['id']
    print("saveitem")
    print(id_a)
    with open('sample-data.json') as f:
         sample_data = json.load(f)
    for inst in sample_data:
        if inst["id"] == id_a:
            inst["selected"] = "1"
    with open('sample-data.json', 'w') as f:
        json.dump(sample_data, f )
    return jsonify({"msg":"success"})

@app.route('/api/postNote',  )
def postNote():
    id_a = request.args['id']
    note = request.args['note']
    print("postnote")
    print(id_a)
    print(note)
    with open('sample-data.json') as f:
        sample_data = json.load(f)    
    for inst in sample_data:
        if inst["id"] == id_a:
            inst["note"] = note
    with open('sample-data.json', 'w') as f:
        json.dump(sample_data, f)
    return jsonify({"msg":"success"})

@app.route('/api/getCurrentItem'  )
def getCurrenItem():
    idx = request.args['id']
    print(idx)
    with open('sample-data.json') as f:
        sample_data = json.load(f)
    return jsonify(sample_data[int(idx)-1])

if __name__ == "__main__":
    app.run(debug=True)
