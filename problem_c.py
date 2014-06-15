infile = open('c2.in','r')
lines = infile.readlines()
index = 0
num_test_cases = int(lines[index].strip())
index += 1 #blank line

def solve(n, SS):
	'''return original permutation given 
	n = integer length of final sequence
	S = the final sequence as a string of space separated integers'''
	A = SS.strip().split()
	seq = []
	for i in A:
		if i not in seq:
			seq.append(i)

	perm = ""
	for i in seq:
		perm+=i
		perm +=" "
	return perm[:-1]
print solve(11, "4 3 1 2 3 1 4 3 3 1 4")
		
index+=1 #starting line
f = open('answer_c2.txt','r+')
while index < len(lines):
	seq = str(solve(int(lines[index]),lines[index+1]))
	index += 3
	f.write(seq + "\n")
f.close()