infile = open('u1.in','r')
lines = infile.readlines()

num_test_cases = int(lines[0].strip())

class Junction:
	def __init__(self, number, connections):
		self.number = number #Junction ID #
		self.connections = connections #list of Junction's it's connected to
	def add_connection(Junction):
		#add a connection to Junction_number
		self.connections.append(Junction)
	
#n is the number of junctions
#network is a list (n items) of reachable connections
#function outputs m and a list of m items, length 2 (roads from junction a->b)
def junction_solve(n, network):


for i in range(num_test_cases):

