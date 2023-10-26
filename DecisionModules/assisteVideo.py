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