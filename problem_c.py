infile = open('c1.in','r')
lines = infile.readlines()
index = 0
num_test_cases = int(lines[index].strip())
index += 1 #blank line

def solve(n, SS):
	'''return original permutation given 
	n = integer length of final sequence
	S = the final sequence as a string of space separated integers'''
	A = SS.strip().split()
	S = [int(i) for i in A]
	l = int(max(S))
	sequence_length = n - l #length of repeated sequence
	for block_index in range(l):
		block = S[block_index:(block_index+sequence_length)]
		next_block = S[block_index+sequence_length:(block_index+2*sequence_length)]
		if block == next_block:
			s = S[:block_index]+S[block_index+sequence_length:]
			a = ""
			for i in s:
				a += str(i)
				a += " "
			return a
		
index+=1 #starting line
f = open('answer_c1.txt','r+')
while index < len(lines):
	seq = str(solve(int(lines[index]),lines[index+1]))
	index += 3
	f.write(seq + "\n")
f.close()