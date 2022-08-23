from python_utils.request import get_input

def increment_adj(grid, i, j):
	opts = [-1, 0, 1]
	for i_opt in opts:
		for j_opt in opts:
			if i_opt == j_opt == 0:
				continue
			if 0 <= i_opt + i < len(grid):
				if 0 <= j_opt + j < len(grid):
					grid[i_opt + i][j_opt + j] += 1

def part1(fn_in: str) -> str:
	grid = [[int(x) for x in row] for row in fn_in.split("\n")]

	flash_count = 0
	for _ in range(100):
		flashed = set()
		for i in range(len(grid)):
			for j in range(len(grid)):
				grid[i][j] += 1
		had_flash = True
		while had_flash:
			had_flash = False
			for i in range(len(grid)):
				for j in range(len(grid)):
					if (i, j) not in flashed and grid[i][j] > 9:		
						flashed.add((i, j))
						increment_adj(grid, i, j)
						had_flash = True

		flash_count += len(flashed)
		for i, j in flashed:
			grid[i][j] = 0
	return flash_count

def part2(fn_in: str) -> str:
	grid = [[int(x) for x in row] for row in fn_in.split("\n")]

	step = 1
	while True:
		flashed = set()
		for i in range(len(grid)):
			for j in range(len(grid)):
				grid[i][j] += 1
		had_flash = True
		while had_flash:
			had_flash = False
			for i in range(len(grid)):
				for j in range(len(grid)):
					if (i, j) not in flashed and grid[i][j] > 9:		
						flashed.add((i, j))
						increment_adj(grid, i, j)
						had_flash = True
		for i, j in flashed:
			grid[i][j] = 0
		if len(flashed) == 100:
			return step
		step += 1
	return -1

inp ="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

if __name__ == "__main__":
	fn_input = get_input(11)
	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(inp))
