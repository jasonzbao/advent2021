package main

import (
	"fmt"
	"req"
	"strconv"
)

func part1() {
	input := req.FormattedRequest(1)
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
	fmt.Println(increaseCount)
}

func main() {
	part1()
}
