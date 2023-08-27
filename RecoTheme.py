import spacy

nlp = spacy.load("pt_core_news_sm")

def RecoKeys(texto):
    Tema = False
    texto4 = nlp(texto)
    Themes = ['esportes', 'religião', 'aprender', 'dinheiro', 'relacionamento', 'sexo', 'sentimentos']
    for theme in Themes:
        theme = nlp(theme)
        for token in texto4:
            similaridade = round((token.similarity(theme) * 100),2)
            if similaridade == 100:
                print("A palavra: {} é {}% similar a palavra {}".format(token.text,similaridade,theme))
                Tema = True
            elif similaridade >= 33 and similaridade < 100:
                print("A palavra: {} é {}% similar a palavra {}".format(token.text,similaridade,theme))
                Tema = True
            else:
                Tema = False
        if Tema == True:
            break
    if Tema == False:
        print("Não encontrei tema na palavra.")