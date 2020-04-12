def binarySearch(arr, start, end, query, side):
	if (start == end):
		if(arr[start] == query):
			return start
		return -1
	mid = int((start + end +1)/2)
	print(start, end, mid)
	if (query < arr[mid]):
		return binarySearch(arr, start, mid -1, query, side)
	elif(query > arr[mid]):
		return binarySearch(arr, mid +1, end, query, side)
	else:
		return binarySearch(arr, start, mid, query, side) if side else binarySearch(arr, mid, end, query, side)

if __name__ == '__main__':
	arr = [1,2,3,3,3,3,4,5,6,7]
	# print(binarySearchLeft(arr, 0, len(arr), 3, True))
	# print(binarySearchLeft(arr, 0, len(arr), 3, False))	
	#print(binarySearchRight(arr, 0, len(arr), 3))
	print(binarySearch(arr, 0, len(arr) -1, 3, True))
	print(binarySearch(arr, 0, len(arr) -1, 3, False))
