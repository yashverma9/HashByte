#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable
cnt = 1
while (cnt <= 1):
    # with sr.AudioFile('output{}.wav'.format(cnt)) as source:
    with sr.AudioFile('OSR_uk_000_0020_8k.wav') as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio_text = r.record(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:

            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)

        except:
            print('Sorry.. run again...')
    cnt = cnt + 1
