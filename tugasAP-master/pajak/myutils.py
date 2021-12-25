def countVocal(x):
    vowel = 'aiueo'
    cvocal = 0
    for i in x:
        if i in vowel:
            cvocal += 1
    return cvocal

def countConsonant(x):
    vowel = 'aiueo'
    cconsonant = 0
    for i in x:
        if i not in vowel:
            cconsonant += 1
    return cconsonant