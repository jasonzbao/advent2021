from python_utils.request import get_input

points = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

points_2 = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}

symbols = {
	")": "(",
	"]": "[",
	"}": "{",
	">": "<"
}

symbols_f = {v: k for k, v in symbols.items()}

def part1(fn_in: str) -> str:
	lines = fn_in.split("\n")
	ret = 0
	for line in lines:
		stack = []
		for sym in line:
			if sym in symbols:
				if len(stack) == 0 or stack.pop() != symbols[sym]:
					ret += points[sym]
					break
			else:
				stack.append(sym)
	return ret

def part2(fn_in: str) -> str:
	lines = fn_in.split("\n")
	scores = []
	for line in lines:
		stack = []
		for sym in line:
			if sym in symbols:
				if len(stack) == 0 or stack.pop() != symbols[sym]:
					stack = []
					break
			else:
				stack.append(sym)
		score = 0
		for sym in stack[::-1]:
			score *= 5
			score += points_2[symbols_f[sym]]
		if score != 0:
			scores.append(score)
	return sorted(scores)[len(scores) // 2]

if __name__ == "__main__":
	fn_input = get_input(10)
	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(fn_input))
