from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = '-XOpPXfHPTI5jnjjyQprxFoh5NFcDpY1CjdZ6Atnjubn'
url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/cf343907-bfbf-4fda-b324-0c3b1eab5cff'

# Setup Service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# Perform conversion
k = 9
while k <= 12:
    with open('output{}.wav'.format(k), 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/wav',
                            model='en-US_NarrowbandModel', continuous=True).get_result()

    text = ""
    for i in range(0, len(res['results'])):
        text += res['results'][i]['alternatives'][0]['transcript']
    print(text)

    k = k + 1
