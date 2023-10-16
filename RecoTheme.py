import spacy
import re

nlp = spacy.load("pt_core_news_sm")

def remove_numeros(texto):
    # Use uma expressão regular para substituir todos os números por espaços em branco
    return re.sub(r'\d', ' ', texto)

def RecoKeys(texto, usar_nlp=False):  # Renomeado o parâmetro para evitar conflito de nomes
    texto = remove_numeros(texto)  # Remove números do texto

    if usar_nlp:  # Usar o parâmetro renomeado
        Tema = None  # Inicialize o tema como None
        texto4 = nlp(str(texto))
        Themes = ['esportes', 'religião', 'aprender', 'dinheiro', 'relacionamento', 'sexo', 'sentimentos']
        for theme in Themes:
            theme = nlp(theme)
            for token in texto4:
                similaridade = round((token.similarity(theme) * 100), 2)
                if similaridade == 100:
                    return theme.text  # Retorna o texto do tema encontrado
                elif similaridade >= 33 and similaridade < 100:
                    return theme.text  # Retorna o texto do tema encontrado
        return "Null"  # Retorna "Null" se nenhum tema for encontrado
    else:
        Tema = "Null"
        texto4 = nlp(str(texto))
        Themes = ['esportes', 'religião', 'aprender', 'dinheiro', 'relacionamento', 'sexo', 'sentimentos']
        for theme in Themes:
            theme = nlp(theme)
            for token in texto4:
                similaridade = round((token.similarity(theme) * 100), 2)
                if similaridade == 100:
                    print("A palavra: {} é {}% similar a palavra {}".format(token.text, similaridade, theme))
                    Tema = "Null"
                elif similaridade >= 33 and similaridade < 100:
                    print("A palavra: {} é {}% similar a palavra {}".format(token.text, similaridade, theme))
                    Tema = "Null"
                else:
                    Tema = "Null"
            if Tema == "Null":
                break
        if Tema == False:
            print("Não encontrei tema na palavra.")
