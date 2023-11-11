from youtube_transcript_api import YouTubeTranscriptApi

def transcrever_video(url):
    video_id = url.split('v=')[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

    texto_transcrito = ""
    for linha in transcript:
        texto_transcrito += linha['text'] + "\n"

    return texto_transcrito

# Exemplo de uso
url_do_video = "https://www.youtube.com/watch?v=BWVyp0wYpgA&ab_channel=GrantCollins"
transcricao = transcrever_video(url_do_video)
print(transcricao)
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

import spacy

# Carregando o modelo de linguagem
nlp = spacy.load('pt_core_news_sm')

# Processando o texto com SpaCy
doc = nlp(transcricao)

# Obtendo as sentenças mais importantes
frases_importantes = [sent.text for sent in doc.sents if any(token.is_stop for token in sent)]

# Gerando o sumário
sumario = ' '.join(frases_importantes[:3])  # Exemplo: Pegando as 3 primeiras sentenças importantes

print(sumario)