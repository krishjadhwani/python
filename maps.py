def merch(arr):
	nums = {}
	pairs = 0
	for i in arr:
		if nums.get(i) is not None:
			print(i, ' paired')
			pairs += 1
		else:
			nums[i] = True

	return pairs


if __name__ == '__main__':
	arr = [10, 10, 20, 20]
	print(merch(arr))