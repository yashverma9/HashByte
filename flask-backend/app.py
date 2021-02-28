from flask import Flask, jsonify, request
import json
import sys
import pyaudio
import wave
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from flask_cors import CORS

original_stdout = sys.stdout
app = Flask(__name__)
CORS(app)
app.static_folder = 'static'
app.secret_key = 'the random string'

test_data = [{"color": "red"}, {"color": "blue"}, {"color": "pink"}]


# apikey = '-XOpPXfHPTI5jnjjyQprxFoh5NFcDpY1CjdZ6Atnjubn'
# url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/cf343907-bfbf-4fda-b324-0c3b1eab5cff'

# # Setup Service
# authenticator = IAMAuthenticator(apikey)
# stt = SpeechToTextV1(authenticator=authenticator)
# stt.set_service_url(url)


# # Function for generating live audio clips
# def recording():
#     CHUNK = 1024
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 2
#     RATE = 44100
#     RECORD_SECONDS = 10
#     WAVE_OUTPUT_FILENAME = "output.wav"

#     p = pyaudio.PyAudio()

#     stream = p.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK)

#     print("* recording")

#     frames = []

#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)

#     print("* done recording")

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()


# print(sample_data[0]["selected"])

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
        json.dump(sample_data, f)
    return jsonify({"msg": "success"})


@app.route('/api/postNote')
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
    return jsonify({"msg": "success"})

'''
@app.route('/api/getRealTimeItems')
def getRealTimeItems():
    recording()
    id_a = request.args['id']
    if id_a == "5":
        return jsonify({"msg": "end"})    
    with open('output.wav', 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/wav',
                            model='en-US_NarrowbandModel', continuous=True).get_result()

    text = ""
    for i in range(0, len(res['results'])):
        text += res['results'][i]['alternatives'][0]['transcript']
    print(text)
    if text == "":
        return jsonify({"msg": "end"})
    else:
        with open('real-data.json') as json_file:
            data = json.load(json_file)

        data["data"].append({"id": id_a, "text": text})
        with open('real-data.json', 'w') as f:
            json.dump(data, f)
        return jsonify(data)
'''



@app.route('/api/getRealTimeItems')
def getRealTimeItems():
    id_a = request.args['id']
    if id_a == "7":
        return jsonify({"msg": "end"})    
    with open('sample-audio.json') as json_file:
            audio = json.load(json_file)
    
    #for i in audio:
    #    if i["id"] == id_a:
    text = audio[int(id_a)-1]
    print(text)
    if text == "":
        return jsonify({"msg": "end"})
    else:
        with open('real-data.json') as json_file:
            data = json.load(json_file)

        data["data"].append(text)
        with open('real-data.json', 'w') as f:
            json.dump(data, f)
        return jsonify(data)



@app.route('/api/getCurrentItem')
def getCurrenItem():
    idx = request.args['id']
    print(idx)
    with open('sample-data.json') as f:
        sample_data = json.load(f)
    return jsonify(sample_data[int(idx)-1])


if __name__ == "__main__":
    app.run(debug=True)
