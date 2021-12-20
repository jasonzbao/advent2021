package main

import (
	"fmt"
	"req"
	"strconv"
)

func part1(input []string) {
	lastVal, increaseCount := -1, -1
	for _, val := range input {
		valInt, err := strconv.Atoi(val)
		if err != nil {
			panic(err)
		}
		if valInt > lastVal {
			increaseCount += 1
		}
		lastVal = valInt
	}
	fmt.Println("Part 1: %v", increaseCount)
}

func part2(input []string) {
	lastVal, increaseCount := -1, -1
	for i, _ := range input {
		if i > len(input)-3 {
			break
		}
		sum := 0
		for j := 0; j < 3; j++ {
			valInt, err := strconv.Atoi(input[i+j])
			if err != nil {
				panic(err)
			}
			sum += valInt
		}
		if sum > lastVal {
			increaseCount += 1
		}
		lastVal = sum
	}
	fmt.Println("Part 2: %v", increaseCount)
}

func main() {
	input := req.FormattedRequest(1)
	part1(input)
	part2(input)
}
