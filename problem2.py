with open("t1.in", "r") as wordfile:
	#take in the number of test cases, l, n, & k
	num_testcases = wordfile.next()
	wordfile.next()
	lnk = wordfile.next()
	lnk_split = lnk.split(" ")
	l = lnk_split[0]
	n = lnk_split[1]
	k = lnk_split[2].strip()

	#make an array of pieces n
	pieces = []
	for line in wordfile:
		be = line.split(" ")
		b = be[0]
		e = be[1].strip()
		pieces.append((b,e))

	#make a list of not properly covered indices
	npc = [] #not properly covered
	for i in range(1,l):
		cond1 = False
		cond2 = False
		#check if there's a piece satisfying condition 1
		for (b,e) in pieces:
			if b<=i-k

		#check if there's a different piece satisfying condition 2

