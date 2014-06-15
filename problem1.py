import re

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


def detScore(s):
	words = re.compile('[\s,.:;\'\"!?-]').split(s)
	words = [word.strip() for word in words]
	n = len(words)
	in_asterick = [False]*len(words)
	typ = [None]*len(words)
	in_ast_space = False
	for i, word in enumerate(words):
		if word == '':
			continue
		begin = True if word[0] =='*' else False
		end = True if word[-1] == '*' else False
		if begin or word == '*':
			in_asterick = in_asterick[:i].append([not in_asterick[i]]*(n-i))
		if end:
			in_asterick = in_asterick[:i+1].append([not in_asterick[i]]*(n-i-1))

	score = 0
	for i, word in enumerate(words):
		if word == '' or word == '*':
			continue
		caps = isAllCaps(word)
		if caps and in_asterick[i]:
			score += 6
		elif in_asterick[i]:
			score += 3
		elif caps:
			score += 2
		else:
			score += 1
	return score
			
def isAllCaps(word):
	for c in word:
		if c.isupper()	
		
