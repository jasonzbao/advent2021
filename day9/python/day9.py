from functools import reduce

from python_utils.request import get_input

def shared(fn_in: str) -> str:
	data = fn_in.split("\n")
	data = [[int(i) for i in row] for row in data]

	low_points = []
	for i in range(len(data)):
		for j in range(len(data[i])):
			adj = []
			if i != 0:
				adj.append(data[i-1][j])
			if j != 0:
				adj.append(data[i][j-1])
			if i < len(data) - 1:
				adj.append(data[i+1][j])
			if j < len(data) - 1:
				adj.append(data[i][j+1])
			if data[i][j] < min(adj):
				low_points.append((i, j))
	return low_points, data

def part1(fn_in: str) -> str:
	low_points, data = shared(fn_in)

	return sum([data[i][j] for i, j in low_points]) + len(low_points)

def part2(fn_in: str) -> str:
	low_points, data = shared(fn_in)

	sizes = []
	for point in low_points:
		basin_size = 0
		stack = [point]
		seen = set()
		while len(stack) > 0:
			i, j = stack.pop()
			if data[i][j] == 9 or (i, j) in seen:
				continue
			seen.add((i, j))

			basin_size += 1
			if i != 0:
				stack.append((i - 1, j))
			if j != 0:
				stack.append((i, j - 1))
			if i < len(data) - 1:
				stack.append((i + 1, j))
			if j < len(data) - 1:
				stack.append((i, j + 1))

		sizes.append(basin_size)
	return reduce(lambda x, y: x * y, sorted(sizes)[-3:])

if __name__ == "__main__":
	fn_input = get_input(9)
	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(fn_input))
