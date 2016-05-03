def exertwo(word='lallalaa'):
	print('exercise 2: will remove adjacent+similar letters in a word')
	str_new = [l for ind, l in enumerate(word) if l != word[ind-1]]
	print str_new
	pass
	
exertwo('lallalaa')
