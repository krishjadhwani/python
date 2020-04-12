def lengthOfLongestSubstring(s: str) -> int:
	i = 0
	longest_count = 0
	while i < len(s):
		letters_seen = dict()
		run = 0
		j = i
		while (j < len(s) and letters_seen.get(s[j]) == None):
			letters_seen[s[j]] = True
			run+=1
			j+=1
		print(run)
		if longest_count < run:
			longest_count = run
		i+=1
	return longest_count
if __name__ == '__main__':
	s = 'hello'
	print(s)
	print(lengthOfLongestSubstring(s))