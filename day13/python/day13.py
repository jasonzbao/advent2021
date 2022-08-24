from python_utils.request import get_input

def print_coords(coords):
	coords_max_x = max(coords, key=lambda x: x[0])[0]
	coords_max_y = max(coords, key=lambda x: x[1])[1]

	coords = set([(coord[0], coord[1]) for coord in coords])

	for y in range(coords_max_y + 1):
		for x in range(coords_max_x + 1):
			if (x, y) in coords:
				print("#", end="")
			else:
				print(".", end="")
		print("")
	print("___________________________")

def part1(fn_in: str):
	coords, instructions = fn_in.split("\n\n")
	coords = [[int(x) for x in line.split(",")] for line in coords.split("\n")]

	# print_coords(coords)

	for instruction in instructions.split("\n")[:1]:
		instruction.strip("fold along")
		axis, value = instruction.split("=")
		value = int(value)

		if axis == "x":
			coord_index = 0
		else:
			coord_index = 1

		for coord in coords:
			if coord[coord_index] < value:
				continue
			else:
				coord[coord_index] = value - (coord[coord_index] - value)
		# print_coords(coords)

	return len(set([(coord[0], coord[1]) for coord in coords]))

def part2(fn_in: str):
	coords, instructions = fn_in.split("\n\n")
	coords = [[int(x) for x in line.split(",")] for line in coords.split("\n")]

	for instruction in instructions.split("\n"):
		instruction = instruction.strip("fold along")

		axis, value = instruction.split("=")
		value = int(value)

		if axis == "x":
			coord_index = 0
		else:
			coord_index = 1

		for coord in coords:
			if coord[coord_index] < value:
				continue
			else:
				coord[coord_index] = value - (coord[coord_index] - value)
	print_coords(coords)

if __name__ == "__main__":
	fn_input = get_input(13)
	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(fn_input))
