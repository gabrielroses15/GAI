def dicio(complexity):
    if complexity < 1 :
       return "Erro na classificação de complexidade da frase."
    else:
        if complexity > 1 and complexity < 10:
            frases_mapeadas = {("quem foi", "quem era", "qm era", "qm foi", "qm foram", "quem foram"): "biografia de", ("história de", "história do", "historia da", "história di", "história du", "historia do", "história de", "historia da", "história di", "historia du", "hist da", "hist de", "hist di", "hist di", "hist do", "hist du"): "história"}
            return frases_mapeadas#qm foram? plural?

def verbosList():
    verbosList = {
    "fazer": ["faço", "fazia", "fazeis", "feito"],
    "ir": ["vou", "ia", "ides"],
    "ter": ["tenho", "tinha", "tendes"],
    "ser": ["sou", "era", "sereis"],
    "estar": ["estou", "estava", "esteis"],
    "poder": ["posso", "podia", "podeis"],
    "dizer": ["digo", "dizia", "dizeis"],
    "ver": ["vejo", "via", "veis"],
    "dar": ["dou", "dava", "dais"],
    "saber": ["sei", "sabia", "sabeis"],
    "coseguir": ["cosegue", "conseguia", "consegues"],
    "escrever": ["escreveu", "escrito", "escrevido"],
    "produzir": ["produzido"],
    "recomendar": ["recomendou", "recomendaste", "recomendado"],
    "falar": ["falou", "fala", "falaste"]
    }
    return verbosList

def nomes():
    nomes = ["salomão", "miguel", "gabriel", "josé", "jose",
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
    "ricardo", "veronica", "felipe", "alejandro", "carlos", "fernanda", "diana", "thaynara", 
    "salomao", "elizeu", "eliza", "elizabeth", "beth", "gregory", "greg", "maria", "charles", "darwin",
    "saulo", "cleber", "ester", "napoleão"]
    return nomes

def pronomes():
    pron = ["eu", "tu", "ele", "nós", "vós", "eles", "nos", "vos", "nois", "você", "vc", "voce", "ela", "elx", "ela", "vocês", "vcs", "voces"]
    return pron