from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator

def CalcFeeling(text):

    def pt_to_english(texto):
        translator = Translator()
        translated_text = translator.translate(texto, src='pt', dest='en')
        return translated_text.text

    # Traduz a frase completa para inglês
    translated_text = pt_to_english(text)

    # Inicializar o SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    # Analisar o sentimento da frase traduzida
    sentiment_scores = sia.polarity_scores(translated_text)
    sentiment = sentiment_scores['compound']

    if sentiment >= 0.05:
        sentiment_label = "Positivo:"
    elif sentiment <= -0.05:
        sentiment_label = "Negativo:"
    else:
        sentiment_label = "Neutro:"
    
    return sentiment_label, sentiment