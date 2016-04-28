def exerone(lwh=3):
	print('exercise 1 : will create 3d array with value made up of 3d indices')

	threedimarr=[]
	threedimarr = [[[str(x)+'-'+str(y)+'-'+str(z)  for z in range(3)] for y in range(3)] for x in range(3)]
	print threedimarr
	
	for a_idx, a in enumerate(threedimarr):
	for b_idx, b in enumerate(a):
		for c_idx, c in enumerate(b):
			# line += str(c)
			print threedimarr[a_idx][b_idx][c_idx],
	print '\n'	

exerone(3)
