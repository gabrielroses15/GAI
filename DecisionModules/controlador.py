from DecisionModules import ArvoreDeDecisao as choose
from DecisionModules import recoTheme as Theme
def controller(prompt:str):
    tema = Theme.recognizeTheme(prompt)
    print(tema)

    resposta = "Por favor reformule."

    resposta = choose.choose(prompt, resposta)

    return resposta