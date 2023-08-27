import spacy

nlp = spacy.load("pt_core_news_sm")

# Tokenização

texto = nlp(u'Eu estou aprendendo a utilizar chatBots')

for token in texto:
    print(token.text, token.pos_)
    
print()

# Atributos do token
    
texto2 = nlp(u'O canal do "Dark" está chegando a 11,1 inscritos.')
for token in texto2:
    print("- Texto:", token.text, " - Forma raiz:", token.lemma_, "Tipo da palavra:", token.pos_, "É letra:", token.is_alpha)
    
# Buscando semelhanças
print()

texto3 = input("Como posso te ajudar no dia de hoje?")
texto3 = nlp(texto3)

for token1 in texto3:
    for token2 in texto3:
        similaridade = round((token1.similarity(token2) * 100),2)
        print("A palavra: {} é {}% similar a palavra {}".format(token1.text,similaridade,token2.text))
        
# Buscando similaridade e comparando com as REGRAS do meu chatbot (KeyWords) dá pra comparar com temas.
print()

texto4 = input("Como posso te ajudar no dia de hoje?")
texto4 = nlp(texto4)
comparar = nlp("conhecimento")

for token in texto4:
    similaridade = round((token.similarity(comparar) * 100),2)
    if similaridade == 100:
        print("A palavra: {} é {}% similar a palavra {}".format(token.text,similaridade,comparar))
    elif similaridade >= 39 and similaridade < 100:
        pergunta_similaridade = input("Você está em busca de conhecimento? s/n")
        if pergunta_similaridade.lower() == "s":
            print("A palavra: {} é {}% similar a palavra {}".format(token.text,similaridade,comparar))
        else:
            print("Ok, por favor refaça sua pergunta")
    else:
        print("Ok, por favor refaça sua pergunta")