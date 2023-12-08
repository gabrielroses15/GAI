def recognizeTheme(prompt: str, inicio: list = ["quem", "quando", "onde", "por que", "qm", "ond"], verbos: list = ["escreveu", "escrito", "recomendou", "fez"], nomes: list = ["salomão", "davi", "gabriel"]):


    carros = ["bmw", "ford", "porshe", "lamborguini", "fusca", "opala", "caminhão", "caminhonete", 
              "caminhao", "ferrari"]
    esportes = ["futebol", "xadrez", "volei", "basquete", "hoquei", "ski"]
    casa = ["casa", "mansão"]
    perguntaSimples = ["quem é você", "qm é vc", "qm é você", "qm é voce", "quem e você", "quem é voce",
                       "o que é vc", "o q é vc", "o que e vc", "oq é vc", "oq e vc", "de onde vc veio",
                       "d ond vc veio", "de onde você veio", "de onde voce veio"]
    perguntaMedia = ["quantos"]
    perguntaDificil = ["por que que a vida é tão difícil", "pq que a vida é tão difícil", "por quê que a vida é tão difícil", "porque que a vida é tão difícil", "porquê que a vida é tão difícil", "por que a vida é tão difícil", "pq a vida é tão difícil", "por quê a vida é tão difícil", "porque a vida é tão difícil", "porquê a vida é tão difícil"]
    financas = ["quanto está o bitcoin", "bitcoin", "onde investir", "como investir", 
                "investimentos", "criptomoedas"]
    relacionamento = ["namorada", "namorado", "namo", "amiga", "irma", "irmã", "vó", "vo", "vô", 
                      "tia", "melhor amigo"]
    amor = ["amo", "amor", "ama-la"]
    sexo = ["sexo", "transa", "transar", "sequiso"]
    antiNSFW = ["sexo", "transa", "transar", "sequiso"]
    informacoesSimples = [] #"meu nome é {}", ...
    programacao = ["python", "java", "c#", "c++", "html", "css", "tailwind", "cobol"]
    morte = ["morrer", "morte", "suicidio", "suicídio"]
    arte = ["arte", "artista"]
    historia = ["napoleao", "bonaparte", "einsten", "einstein", "tesla", "gandi", "jesus", "cristo"]
    matematica = []
    geografia = ["continente", "rua", "lago", "local", "avenida"]
    portugues = ["verbo", "advérbio", "pronome", "substantivo", "adjetivo"]
    geometria = []
    reflexao = []
    badVibes = []
    solidao = []
    amigos = []
    NPCTalk = []
    Normal = ["quem foi", "quem era", "qm foi" "qm era", "quem foram", "qm foram", "quem", "quando", "onde", "por que", "qm", "ond", "quantos", "que"]
    temas = [carros, esportes, casa, perguntaSimples, perguntaMedia, perguntaDificil, 
             financas, relacionamento, amor, sexo, antiNSFW, informacoesSimples, programacao,
             morte, arte, historia, matematica, geografia, portugues, geometria, reflexao, badVibes,
             solidao, amigos, NPCTalk, Normal]
    
    palavras = prompt.lower().split()

    BinaryMap = []

    for tema in temas:
        add = 0
        for frase in tema:
            if " " in frase:
                if frase in prompt.lower():
                    add = 1
                    break
            else:
                for palavra in palavras:
                    if palavra == frase:
                        add = 1
        BinaryMap.append(add)

    return BinaryMap