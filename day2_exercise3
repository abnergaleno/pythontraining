def exerthree(romaninput='XIV'):
	print('exercise 3 : roman numeral to string')
	romaninput = romaninput.upper()
	print 'romaninput = '+romaninput
	romans = 'MDCLXVI'
	decvals = [1000,500,100,50,10,5,1]
	dec = 0
	for l in romaninput:
		print 'l = ' + l
		print 'index = ' + str(romans.index(l))
		print ' index2 = ' + str(min(romans.index(l)+1,len(romans)-1))

		if decvals[romans.index(l)] < decvals[romans.index(romaninput[min(romaninput.index(l)+1,len(romaninput)-1)])]:
			dec += decvals[romans.index(l)].__neg__() 
			print '< ' + str(decvals[min(romans.index(l)+1,len(romans)-1)])
		else:
			dec += decvals[romans.index(l)]
			print 'not <'

	print 'dec = ' + str(dec)

exerthree('LXIV')
