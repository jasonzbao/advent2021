from collections import Counter, defaultdict

from python_utils.request import get_input

def part1(fn_in: str):
	start, pairs = fn_in.split("\n\n")

	pairs = [[p.strip(" ") for p in line.split("->")] for line in pairs.split("\n")]
	kv = {}
	for pair in pairs:
		kv[pair[0]] = pair[1]
	
	start = list(start)
	for _ in range(10):
		pairs = zip(start[:-1], start[1:])
		additions = []
		for pair in pairs:
			p = ''.join(pair)
			if p in kv:
				additions.append(kv[p])
			else:
				additions.append("")
		new_start = ""
		for (i, addition) in enumerate(additions):
			new_start += start[i] + addition
		new_start += start[-1]
		start = new_start

	counts = Counter(start)
	print(counts)
	values = sorted(counts.values())
	return values[-1] - values[0]

def part2(fn_in: str):
	start, pairs = fn_in.split("\n\n")

	pairs = [[p.strip(" ") for p in line.split("->")] for line in pairs.split("\n")]
	kv = {}
	for pair in pairs:
		kv[pair[0]] = pair[1]

	counts = defaultdict(int)

	start = list(start)
	pairs = zip(start[:-1], start[1:])
	for pair in pairs:
		p = ''.join(pair)
		counts[p] += 1

	for _ in range(40):
		count_copy = dict(counts)
		for key, value in count_copy.items():
			a, b = list(key)
			counts[a + kv[key]] += value
			counts[kv[key] + b] += value
			counts[key] -= value

	poly_counts = defaultdict(int)
	for key, value in counts.items():
		a, b = list(key)
		poly_counts[a] += value

	# we will miss one value this way which will be the value at the very end
	poly_counts[start[-1]] += 1

	values = sorted(poly_counts.values())
	return values[-1] - values[0]

inp = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

if __name__ == "__main__":
	fn_input = get_input(14)
	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(fn_input))
