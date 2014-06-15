infile = open('s1.in', 'r')
lines = infile.readlines()

num_test_cases = int(lines[0].strip())
index = 1

while index < len(lines):
	index += 1 #skip blank line
	num_sents = int(lines[index].strip())
	index += 1 #push reader index to next line
	
	for i in range(index, index+num_sents):
		sentence = lines[index].strip()
		score = detScore(sentence)
		words = lines.split()
		in_asterick = 
		tipe = [None]*len(words)
		for word in words:


def detScore(s):
		


print num_test_cases
