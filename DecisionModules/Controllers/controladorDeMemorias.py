def retornaDicioAnterior(complexity:int):
    return returnoDicioVerbosoToBinaryMap(complexity-1)

def returnoDicioVerbosoToBinaryMap(complexity:int):
    complexidadeMaximaMapeada = 2
    if complexity == 0:
        dicioBinaryMap = {
            "carros": ["bmw", "ford", "porshe", "lamborguini", "fusca", "opala", "caminhão", "caminhonete", 
                "caminhao", "ferrari"],
            "esportes": ["futebol", "xadrez", "volei", "basquete", "hoquei", "ski"],
            "casa": ["casa", "mansão"],
            "perguntaSimples": ["quem é você", "qm é vc", "qm é você", "qm é voce", "quem e você", "quem é voce",
                        "o que é vc", "o q é vc", "o que e vc", "oq é vc", "oq e vc", "de onde vc veio",
                        "d ond vc veio", "de onde você veio", "de onde voce veio"],
            "perguntaMedia": ["quantos"],
            "perguntaDificil": ["por que que a vida é tão difícil", "pq que a vida é tão difícil", "por quê que a vida é tão difícil", "porque que a vida é tão difícil", "porquê que a vida é tão difícil", "por que a vida é tão difícil", "pq a vida é tão difícil", "por quê a vida é tão difícil", "porque a vida é tão difícil", "porquê a vida é tão difícil"],
            "financas": ["quanto está o bitcoin", "bitcoin", "onde investir", "como investir", 
                    "investimentos", "criptomoedas"],
            "relacionamento": ["namorada", "namorado", "namo", "amiga", "irma", "irmã", "vó", "vo", "vô", 
                        "tia", "melhor amigo"],
            "amor": ["amo", "amor", "ama-la"],
            "sexo": ["sexo", "transa", "transar", "sequiso"],
            "antiNSFW": ["sexo", "transa", "transar", "sequiso"],
            "informacoesSimples": [], #"meu nome é {}", ...
            "programacao": ["python", "java", "c#", "c++", "html", "css", "tailwind", "cobol"],
            "morte": ["morrer", "morte", "suicidio", "suicídio"],
            "arte": ["arte", "artista"],
            "historia": ["napoleao", "bonaparte", "einsten", "einstein", "tesla", "gandi", "jesus", "cristo"],
            "geografia": ["continente", "rua", "lago", "local", "avenida"],
            "portugues": ["verbo", "advérbio", "pronome", "substantivo", "adjetivo"],
            "geometria": ["seno", "coseno", "tangente"],
            "matematica": ["soma", "multiplicação", "divisão", "potenciação"],
            "reflexao": ["se o", "sera que o"],# se o .... entao ...
            "badVibes": ["triste", "choro", "refletindo"],
            "solidao": ["sozinho", "sem ngm"],
            "amigos": ["meus amigos", "meu amigo"],
            "NPCTalk": ["oi", "tudo bem", "bom dia", "boa noite"],
            "Normal": ["quem foi", "quem era", "qm foi" "qm era", "quem foram", "qm foram", "quem", "quando", "onde", "por que", "qm", "ond", "quantos", "que"]
        }
        return dicioBinaryMap
    elif complexity == 1:
        dicio1 = retornaDicioAnterior(complexity)
        dicio1["carros"].append("camaro")
        return dicio1
    elif complexity == 2:
        dicio1 = retornaDicioAnterior(complexity)
        dicio1["amigos"].append("amigar")
        return dicio1
    if complexity > complexidadeMaximaMapeada:
        return retornaDicioAnterior(complexity)

def retornoDaGeografia():
    return ["avenida", "rua", "local", "quadra", "mercado", "hospital", "praça"]

def getActionVerbs():
    return {0.62: "recomendar", 0.70: "falar",
                 0.80: "fazer", 0.751: "ir", 0.75: "ter",
                 0.78: "ser", 0.50: "estar", 0.59: "poder",
                 0.63: "dizer", 0.619: "ver", 0.64: "dar",
                 0.65: "saber", 0.60: "coseguir", 0.785: "escrever",
                 0.81: "produzir", 0.82: "criar"}
def getInfinitiveVerbs():
    return ["recomendar", "falar", "fazer", "ir", "ter", "ser", "estar",
             "poder", "dizer", "ver", "dar", "saber", "coseguir", "escrever",
            "produzir"]