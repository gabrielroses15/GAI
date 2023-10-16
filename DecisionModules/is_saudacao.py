from DecisionModules import translate_en as trad

#VerificaSaudação en
def is_saudacao(prompt):
    import spacy
    nlp = spacy.load("pt_core_news_lg")
    doc = nlp(prompt.lower())
    
    saudacoes = ["hi", "hello", "hey"]
    
    for token in doc:
        if token.text in saudacoes:
            return True
    
    return False

def VerificaSaudação(prompt: str):
    promptTraduzido = trad.trad(prompt)
    
    saudacao = is_saudacao(promptTraduzido)
    return saudacao