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



	for move in moves:
		if move = 'l'
			new_nums = move_left(nums)
		else:
			new_nums = move_right(nums)

		#get new random val
		num_empty = sum([1 for x in frequencies if x == 0])
		if new_nums == nums:
			pos = random() % num_empty
			if (random() % 10) == 0:
				new_value = 4
			else:
				new_value = 2

		#insert it
			empty_counter = 0
			for i,num in enumerate(new_num):
				if new_nums[i] != 0:
					continue
				if new_nums[i] == 0 and empty_counter == pos:
					new_nums[i] = new_value
				else:
					empty_counter += 1

		nums = new_nums

	
def move_left(nums):
	new_nums = [0]*len(size_strip)
	inPair = False
	pastNum = 0
	index = 0
	for i, num in enumerate(nums):
		if num == 0:
			continue
		else:
			if inPair and pastNum == num:
				new_nums[index] = pastNum*2
				index += 1
			elif inPair and pastNum != num:
				new_nums[index] = pastNum
				new_nums[index+1] = num
				inPair = False
				index += 2
			elif not inPair:
				pastNum = num
				inPair = True
	return new_nums
	
def move_right(nums):
	new_nums = [0]*len(size_strip)
	inPair = False
	pastNum = 0
	index = 0
	pairs = enumerate(nums)
	pairs.reverse()
	for i, num in pairs:
		if num == 0:
			continue
		else:
			if inPair and pastNum == num:
				new_nums[index] = pastNum*2
				index += 1
			elif inPair and pastNum != num:
				new_nums[index] = pastNum
				new_nums[index+1] = num
				inPair = False
				index += 2
			elif not inPair:
				pastNum = num
				inPair = True


