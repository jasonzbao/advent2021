from collections import defaultdict
from python_utils.request import get_input

sample_input = "3,4,3,1,2"

def part1(input: str, number_of_days: int = 80) -> str:
	fishes = input.split(",")
	fishes = [int(fish) for fish in fishes]

	for _ in range(number_of_days):
		new_fish = []
		for (i, fish) in enumerate(fishes):
			if fish == 0:
				new_fish.append(8)
				fishes[i] = 6
			else:
				fishes[i] -= 1
		fishes += new_fish
	return len(fishes)

def part2(input: str) -> str:
	fishes = input.split(",")
	fishes = [int(fish) for fish in fishes]

	fish = {}

	# count number of fish at each day
	for i in range(7):
		fish[i] = fishes.count(i)

	new_fish = defaultdict(int)
	for i in range(256):
		# old fish make more new fish, new fish also make more new fish
		new_fish[(i - 1) % 9] = fish[i % 7] + new_fish[i % 9]

		# new fish become old fish
		fish[i % 7] += new_fish[i % 9]

	return sum(fish.values()) + sum(new_fish.values())

def part2_2(input: str) -> str:
	fishes = input.split(",")
	fishes = [int(fish) for fish in fishes]

	fish = {}

	# count number of fish at each day
	for i in range(9):
		fish[i] = fishes.count(i)

	for i in range(256):
		# when the graduated fish mate, they create new fish
		fish[(i + 7) % 9] += fish[i % 9]
	return sum(fish.values())

if __name__ == "__main__":
	fn_input = get_input(6)
	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(fn_input))
	print("Part 2 part 2 answer: ", part2_2(fn_input))

