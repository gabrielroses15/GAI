import spacy

nlp = spacy.load("pt_core_news_sm") 

prompts = ["Olá bom dia", "Qual é o seu nome?", "Onde você mora?", "Quando você viu isto?", "Como é que é?", "Quanto fica dois desse?", "Por que você não me disse antes"]

def AnalisaFrase(prompt: str):

    doc = nlp(prompt)

    tipo = []
    importantInfo = []

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
        "quanto": ["quanto"],
        "você": ["você", "voce", "vc"]
    }

    for keyword, words in keyWords.items():
        if any(word in prompt.lower() for word in words):
            tipo.append(keyword)
        
    for token in doc:
        if token.dep_ == "nsubj" or token.dep_ == "dobj" or token.ent_type_ == "PER":
            importantInfo.append(token.text)

    return "Tipo: {}\nInformações Importantes: {}".format(", ".join(tipo), ", ".join(importantInfo))

for prompt in prompts:
    resultado = AnalisaFrase(prompt)
    print(resultado)
    print("-" * 30)