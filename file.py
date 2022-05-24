# hello this is a title text

import sys

def title(n):
	return n**2

n = int(sys.argv[1])

print '{0}^2 = {1}'.format(n, title(n))
