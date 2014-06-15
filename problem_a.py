infile = open('a1.in','r')
outfile = open('a1.out','w')
lines = infile.readlines()

num_test_cases = int(lines[0].strip())

enter = "*"
backspace = "<"

# given p & q, output a string of the keystrokes we want to press to get from 
# q -> p with as few moves as possible
def solve(p, q):

	#find the first mistake
	first_mistake = -1
	for i in range(0,min(len(p),len(q))):
		if p[i] != q[i]:
			first_mistake = i
			break

	if first_mistake >= 0:

		#compare two options: 
		#1) deleting up until you've gotten rid of the first mistake and retyping the rest of p
		#2) starting all over and typing p
		num_deletes = len(q) - first_mistake
		num_additions_after_delete = len(p) - first_mistake
		option_1_cost = num_deletes + num_additions_after_delete
		option_2_cost = 1 + len(p) # p additions + 1 for pressing enter

		output_string = "" #the string showing the key sequence we want
		if option_1_cost <= option_2_cost:
			output_string = backspace*num_deletes + p[first_mistake:] + enter
		else:
			output_string = enter + p + enter

		outfile.write(output_string)

	#if there was no mistake
	else:
		diff = len(p) - len(q)
		if diff > 0:
			outfile.write(p[(len(p) - diff):] + enter)
		else:
			outfile.write(enter)


solve('superfastawesome', 'superfastaxesome')



	