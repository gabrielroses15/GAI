from DecisionModules import verificaByDicio as vbd

#Montar níveis de extração de contexto

#Função pra retirar o contexto da frase
def extrair_contexto(prompt: str, tipos, complexidade:int, resposta):
    if complexidade == 2:
        return "responder", "nada"
        saudacao = "Olá, " #Início padrão, começará a retornar a saudação, q é um parâmetro opcional de devolução, mas tlvz seja necessário pedir no início
        tipos, saudacao, palavraQuestão = vbd.verificaByDicio(prompt, tipos, saudacao) #palavraQuestão provavelmente é inútil
        
    
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
    
    frases_mapeadas = {"biografia de ": "quem foi"}
    frase = "quem foi joao"
    if frase in frases_mapeadas:
        print(frases_mapeadas[frase])
    
    #Tentando uma lógica nova para enteder contexto, mapeando tipos padrões de perguntas e compreendendo variáveis x, y, z dentro da frase, para compreensão de contexto

    #return contexto, tipos, saudacao