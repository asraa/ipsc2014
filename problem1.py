infile = open('s1.in', 'r')
lines = infile.readlines()

num_test_cases = int(lines[0].strip())
index = 1

max_score = -1
max_sentence = ''
outfile = open('s1_ans.out', 'w')

while index < len(lines):
	index += 1 #skip blank line
	num_sents = int(lines[index].strip())
	index += 1 #push reader index to next line

	for i in range(index, index+num_sents):
		sentence = lines[index].strip()
		score = detScore(sentence)
		if score > max_score:
			max_sentence = sentence
			max_score = score
		
	outfile.write(str(max_score) + '\n')

import re

def detScore(s):
	words = lines.split()
	n = len(words)
	in_asterick = [False]*len(words)
	typ = [None]*len(words)
	in_ast_space = False
	for i, word in enumerate(words):
		begin = True if word[0] =='*' else False
		end = True if word[-1] == '*' else False
		if begin:
			in_asterick = in_asterick[:i].append([not in_asterick[i]]*(n-i))
		if end:
			in_asterick = in_asterick[:i+1].append([not in_asterick[i]]*(n-i-1))

	for word in enumerate(words):
		if
			
		
		


print num_test_cases
