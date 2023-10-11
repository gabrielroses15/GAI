import speech_recognition as sr
import RecoResposta_Fala
import pyaudio

def voiceRecord(passagem):
    CHUNK = 1024
    RATE = 44100
    CHANNELS = 1
    RECORD_SECONDS = 3

    p = pyaudio.PyAudio()

    recognizer = sr.Recognizer()

    def record_and_recognize():
        if passagem == True:
            print("Comece a falar...")
        else:
            print("Responda:")
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
            if passagem == True:
                RecoResposta_Fala.BuildAwnswer(str(recognized_text).lower())
            else:
                return recognized_text
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio")

    recorded_text = record_and_recognize()

    p.terminate()

    return recorded_text