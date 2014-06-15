f = open('b1.in', 'r')
lines = f.readlines()
index = 0
num_tests = int(lines[index].strip())
index += 1 #move to blank line

while index < len(lines):
	index += 1 #move past blank line
	size_strip = float(lines[index].strip())
	index += 1 #move past size strip line
	nums = lines[index].strip().split()
	nums = [int(num) for num in nums]
	index += 1 #move past strip nums
	ms = lines[index].strip().split()	
	ms = [int(m} for m in ms]
	index += 1
	num_moves = int(lines[index])
	index += 1
	moves = lines[index]


	new_array = [0]*len(size_strip)

	for move in moves:
		if move = 'l'
			new_nums = move_left(nums)
			num_empty = sum([1 for x in frequencies if x == 0])
			if new_nums == nums:
				pos = random() % num_empty
				if (random() % 10) == 0:
					new_value = 4
				else:
					new_value = 2
		else:
			new_nums = move_right(nums)

	

