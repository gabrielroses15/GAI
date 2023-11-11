import speech_recognition as sr
import pyaudio

def voiceRecord():
    CHUNK = 1024
    RATE = 44100
    CHANNELS = 1
    RECORD_SECONDS = 3

    p = pyaudio.PyAudio()

    recognizer = sr.Recognizer()

    def record_and_recognize():
        stream = p.open(format=pyaudio.paInt16,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        frames = []

        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        audio_data = b''.join(frames)
        audio_chunk = sr.AudioData(audio_data, RATE, 2)

        try:
            recognized_text = recognizer.recognize_google(audio_chunk, language="pt-BR")
            return recognized_text
        except sr.UnknownValueError:
            return ["404", "Não foi possível reconhecer o áudio"]

    recorded_text = record_and_recognize()

    p.terminate()

    return recorded_text