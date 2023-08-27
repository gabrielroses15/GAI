from gtts import gTTS
import pygame
import io

def AwnswerAudio(resposta):
    # Criar um objeto gTTS com o texto e o idioma desejado
    tts = gTTS(text=resposta, lang='pt-br')

    # Criar um buffer para armazenar o áudio
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)

    # Inicializar o módulo de áudio do pygame
    pygame.mixer.init()

    # Carregar o áudio do buffer
    audio_buffer.seek(0)
    pygame.mixer.music.load(audio_buffer)

    # Reproduzir o áudio
    pygame.mixer.music.play()

    # Aguardar até que o áudio termine de ser reproduzido
    while pygame.mixer.music.get_busy():
        pass