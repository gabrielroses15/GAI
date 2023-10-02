def comparaTamanhos(lista1:list, lista2:list, tipo:str = ""):
    if tipo == "Chaves e Nomes":
        if len(lista1) == len(lista2):
            return "Listas iguais"#Lógica q dá mais valor de importância a certos nomes baseado em regras como "?" caracteres especiais
        elif len(lista1) < len(lista2):
            return "Chaves maiores" #Desconsidera o nome após "meu nome é" e re-compara os tamanhos (possivelmente isso virará uma função ou um neurônio próprio, mas ai tem q ver se ele é ativado sempre, por complexidade ou mapa binário)
        else:
            return "Nomes maiores" #sla
    else:
        if len(lista1) == len(lista2):
            return "Listas iguais"
        elif len(lista1) < len(lista2):
            return "Lista 1 maior"
        else:
            return "Lista 2 maior"