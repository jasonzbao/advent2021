from pprint import pprint

from python_utils.request import get_input

def format_input(fn_in: str):
	segments = fn_in.split("\n")
	segments = [[y.strip(" ").split(" ") for y in x.split("|")] for x in segments]
	return segments

def part1(fn_in: str) -> str:
	segments = format_input(fn_in)
	ret = 0
	for phrase in segments:
		for out in phrase[1]:
			if len(out) in [7, 4, 3, 2]:
				ret += 1
	return ret

def part2(fn_in: str) -> str:
	segments = format_input(fn_in)
	rets = []
	for phrase in segments:
		decoded = {}

		# numbers with 5 lines
		fives = []
		sixes = []
		for token in phrase[0]:
			if len(token) == 2:
				decoded[1] = set(token)
			elif len(token) == 3:
				decoded[7] = set(token)
			elif len(token) == 7:
				decoded[8] = set(token)
			elif len(token) == 4:
				decoded[4] = set(token)

			if len(token) == 5:
				fives.append(token)
			if len(token) == 6:
				sixes.append(token)

		if len(set(fives[0]) | set(fives[1])) == 7:
			decoded[3] = set(fives[2])
		elif len(set(fives[0]) | set(fives[2])) == 7:
			decoded[3] = set(fives[1])
		else:
			decoded[3] = set(fives[0])

		decoded[9] = decoded[3] | decoded[4]

		in_two = (decoded[8] - decoded[9]).pop()
		for token in fives:
			if set(token) != decoded[3]:
				if in_two in set(token):
					decoded[2] = set(token)
				else:
					decoded[5] = set(token)

		in_zero = (decoded[9] - decoded[5]).pop()
		for token in sixes:
			if set(token) != decoded[9]:
				if in_zero in set(token):
					decoded[0] = set(token)
				else:
					decoded[6] = set(token)		

		ret = ""
		for token in phrase[1]:
			for key, value in decoded.items():
				if value == set(token):
					ret += str(key)
		rets.append(int(ret))
	return sum(rets)


inp = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""



if __name__ == "__main__":
	fn_input = get_input(8)
	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(fn_input))

