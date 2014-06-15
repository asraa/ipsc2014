infile = open('u1.in','r')
lines = infile.readlines()

num_test_cases = int(lines[0].strip())

class Junction:
	def __init__(self, number, connections):
		self.number = number #Junction ID #
		self.connections = connections #list of Junction's it's connected to
	def number_connections(self):
		return len(self.connections)
	def add_connection(self, junction):
		self.connections.append(junction)
	def is_reachable(self, junction):
		return junction in self.connections #GOTTA CHANGE THIS

def assemble_network(n,network):
	#assemble network based on sum line
	assembled = n*[None]
	for i in network:
		s = sum(network[i].strip())
		assembled[s] = network[i]
	return assembled

#n is the number of junctions
#network is 
#function outputs m (num of roads) and a list of m items, length 2 (roads from junction a->b)
def junction_solve(n, network):
	junction_list = n*[Junction]
	ordered = assemble_network(n, network)
	#for each line in the path:
	for a in range(len(ordered)):
		for b in range(a,len(a)):
			if ordered[a][b] and not b == a:
				if not ordered[a].is_reachable(ordered[b]):
					ordered[a].add_connection(ordered[b])
	m = 0
	path_list = []
	for junction in junction_list:
		m+=junction.number_connections()
		for i in junction.connections:
			path_list.append(junction.number, junction.connections[i].number)
	return m, path_list

for i in range(num_test_cases):

