def Carro(prompt:str, resposta):
    if "quais são os carros" in prompt:
        resposta = "carros " + prompt.split()[-2] + " " + prompt.split()[-1]
    return resposta