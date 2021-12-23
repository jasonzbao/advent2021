package main

import (
	"fmt"
	"req"
	"strconv"
	"strings"
)

type direction string

const (
	Forward direction = "forward"
	Down    direction = "down"
	Up      direction = "up"
)

func part1(input []string) {
	horizontal, vertical := 0, 0
	for _, val := range input {
		row := strings.Split(val, " ")

		amount, err := strconv.Atoi(row[1])
		if err != nil {
			panic(err)
		}

		switch direction(row[0]) {
		case Forward:
			horizontal += amount
		case Down:
			vertical += amount
		case Up:
			vertical -= amount
		}
	}
	fmt.Println("Part 1: %v", vertical*horizontal)
}

func part2(input []string) {
	horizontal, vertical, aim := 0, 0, 0
	for _, val := range input {
		row := strings.Split(val, " ")

		amount, err := strconv.Atoi(row[1])
		if err != nil {
			panic(err)
		}

		switch direction(row[0]) {
		case Forward:
			horizontal += amount
			vertical += aim * amount
		case Down:
			aim += amount
		case Up:
			aim -= amount
		}
	}
	fmt.Println("Part 2: %v", vertical*horizontal)
}

func main() {
	input := req.FormattedRequest(2)
	part1(input)
	part2(input)
}
