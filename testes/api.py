class decisoes:

    #translate_en
    def trad(text):
        from googletrans import Translator
        translator = Translator()
        translated_text = translator.translate(text, src='auto', dest='en').text
        return translated_text

    #VerificaSaudação
    def is_saudacao(prompt):
        import spacy
        nlp = spacy.load("pt_core_news_lg")
        doc = nlp(prompt.lower())
        
        saudacoes = ["hi", "hello", "hey"]
        
        for token in doc:
            if token.text in saudacoes:
                return True
        
        return False

    # Início da árvore de Decisão:

    def choose(prompt=str):
        #Criando uma lista de tipos, buscando otimização no entendimento do contexto.
        #Considero que seja melhor dar um append do que verificar tipo a tipo.
        tipos = []

        maybeQuestion = []

        #Dicionário de palavras
        key_saudacoes =  ["oiee","oie","oii","oi","eae","olá","ola","salve","e ai","e aí","saudações", 
                    "saudaçoes", "saudacões", "saudacoes", "saudacao", "saudacão"]
        
        key_question = ["quem", "como", "quando", "pq", "onde", "qual"] #final ia "gostaria" "ficaria", porem tem certas chances dependendo do contexto, "eu ficaria com ela mas..." "eu ficaria fazendo?"

        key_thx = ["obrigado", "valeu", "obrigada", "vlw"]

        key_pronome = ["eu", "tu", "ele", "nós", "vós", "eles", "ela"]

        resultado = []

        dicio = [key_saudacoes, key_question, key_thx]
        
        #Início padrão
        start = "considerando sua frase, "
        saudacao = "Olá, "

        #Verificações baseadas no dicionário

        tamanho_prompt = prompt.split()
        if len(tamanho_prompt) == 1:
            if prompt in key_saudacoes:
                print(prompt.title() + ", Por favor reformule sua frase")
            elif prompt in key_thx:
                print("Denada!")
            elif prompt in key_question:
                print("Por favor, termine de escrever sua pergunta.")
            else:
                print('Vc escreveu "{}", pode reformular por favor?'.format(prompt))
        else:
            palavras = prompt.split()
            for palavra in palavras:
                for lista in dicio:
                    if palavra.lower() in lista:
                        if lista == key_saudacoes:
                            tipos.append("saudacao")
                            saudacao = palavra.title() + ", "
                        elif lista == key_question:
                            tipos.append("question")
                        elif lista == key_thx:
                            tipos.append("thx")
                        break
                if palavra.lower().endswith("ia"):
                    maybeQuestion.append(palavra)
                    
        
        palavras = prompt.split()
        for i, palavra in enumerate(palavras):
            if palavra.lower().endswith("ia"):
                verbo = palavra.lower()
                for j in range(i-1, -1, -1):
                    if palavras[j].lower() in key_pronome:
                        pronome_contexto = palavras[j].lower()
                        contexto.insert(0, palavras[j])
                        pronome_encontrado = palavras[j]
                        break
                    contexto.insert(0, palavras[j])
                contexto.append(verbo)
                break
        
        if "thx" in tipos and "question" in tipos:
            start = "Fico feliz em ajudar, considerando sua pergunta, "
        elif "thx" in tipos:
            start = "Fico feliz em ajudar você!"
        elif "question" in tipos:
            start = "Considerando sua pergunta, "
        
        #Verifica dia/tarde/noite

        if "bom dia" in prompt.lower():
            tipos.append("dia")

        if "boa tarde" in prompt.lower():
            tipos.append("tarde")

        if "boa noite" in prompt.lower():
            tipos.append("noite")

        
        #Construção do "start"

        if "thx" in tipos:
            start = start
        else:
            start = saudacao + start

        print("tipo = {}\n Start = {}".format(tipos, start))
        print(maybeQuestion)