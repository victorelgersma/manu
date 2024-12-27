
def wordInCharacterList(liste, word):
     """
     >>> wordInCharacterList(['a', 'b', 'c', 'd'], "bcd")
     True
     """
     string = ''.join(liste)
     return word in string


def wordIsPresentHorizonally(grille, mot):
    """
    >>> wordIsPresentHorizonally([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], "abc")
    True
    >>> wordIsPresentHorizonally([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], "zyx")
    False
    >>> wordIsPresentHorizonally([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], "cfi")
    False
    """
    for i in grille:
        if wordInCharacterList(i, mot):
            return True
    return False

def wordIsPresentVertically(grille, mot):
    """
    >>> wordIsPresentVertically([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], "cfi")
    True
    """
    characterArray = []
    for i in range(len(grille[0])):
        characterArray.append(grille[0][i])
        characterArray.append(grille[1][i])
        characterArray.append(grille[2][i])
    return wordInCharacterList(characterArray, mot)

    

def motCache(grille, mot):
    """
    >>> motCache([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], "abc")
    True
    >>> motCache([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], "zyx")
    False
    >>> motCache([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], "cfi")
    True
    """
    return wordIsPresentHorizonally(grille, mot) or wordIsPresentVertically(grille, mot)
    

        
    









