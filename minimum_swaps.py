#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	arrPos = [*enumerate(arr)]
	arrPos.sort(key = lambda number:number[1])
	visited = {v:False for v in range(len(arr))}
	swaps = 0
	for i in range(len(arr)):
		if visited[i] or arrPos[i][0] == i:
			continue
		localSwaps = 0
		j = i
		while not visited[j]:
			visited[j] = True
			j = arrPos[j][0]
			localSwaps += 1
		swaps+=localSwaps -1
	return swaps

def mergeSort(arr):
	if(len(arr) >1):
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		mergeSort(left)
		mergeSort(right)

		i = 0
		j = 0
		k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
		while i < len(left):
			arr[k] = left[i]
			i+=1
			k+=1
		while j < len(right):
			arr[k] = right[j]
			j+=1
			k+=1



if __name__ == '__main__':
	arr = [1, 5, 4, 3, 2] 
	print(minimumSwaps(arr))
	mergeSort(arr)
	print(arr)

	arr = [1, 5, 4, 3, 2] 
	print(minimumSwaps(arr)) 
	mergeSort(arr)
	print(arr)
