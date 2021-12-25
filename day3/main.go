package main

import (
	"fmt"
	"math"
	"req"
	"strconv"
)

func part1(input []string) {
	vals := make([]int, len(input[0]))
	for _, val := range input {
		for i, innerVal := range val {
			innerVal, err := strconv.Atoi(string(innerVal))
			if err != nil {
				panic(err)
			}
			vals[i] += innerVal
		}
	}

	gamma, epsilon := 0.0, 0.0
	for i := 0; i < len(vals); i++ {
		if len(input)/2 < vals[len(vals)-i-1] {
			gamma += math.Pow(2, float64(i))
		} else {
			epsilon += math.Pow(2, float64(i))
		}
	}
	fmt.Printf("Part 1: %f", gamma*epsilon)
}

func main() {
	input := req.FormattedRequest(3)
	part1(input)
}
