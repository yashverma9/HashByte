import pyaudio
import wave
import numpy as np


CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 44100
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "tmp.wav"


p = pyaudio.PyAudio()


for i in range(0, p.get_device_count()):
    print(i, p.get_device_info_by_index(i)['name'])


# stream using as_loopback to get sound from OS
stream = p.open(
    format=FORMAT,
    channels=2,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    input_device_index=2,
    as_loopback=True)

# stream using my Microphone's input device
stream2 = p.open(
    format=FORMAT,
    channels=1,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    input_device_index=1)
# as_loopback=False)


frames = []
frames2 = []


for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    data2 = stream2.read(CHUNK)
    frames.append(data)
    frames2.append(data2)


# frames = as_loopback sound data (Speakers)
frames = b''.join(frames)

# frames2 = sound data of Microphone
frames2 = b''.join(frames2)

# decoding Speaker data
Sdecoded = np.frombuffer(frames, 'int16')

# decoding the microphone data
Mdecoded = np.frombuffer(frames2, 'int16')

# converting Speaker data into a Numpy vector (making life easier when picking up audio channels)
Sdecoded = np.array(Sdecoded, dtype='int16')

# getting the data on the right side
direito = Sdecoded[1::2]

# getting the data on the left side
esquerdo = Sdecoded[::2]

# mixing everything to mono = add right side + left side + Microphone decoded data that is already mono
mix = (direito+esquerdo+Mdecoded)

# ensuring no value goes beyond the limits of short int
signal = np.clip(mix, -32767, 32766)

# encode the data again
encodecoded = wave.struct.pack("%dh" % (len(signal)), *list(signal))


# stop all streams and terminate pyaudio
stream.stop_stream()
stream.close()
stream2.stop_stream()
stream2.close()
p.terminate()


# recording mixed audio in mono
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes((encodecoded))
wf.close()
