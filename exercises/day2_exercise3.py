def exerthree(romaninput='XIV'):
	print('exercise 3 : roman numeral to string')
	romaninput = romaninput.upper()
	print 'romaninput = '+romaninput
	romans = 'MDCLXVI'
	decvals = [1000,500,100,50,10,5,1]
	dec = 0
	for l in romaninput:
		if decvals[romans.index(l)] < decvals[romans.index(romaninput[min(romaninput.index(l)+1,len(romaninput)-1)])]:
			dec += decvals[romans.index(l)].__neg__() 
		else:
			dec += decvals[romans.index(l)]

	print 'dec = ' + str(dec)

exerthree('LXIV')
