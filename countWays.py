from typing import Dict


def countWaysBruteForce(n: int) -> int:
	if (n < 0):
		return 0
	elif n == 0:
		return 1
	else:
		return countWaysBruteForce(n - 1) + countWaysBruteForce(n - 2) + countWaysBruteForce(n - 3)

def countWaysMemo(n: int) -> int:
	memo = {}
	for i in range(n + 1):
		memo[i] = -1
	return countWaysMemoHelper(n, memo)

def countWaysMemoHelper(n: int, memo: Dict[int, int]):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif memo[n] != -1:
		return memo[n]
	else:
		memo[n] = countWaysMemoHelper(n - 1, memo) + countWaysMemoHelper(n - 2, memo)+ countWaysMemoHelper(n - 3, memo)
		return memo[n]



if __name__ == '__main__':
	print(countWaysBruteForce(4))
	print()
	print(countWaysMemo(4))
	print(countWaysMemo(10))
	print(countWaysMemo(25))
	print(countWaysMemo(33))