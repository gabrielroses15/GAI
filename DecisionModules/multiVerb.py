def multiVerb(infinitivos, verbs, i):
    try:
        if infinitivos.split()[i + 1] in verbs:
            return True
        if infinitivos.split()[i + 1] in ["a", "e", "o"]:
            if infinitivos.split()[i + 2] in verbs:
                return True
        if infinitivos.split()[i - 2] in ["a", "e", "o"] or infinitivos.split()[i - 2] in verbs and infinitivos.split()[
            i] in verbs:
            return True
        return False
    except:
        return False