def printArena(arena):
	for i in range(10, -1, -1):
		row = [] 
		for j in range(len(arena)):
			if arena[j][i]:
				row.append('X')
			else:
				row.append(' ')
		print(row)
