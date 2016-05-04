def removeadjacent(word='lallalaa'):
    print('exercise 2: will remove adjacent+similar letters in a word')
    print word
    str_new = (l for ind, l in enumerate(word) if l != word[ind - 1])
    newword =''
    for l in str_new:
        newword+=l
    print newword


removeadjacent('lallalaa')
removeadjacent('Hello and Good Morning World')
