import sys

def parseFile(file):
	lines = []
	for line in file:
		pieceList = []
		moves = line.split(',')
		for move in moves:
			pieceType = move[0]
			piecePos = move[1]
			if pieceType == 'Q':
				pieceList.append((pieces.Q, int(piecePos)))
			elif pieceType == 'Z':
				pieceList.append((pieces.Z, int(piecePos)))
			elif pieceType == 'S':
				pieceList.append((pieces.S, int(piecePos)))
			elif pieceType == 'T':
				pieceList.append((pieces.T, int(piecePos)))
			elif pieceType == 'I':
				pieceList.append((pieces.I, int(piecePos)))
			elif pieceType == 'L':
				pieceList.append((pieces.L, int(piecePos)))
			elif pieceType == 'J':
				pieceList.append((pieces.J, int(piecePos)))
			else:
				raise ValueError
		lines.append(pieceList)
	return lines

def placePiece(arena, piece):
	pieceSpots = piece[0]
	piecePos = piece[1]
	placementHeight = 0
	for i in range(piecePos, min(piecePos + 4, 10)):
		columnHeight = 0
		for j in range(len(arena[i])):
			if arena[i][j] and pieceSpots[i - piecePos][0]:
				columnHeight = j + 1
		if columnHeight > placementHeight:
			placementHeight = columnHeight
	for i in range(piecePos, min(piecePos + 4, 10)):
		for j in range(3):
			arena[i][j + placementHeight] = arena[i][j + placementHeight] or pieceSpots[i - piecePos][j]
	return (arena, placementHeight + 3)


def clearLines(arena, maxHeight):
	j = 0
	while j < maxHeight:
		if all(arena[i][j] for i in range(len(arena))):
			for x in range(len(arena)):
				arena[x].pop(j)
		else:
			j += 1
	return arena

def findMaxHeight(arena, maxHeight):
	j = 0
	height = 0
	while j < maxHeight:
		if any(arena[i][j] for i in range(len(arena))):
			height+=1
		j += 1
	return height


def evaluate(line):
	maxHeight = 0
	arena = []
	for i in range(10):
		column = []
		for j in range(100):
			column.append(False)
		arena.append(column)

	for piece in line:
		(arena, newHeight) = placePiece(arena, piece)
		clearLines(arena, newHeight + 1)
		maxHeight = findMaxHeight(arena, newHeight)
	return maxHeight

if __name__ == '__main__':
	import pieces
	fileName = sys.argv[1]
	file = open(fileName)
	lines = parseFile(file)

	for line in lines:
		print(evaluate(line))