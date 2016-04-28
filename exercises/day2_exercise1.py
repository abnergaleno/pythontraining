def exerone(lwh=3):
	print('exercise 1 : will create 3d array with value made up of 3d indices')

	threedimarr=[]
	threedimarr = [[[str(x)+'-'+str(y)+'-'+str(z)  for z in range(3)] for y in range(3)] for x in range(3)]
	print threedimarr

exerone(3)
