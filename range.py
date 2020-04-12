from typing import Dict

if __name__ == '__main__':
	# p = [1,2,3,4,5,6,7]
	# a = range(1,0)
	# for x in a:
	# 	print(p[x])
	arr = [4,5, 1 , 3, 2]
	arrpos = [*enumerate(arr)]
	arrpos.sort(key = lambda b:b[1])
	letters_seen = dict()
	letters_seen['a'] = True
	print(letters_seen)
	print(arr)
	print(arrpos)
	print('hi')
	a = {}
	a.setdefault(1, 'a')
	a[4] = 'd'
	for x in a.keys():
		print(x)
	print(a)
	for i in range( 4, 7):
		print(i)

	a = [True, True, True, True, True, True]
	b = [True, True, True, False, True, True]
	print(all(elem for elem in a))
	print(all(elem for elem in b))	