from DecisionModules import ArvoreDeDecisao as choose
def controller(prompt:str):
    resposta = "Por favor reformule."

    resposta = choose.choose(prompt, resposta)

    return resposta