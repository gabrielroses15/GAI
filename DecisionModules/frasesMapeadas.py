def dicio(complexity):
    if complexity < 1 :
       return "Erro na classificação de complexidade da frase."
    else:
        if complexity > 1 and complexity < 10:
            frases_mapeadas = {("quem foi", "quem era", "qm era", "qm foi"): "biografia de", ("história de", "história do", "historia da", "história di", "história du", "historia do", "história de", "historia da", "história di", "historia du", "hist da", "hist de", "hist di", "hist di", "hist do", "hist du"): "história"}
            return frases_mapeadas

def nomes():
    nomes = ["salomão", "miguel", "gabriel",
    "lucas", "joão", "davi", "pedro", "enzo",
    "gustavo", "eduardo", "nicolas", "yuri", "caio", "vitor",
    "antonio", "vinicius", "william", "paulo",
    "daniel", "marcos", "fernando", "rodrigo", "anderson",
    "andre", "julio", "renan", "valmir",
    "luis", "leonardo", "fabio", "arthur", "giovanna", "lais", "marina", "raissa", "thiago", "laura",
    "laisa", "sophia", "joao", "henrique", "samuel", "matheus", "luiza",
    "marcela", "leticia", "beatriz", "mirella", "clara", "isabella", "livia",
    "mateus", "guilherme", "marcelo", "jose", "gabriela", "rafaela", "raul",
    "gabrielle", "julia", "victor", "valentina", "viviane", "isabel", "isabelle", "thais",
    "nathalia", "nathalie", "diego", "bruno", "vivian", "marcio", "amanda", "carolina", "erica", "hugo", "joaquin",
    "karina", "lucia", "mario", "nadia", "patricia", "rafael", "sergio", "tomas",
    "ursula", "viviana", "yolanda", "sebastian", "valeria", "xavier",
    "martin", "pablo", "natalia", "manuel", "francisco",
    "ricardo", "veronica", "felipe", "alejandro", "carlos", "fernanda", "diana", "thaynara", "salomao"]
    return nomes

def pronomes():
    pron = ["eu", "tu", "ele", "nós", "vós", "eles", "nos", "vos", "nois", "você", "vc", "voce", "ela", "elx", "ela", "vocês", "vcs", "voces"]
    return pron