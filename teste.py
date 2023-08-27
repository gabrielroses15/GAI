import spacy

def RecoNome(text):
    nlp = spacy.load("pt_core_news_sm")

    texto = nlp(text)

    for token in texto:
        if token.pos_ == "PROPN":
            return token.text