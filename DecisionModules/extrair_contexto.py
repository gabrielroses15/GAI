from DecisionModules import verificaByDicio as vbd

#Função para Contar palavras
def verifica_palavras(prompt):
    # Separa o prompt em palavras usando espaço como delimitador
    palavras = prompt.split()
    
    # Verifica o número de palavras
    if len(palavras) > 1:
        return True
    else:
        return False

#Função pra retirar o contexto da frase
def extrair_contexto(prompt: str, saudacao: str, tipos):
    fraseOrPalavra = verifica_palavras(prompt)
    if fraseOrPalavra:
        import spacy
        nlp = spacy.load("pt_core_news_lg")
        doc = nlp(prompt.lower())
        pron = ["eu", "tu", "ele", "nós", "vós", "eles", "nos", "vos", "nois", "você", "vc", "voce", "ela", "elx", "ela", "vocês", "vcs", "voces"]
        nomes = ["salomão", "miguel", "gabriel",
        "lucas", "joão", "davi", "pedro", "enzo",
        "gustavo", "eduardo", "nicolas", "yuri", "caio", "vitor",
        "antonio", "vinicius", "william", "paulo",
        "daniel", "marcos", "fernando", "rodrigo", "anderson",
        "andre", "julio", "renan", "valmir",
        "luis", "leonardo", "fabio", "nome", "arthur", "giovanna", "lais", "marina", "raissa", "thiago", "laura",
        "laisa", "sophia", "joao", "henrique", "samuel", "matheus", "luiza",
        "marcela", "leticia", "beatriz", "mirella", "clara", "isabella", "livia",
        "mateus", "guilherme", "marcelo", "jose", "gabriela", "rafaela", "raul",
        "gabrielle", "julia", "victor", "valentina", "viviane", "isabel", "isabelle", "thais",
        "nathalia", "nathalie", "diego", "bruno", "vivian", "marcio", "amanda", "carolina", "erica", "hugo", "joaquin",
        "karina", "lucia", "mario", "nadia", "patricia", "rafael", "sergio", "tomas",
        "ursula", "viviana", "yolanda", "sebastian", "valeria", "xavier",
        "martin", "pablo", "natalia", "manuel", "francisco",
        "ricardo", "veronica", "felipe", "alejandro", "carlos", "fernanda", "diana", "thaynara"]
        
        contexto = []
        
        tipos, saudacao, wordQuestion = vbd.verificaByDicio(prompt, tipos, saudacao) 
        
        #Tentando uma lógica nova para enteder contexto, mapeando tipos padrões de perguntas e compreendendo variáveis x, y, z dentro da frase, para compreensão de contexto
        
        
        
        #Tentando uma lógica nova para enteder contexto, mapeando tipos padrões de perguntas e compreendendo variáveis x, y, z dentro da frase, para compreensão de contexto
        
        
        #Verifica dia/tarde/noite

        if "bom dia" in prompt.lower(): #bom diaaa bom diaa bommm diaa
            tipos.append("dia")

        if "boa tarde" in prompt.lower():
            tipos.append("tarde")

        if "boa noite" in prompt.lower():
            tipos.append("noite")
        return contexto, tipos, saudacao
    else:
        print("Por favor reformule.")