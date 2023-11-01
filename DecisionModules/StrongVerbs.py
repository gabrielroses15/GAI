def StrongVerbs(frase: str, actionVerbs: dict, dicio, words: list, nomes:list, infinitivos:str):
    contexto_count = {}
    verbosForces = [[], []]

    for valores, frases in dicio.items():
        for valor in valores:
            if frase.count(valor) == 1:
                contexto_count[valor] = contexto_count.get(valor, 0) + 1
            elif frase.count(valor) >= 1:
                contexto_count[valor] = contexto_count.get(valor, 0) + frase.count(valor)

    # for nome in nomes:
    #     #print(nome)
    #     #print(words[words.index(nome) - 3 : words.index(nome) + 3])
    #     #print(words[words.index(nome) + 3 : words.index(nome) - 3 : -1])
    #     #print(actionVerbs)
    #     if nome in words:
    #         if "quem foi ele" in " ".join(words[words.index(nome) - 3 : words.index(nome) + 4]):
    #             nomes_encontrados.append(nome)
    #             print("nomes_encontrados", nomes_encontrados)
    
    nomesEncontrados = []
    for forcas, raizes in actionVerbs.items():
        for word in infinitivos.split():
            if raizes == word:
                verbosForces[0].append(forcas)
                verbosForces[1].append(raizes)
            for nome in nomes:
                if word == nome and word not in nomesEncontrados:
                    nomesEncontrados.append(word)
                    break
            # for nome in nomes:
            #     if nome in words[words.index(word) - 3 : words.index(word) + 3]:
            #         print(nome)

#Adicionar mais codições como: em nomes, todos tem um "meu amigo" ou "Meus amigos" correspondente (meus amigos será mais complexo pois precisará de uma lógica para compreender a quantos nomes isto se refere)
#caso apenas alguns tenham meu amigo, e verbos fortes acompanhem "quem foi" ou qualquer str de dicio.items(), logo estes sãos os nomes importantes, caso contrário, os nomes com forças maiores são os importantes
#adicionar posterioremente variaveis para cada número utilizdao, como por exemplo: memórias temporárias, complexidades, valores de força para verbos (que deverão estar dentro de um limite), adicionar testes para
#garantir q os nmrs de dicionários sejam diferentes, pois um dicio n pode ter um valor igual.
#Adicionar a "escolha" da ia para cada "peso" detro dos códigos, tornando eles mais robustos e complexos, porém mais "inesperados", pois assim a I.A irá decidir cada peso, podendo levar em consideração a complexidade.
#A complexidade pode ser calculada por tamahos, verbos, nomes e outros valores que vou adicionar, como por exemplo, quem é o usuário, complexidades anteriores, frases e respostas anteriores, entre outros.
#Porém, se quiser algo colossal, os pesos da complexidade podem ser cotrolados também pela I.A ao invés de seguirem um estilo padronizado, assim, mesmo que minimamete, frases idênticas, podem ter complexidades diferentes
#Já que quem as considerará será a I.A, inicialmente, isto acarreterá em diversos erros, "burrices" e complicações quanto a inteligência da I.A, porém, após multiplos testes e muito treinamento, seu sistema de complexidade
#Pode evoluir exponencialmente, chegando a níveis que padrões e lógicas comuns nunca alcançariam, além de tudo, poderá ser considerado que de fato a I.A está entendendo o cotexto da frase, afinal, ela que vai decidir qual é
#A complexidade de uma frase baseada em algus poucos dados (comparado ao nível de dados que se podem ser retirados de uma frase), logo em algum momento a I.A pode entender sentidos diferetes de frases iguais, como por exemplo:
#"Qual a cor da manga?", a I.A pode considerar contextos anteriores, e entender se "manga" é referente a blusa ou a fruta, podendo entender inclusive se a fruta manga se refere ao geral (qualquer maga) ou se refere-se à uma
#Manga específica, como por exemplo uma manga que o usuário comentou anteriormente que comprou na feira e q a cor dela era rosa por exemplo. e o mais complexo de tudo é que, talvez o usuário tenha comentado de múltiplas mangas
#Tanto referente a frutas quanto referentes a blusa, fazendo a I.A gerar ao que se refere. Por fim, deixo aqui uma pergunta, MESMO SEM BANCO, E COM MENOS DE 30KB DE INFORMAÇÃO (LISTA DE NOMES, VERBOS ... SÃO APENAS FRASES), A IA
#CONSIDERANDO QUE A I.A COMPREENDA CONTEXTOS "COMPLEXOS" COMO O DA MANGA CITADO ANNTERIORMENTE, CONSIDERANDO Q A FRASE SEJA A MESMA E EM CASOS DIFERENTES ELA COMPREENDA QUE O SENTIDO É DIFERENTE (E ACERTE O SENTIDO CORRETO).
#PODERÍAMOS CONSIDERAR QUE A I.A ESTÁ "PENSANDO", PARA GERAR O CONTEXTO, ASSIM COMO NÓS FAZEMOS?
#---------------------------Obrigado por ler, by Dark <3------------------------------Obrigado por ler, by Dark <3-------------------------------Obrigado por ler, by Dark <3---------------------------------------------------

    namesForce = {}
    if len(verbosForces[1]) == len(nomesEncontrados):
        count = 0
        for nom in nomesEncontrados:
            namesForce[nom] = verbosForces[0][count]
            count += 1
        print(namesForce)

    print(infinitivos)
    print(verbosForces)
    print(nomesEncontrados)
    input("eae")
    

    if len(contexto_count) == 1 and sum(contexto_count.values()) == 1:
        from DecisionModules import lightSaber as lSaber
        if None in lSaber.teste(frase, dicio, nomes):
            print("We are in trouble here!")
            return None, None
        else:
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))
            return "resposta", resposta
        #contar as aparições de valor antes de passar action verbs, otimizando mais ainda!
    else:
        print("Mais de uma frase ou mais de um valor.")
        indexesMeu = []
        indexesAmigo = []
        indexesMeus = []
        indexesAmigos = []
        contador = 0
        for word in words:
            if word == "meu":
                indexesMeu.append(contador)
            if word == "amigo":
                indexesAmigo.append(contador)
            if word == "meus":
                indexesMeus.append(contador)
            if word == "amigos":
                indexesAmigos.append(contador)
            contador += 1
        if len(indexesMeu) == len(indexesAmigo):
            for index in indexesAmigo:
                for nome in nomes:
                    if nome == words[index+1]:
                        frase = frase.replace(nome, "").replace("  ", " ")
            print('f', frase)
        else:
            print("uma lista é melhor, me encontre no strongVerbs")
        
        if len(indexesMeus) == len(indexesAmigos):#CRIAR LÓGICA PARA CASO A FRASE CONTENHA MEU E MEUS
            print("b")
        else:
            print("uma lista é melhor, me encontre no strongVerbs")



#print(splitFriends("Meu amigo gregory me recomendou o livro de salmos, que também foi recomendado pelo meu amigo samuel, escrito pelo meu amigo salomão, quem foi ele?".lower()))