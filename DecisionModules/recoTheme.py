def recognizeTheme(prompt: str, inicio: list = ["quem", "quando", "onde", "por que", "qm", "ond"], verbos: list = ["escreveu", "escrito", "recomendou", "fez"], nomes: list = ["salomão", "davi", "gabriel"]):
    media = False
    def perguntaMedia(frase:str, inicio: list, verbos: list, nomes: list):
        palavras = frase.lower().split()

        if palavras[0] in inicio:
            for verbo in verbos:
                if verbo in palavras:
                    index_verbo = palavras.index(verbo)
                    if len(palavras) - index_verbo <= 7:
                        return True
        if len(frase.split()) < 13:
            contador = 0
            for verbo in verbos:
                for palavra in frase.lower().split():
                    if palavra == verbo:
                        contador += 1
                    else:
                        for nome in nomes:
                            if nome == palavra:
                                contador += 1
            if contador < 8: #valor de 8 apenas para teste (peso 8 teste)
                return True
        return False

    if perguntaMedia(prompt, inicio, verbos, nomes):
        media = True


    carros = ["bmw", "ford", "porshe", "lamborguini", "fusca", "opala", "caminhão", "caminhonete", 
              "caminhao", "ferrari"]#porche porshe dps fzr o corretor
    esportes = ["futebol", "xadrez", "volei", "basquete", "hoquei", "ski"]
    casa = ["casa", "mansão"]
    perguntaSimples = ["quem é você", "qm é vc", "qm é você", "qm é voce", "quem e você", "quem é voce",
                       "o que é vc", "o q é vc", "o que e vc", "oq é vc", "oq e vc", "de onde vc veio",
                       "d ond vc veio", "de onde você veio", "de onde voce veio"]#vc voce você = lista pra ser verificada com {}
    perguntaMedia = []
    perguntaDificil = []
    financas = ["quanto está o bitcoin", "bitcoin", "onde investir", "como investir", 
                "investimentos", "criptomoedas"]
    relacionamento = ["namorada", "namorado", "namo", "amiga", "irma", "irmã", "vó", "vo", "vô", 
                      "tia", "melhor amigo"]#frases com mais de uma palavra 
                                            #Terão que ter uma lógica diferente, 
                                            #Pois não dará certgo comparar uma frase de duas palavras 
                                            #Com uma única palavra, ent talvez eu tenha que implementar 
                                            #O trenzinho com consumo de RAM conntrolado.
    amor = ["amo", "amor", "ama-la"]
    sexo = ["sexo", "transa", "transar", "sequiso"]
    antiNSFW = ["sexo", "transa", "transar", "sequiso"]
    informacoesSimples = [] #"meu nome é {}", ...
    programacao = ["python", "java", "c#", "c++", "html", "css", "tailwind", "cobol"]#Talvez o bot tenha q ter conntato com as coisas e as
                                                  #Estruturas pra ele aprendner a defini-las mesmo q
                                                  #Nunca tenham sido vistas por ele antes, ele entenda
                                                  #A estrutura por inteiro, seu contexto e significado.
    morte = ["morrer", "morte", "suicidio", "suicídio"]
    arte = ["arte", "artista"]#Algumas palavras se trazerem sua sucessora e ela for um nome, ja temos
                                #Oq buscar no banco
    historia = ["napoleao", "bonaparte", "einsten", "einstein", "tesla", "gandi", "jesus", "cristo"] # Certos nomes são históricos e não apenas nomes
    matematica = [] #Número + símbolo matemático + número, funções e/ou formúlas representam matemática
    geografia = ["continente", "rua", "lago", "local", "avenida"]
    portugues = ["verbo", "advérbio", "pronome", "substantivo", "adjetivo"]
    geometria = []
    reflexao = []
    badVibes = []
    solidao = []
    amigos = []
    NPCTalk = []
    Normal = ["quem foi", "quem era", "qm foi" "qm era", "quem foram", "qm foram"]
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
    
    if media:
        BinaryMap[4] = 1
        return "resposta", prompt

    return BinaryMap