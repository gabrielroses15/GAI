def recognizeTheme(prompt):
    carros = {"carros": ["bmw", "ford", "porshe", "lamborguini", "fusca", "opala", "caminhão", "caminhonete", 
              "caminhao", "ferrari"]}#porche porshe dps fzr o corretor
    esportes = {"esportes": ["futebol", "xadrez", "volei", "basquete", "hoquei", "ski"]}
    casa = {"casa": ["casa", "mansão"]}
    perguntaSimples = {"perguntaSimples": ["quem é você", "qm é vc", "qm é você", "qm é voce", "quem e você", "quem é voce",
                       "o que é vc", "o q é vc", "o que e vc", "oq é vc", "oq e vc", "de onde vc veio",
                       "d ond vc veio", "de onde você veio", "de onde voce veio"]}#vc voce você = lista pra ser verificada com {}
    perguntaMedia = {}
    perguntaDificil = {}
    financas = {"financas": ["quanto está o bitcoin", "bitcoin", "onde investir", "como investir", 
                "investimentos", "criptomoedas"]}
    relacionamento = {"relacionamento": ["namorada", "namorado", "namo", "amiga", "irma", "irmã", "vó", "vo", "vô", 
                      "tia", "melhor amigo"]}#frases com mais de uma palavra 
                                            #Terão que ter uma lógica diferente, 
                                            #Pois não dará certgo comparar uma frase de duas palavras 
                                            #Com uma única palavra, ent talvez eu tenha que implementar 
                                            #O trenzinho com consumo de RAM conntrolado.
    amor = {"amor": ["amo", "amor", "ama-la"]}
    sexo = {"sexo": ["sexo", "transa", "transar", "sequiso"]}
    antiNSFW = {"antiNSFW": ["sexo", "transa", "transar", "sequiso"]}
    informacoesSimples = {} #"meu nome é {}", ...
    programacao = {"programacao": ["python", "java", "c#", "c++", "html", "css", "tailwind", "cobol"]}#Talvez o bot tenha q ter conntato com as coisas e as
                                                  #Estruturas pra ele aprendner a defini-las mesmo q
                                                  #Nunca tenham sido vistas por ele antes, ele entenda
                                                  #A estrutura por inteiro, seu contexto e significado.
    morte = {"morte": ["morrer", "morte", "suicidio", "suicídio"]}
    arte = {"arte": ["arte", "artista"]}#Algumas palavras se trazerem sua sucessora e ela for um nome, ja temos
                                #Oq buscar no banco
    historia = {"historia": ["napoleao", "bonaparte", "einsten", "einstein", "tesla", "gandi", "jesus", "cristo"]} # Certos nomes são históricos e não apenas nomes
    matematica = {} #Número + símbolo matemático + número, funções e/ou formúlas representam matemática
    geografia = {"geografia": ["continnente", "rua", "lago", "local", "avenida"]}
    portugues = {"portugues": ["verbo", "advérbo", "pronome", "substantivo", "adjetivo"]}
    geometria = {}
    reflexao = {}
    badVibes = {}
    solidao = {}
    amigos = {}
    NPCTalk = {}
    temas = [carros, esportes, casa, perguntaSimples, perguntaMedia, perguntaDificil, 
             financas, relacionamento, amor, sexo, antiNSFW, informacoesSimples, programacao,
             morte, arte, historia, matematica, geografia, portugues, geometria, reflexao, badVibes,
             solidao, amigos, NPCTalk]
    
    palavras = prompt.lower().split()

    recoThemes = []

    for palavra in palavras:
        for tema in temas:
            for valor, frases in tema.items():
                for frase in frases:
                    if frase == palavra:
                        recoThemes.append(valor)
                        #print("o tema é: {}\nele foi reconhecido pela palavra:{}".format(valor, palavra))
    return recoThemes