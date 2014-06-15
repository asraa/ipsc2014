infile = open('a1.in','r')
lines = infile.readlines()

num_test_cases = int(lines[0].strip())

enter = "*"
backspace = "<"

def solve(p, q):
	"" given p and q output string """