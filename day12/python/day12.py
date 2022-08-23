from python_utils.request import get_input

class Node:
	def __init__(self, key):
		self.key = key
		self.adj = []
		if key != "end" and key != "start":
			if key.lower() == key:
				self._is_small = True
			else:
				self._is_small = False
		else:
			# end and start should only be visited once
			self._is_small = True

	def add_adj(self, node: 'Node'):
		""" Adds node to self """
		self.adj.append(node)

	def is_end(self):
		return self.key == "end"

	def is_start(self):
		return self.key == "start"

	@property
	def is_small(self):
		return self._is_small

def unique_paths(current: Node, seen):
	if current.is_end():
		return 1

	if current.is_small and current.key in seen:
		return 0

	seen.add(current.key)
	return sum([unique_paths(n, seen.copy()) for n in current.adj])

def unique_paths2(current: Node, use_twice, seen):
	if current.is_end():
		return 1

	if current.is_small and current.key in seen:
		if use_twice or current.is_start():
			return 0
		else:
			use_twice = True
	seen.add(current.key)
	return sum([unique_paths2(n, use_twice, seen.copy()) for n in current.adj])



def create_graph(fn_in: str):
	fn_in = fn_in.split("\n")
	nodes = {} # key = node key
	for token in fn_in:
		vertices = token.split("-")
		for vertex in vertices:
			if vertex not in nodes:
				nodes[vertex] = Node(vertex)
		nodes[vertices[0]].add_adj(nodes[vertices[1]])
		nodes[vertices[1]].add_adj(nodes[vertices[0]])
	return nodes

def part1(nodes) -> str:
	return unique_paths(nodes["start"], set())

def part2(nodes) -> str:
	return unique_paths2(nodes["start"], False, set())

if __name__ == "__main__":
	fn_input = get_input(12)
	nodes = create_graph(fn_input)
	print("Part 1 answer: ", part1(nodes))
	print("Part 2 answer: ", part2(nodes))
