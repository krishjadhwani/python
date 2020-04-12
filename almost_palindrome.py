def palindrome(input):
	print(input)
	for i in range(int(len(input) /2)):
		if(input[i] != input[len(input) - 1- i]):
			return False
	return True

def almostPalindrome(input):
	for i in range(int(len(input)/2)):
		if(input[i] != input[len(input) -i -1]):
			return palindrome(input[i+1:len(input)- i]) or palindrome(input[i:len(input)-i-1])
	return True

if __name__ == '__main__':
	a = 'tacocat'
	b = 'tacocaat'
	c = 'tacocute'
	print(a, almostPalindrome(a))
	print(b, almostPalindrome(b))
	print(c, almostPalindrome(c))