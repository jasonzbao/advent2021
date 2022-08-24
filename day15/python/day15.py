import sys
sys.setrecursionlimit(1500)

import time

from python_utils.request import get_input

class Solution:
	def __init__(self):
		self.memo = {}

	def lowest_risk(self, grid, i, j):
		if (i, j) in self.memo:
			return self.memo[(i, j)]

		if (i == len(grid) - 1) and (j == len(grid[0]) - 1):
			return grid[i][j]

		go_right, go_down = float('inf'), float('inf')
		if i < len(grid) - 1:
			go_right = self.lowest_risk(grid, i + 1, j) + grid[i][j]
		if j < len(grid) - 1:
			go_down = self.lowest_risk(grid, i, j + 1) + grid[i][j]

		self.memo[(i, j)] = min(go_right, go_down)
		return self.memo[(i, j)]

	def lowest_risk2(self, grid, i, j):
		if (i, j) in self.memo:
			return self.memo[(i, j)]

		ix5 = (len(grid) * 5) - 1
		jx5 = (len(grid[0]) * 5) - 1

		imod = i % len(grid)
		jmod = j % len(grid[0])

		risk = (((grid[imod][jmod] + (i // len(grid)) + (j // len(grid)) - 1)) % 9) + 1

		if (i == ix5) and (j == jx5):
			return risk

		go_right, go_down = float('inf'), float('inf')
		if i < ix5:
			go_right = self.lowest_risk2(grid, i + 1, j) + risk
		if j < jx5:
			go_down = self.lowest_risk2(grid, i, j + 1) + risk			

		self.memo[(i, j)] = min(go_right, go_down)
		return self.memo[(i, j)]

def part1(fn_in: str):
	sol = Solution()
	grid = [[int(x) for x in y] for y in fn_in.split("\n")]
	return sol.lowest_risk(grid, 0, 0) - grid[0][0]

def part2(fn_in: str):
	sol = Solution()
	grid = [[int(x) for x in y] for y in fn_in.split("\n")]
	return sol.lowest_risk2(grid, 0, 0) - grid[0][0]

inp = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

if __name__ == "__main__":
	fn_input = get_input(15)

	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(inp))
