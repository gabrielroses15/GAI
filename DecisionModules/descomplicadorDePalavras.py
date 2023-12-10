class FraseGramaticalmenteCorreta():
    def __init__(self, frase:string, pronomes:list, substantivos:list, memoryID:id, nomes:list):
        self.words = frase.split()
        self.pronomes = pronomes
        self.substantivos = substantivos
        self.memoryID = memoryID
        self.nomes = nomes
        self.construtor = memoryController(1)

def descomplicar(substantivos:list, pronomes:list, nomes:list, words:list, memoryID:int = 1):
    if memoryID == 1:
        for word in words:
            fraseParaBusca = ""


def memoryController(memoryID:int):
    if memoryID == 1:
        return ["ds", "v", "s", "n"] # ds -> double substantivo, v -> verbo, s -> substantivo, n -> nome