#Dicionário de palavras
key_saudacoes =  ["oiee","oie","oii","oi","eae","olá","ola","salve","e ai","e aí","saudações", 
            "saudaçoes", "saudacões", "saudacoes", "saudacao", "saudacão"]

key_question = ["quem", "como", "quando", "pq", "onde", "qual"] #final ia "gostaria" "ficaria", porem tem certas chances dependendo do contexto, "eu ficaria com ela mas..." "eu ficaria fazendo?"

key_thx = ["obrigado", "valeu", "obrigada", "vlw"]

dicio = [key_saudacoes, key_question, key_thx]
def verificaByDicio(prompt, tipos, saudacao):
    wordsQuestion = []
    palavras = prompt.split()
    context_size = 3  # Tamanho do contexto considerado (ele + 1 ja q inicia em 0)
    #Criando uma certa análise de contexto considerando palavras a frente e a trás da que está sendo analizada, quanto mais words mais processamento e memória serão utilizados
    #Porém melhor será o entendimento sobre frases grandes
    
    for indice, palavra in enumerate(palavras):
        context = ' '.join(palavras[indice:indice+context_size+1])
        for lista in dicio:
            if palavra.lower() in lista:
                if lista == key_saudacoes:
                    tipos.append("saudacao")
                    saudacao = palavra.title() + ", "
                elif lista == key_question and "quando me deparei" not in context: #Provavelmente terei uma lista de "blackPhrases" pra serem desconsideradas
                    tipos.append("question")
                    wordsQuestion.append(palavra)
                elif lista == key_thx:
                    tipos.append("thx")
                break
        indice += 1
    if len(wordsQuestion) == 1:
        wordsQuestion = str(wordsQuestion)
    else:
        for word in wordsQuestion:
            wordsQuestion = " ".join(word)
    return tipos, saudacao, wordsQuestion