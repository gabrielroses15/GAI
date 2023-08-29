prompts = ["Olá bom dia", "Qual é o seu nome?", "Onde você mora?", "Quando você viu isto?", "Como é que é?", "Quanto fica dois desse?", "Por que você não me disse antes"]

def AnalisaFrase(prompt: str):

    tipo = []

    keyWords = {
        "saudacao": ["oi", "oii", "oie", "olá", "ola", "eae"],
        "dia": ["bom dia"],
        "tarde": ["boa tarde"],
        "noite": ["boa noite"],
        "qual": ["qual"],
        "onde": ["onde"],
        "quando": ["quando"],
        "como": ["como"],
        "porque": ["porque", "porquê", "pq"],
        "quanto": ["quanto"]
    }

    for keyword, words in keyWords.items():
        if any(word in prompt.lower() for word in words):
            tipo.append(keyword)
    
    return " e ".join(tipo)
    
    dia = False
    tarde = False
    noite = False
    qual = False
    quando = False
    como = False
    porque = False
    quanto = False
    onde = False
    saudacao = False
    informacao = False
    dupla = False
    separador = ""
    tipos = []

    if "bom dia" in prompt:
        dia = True
    if "boa tarde" in prompt:
        tarde = True
    if "boa noite" in prompt:
        noite = True

    prompt = prompt.lower()
    prompt = prompt.replace("por que", "porque")
    prompt = prompt.replace("por quê", "porquê")
    prompt = prompt.split(" ")

    for frase in prompt:
        frase = frase.lower()
        if "qual" in frase:
            qual = True
        if "onde" in frase:
            onde = True
        if "quando" in frase:
            quando = True
        if "como" in frase:
            como = True
        if "porque" in frase or "porquê" in frase or "pq" in frase:
            porque = True
        if "quanto" in frase:
            quanto = True
        if "oi" in frase or "oii" in frase or "oie" in frase or "olá" in frase or "ola" in frase or "eae" in frase:
            saudacao = True

    if qual == True or onde == True or quando == True or como == True or porque == True or quanto == True:
        tipos.append("pergunta")
        dupla = True
    if saudacao == True and dupla == False:
        frase = "saudação"
        if dia:
            frase = "saudaçãoDia"
        if tarde:
            frase = "saudaçãoTarde"
        if noite:
            frase = "saudaçãoNoite"
        tipos.append(frase)
        dupla = True
    elif saudacao == True and dupla == True:
        tipos.append(" e saudacão")
    if informacao == True and dupla == False: #falta identificar qual informação é útil
        tipos.append("informação")
        dupla = True
    if informacao == True and dupla == True:
        tipos.append(" e informação")
    
    tipos = separador.join(tipos)
    #Retorna os tipos encontrados nos tokens
    return tipos

for prompt in prompts:
    print(AnalisaFrase(prompt))