class questsAndAsks():
    def __init__(self):
        pass

    def testes(self, ask: str):
        import brain
        return brain.brain(ask, testing=True)


def autoTest(tests: list, expects: list):
    qa = questsAndAsks()
    results = []
    i = 0
    for test in tests:
        result = qa.testes(test)
        if result[0] == " ":
            result = result[1:]
        if expects[i] != result:
            return result, expects[i]
        i += 1

    return "Ok"
