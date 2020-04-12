#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(s):
	inValley = False
	depth = 0
	i = 0
	valleys = 0
	while (i < len(s)):
		if s[i] == 'D':
			depth -= 1
			if depth < 0:
				inValley = True
		else:
			depth += 1
			if depth == 0 and inValley:
				valleys += 1
				inValley = False
		i += 1
	return valleys




if __name__ == '__main__':
	s = 'UDDDUDUUUDDDUDUUUUDDDUDUUUDDDUDUUUUDDDUDUUUDDDUDUUUUDDDUDUUUDDDUDUUU'
	result = countingValleys(s)
	print(result)