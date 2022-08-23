import math

from python_utils.request import get_input

def part1(input: str) -> int:
	nums = input.split(",")
	nums = [int(num) for num in nums]

	nums = sorted(nums)
	position = 0
	# if its odd the median is the middle, if it's not you can take the value on either side
	# since it will cause the same number of elements to need to shift.
	position = nums[int(len(nums) // 2)]
	return sum([abs(x - position) for x in nums])

def part2(input: str) -> int:
	nums = input.split(",")
	nums = [int(num) for num in nums]

	position_1 = math.floor(sum(nums) / len(nums))
	position_2 = position_1 + 1
	return min([sum([(abs(x - y) * (abs(x - y) + 1)) / 2 for x in nums]) for y in [position_1, position_2]])

if __name__ == "__main__":
	fn_input = get_input(7)
	print("Part 1 answer: ", part1(fn_input))
	print("Part 2 answer: ", part2(fn_input))

