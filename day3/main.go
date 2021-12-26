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
	fmt.Printf("Part 1: %f \n", gamma*epsilon)
}

func filter(ss []string, bitVal string, index int) (ret []string) {
	if len(ss) == 1 {
		return ss
	}
	for _, s := range ss {
		if string(s[index]) == bitVal {
			ret = append(ret, s)
		}
	}
	return
}

func findGreatest(ss []string, index int) (ret int) {
	i := 0
	for _, val := range ss {
		innerVal, err := strconv.Atoi(string(val[index]))
		if err != nil {
			panic(err)
		}
		i += innerVal
	}
	if float64(len(ss))/2.0 <= float64(i) {
		return 1
	} else {
		return 0
	}

}

func part2(input []string) {
	oxygen, co2 := make([]string, len(input)), make([]string, len(input))
	copy(oxygen, input)
	copy(co2, input)
	for i := 0; i < len(input[0]); i++ {
		greatestOx, greatestCo2 := findGreatest(oxygen, i), findGreatest(co2, i)
		oxygen = filter(oxygen, strconv.Itoa(greatestOx), i)
		co2 = filter(co2, strconv.Itoa((greatestCo2+1)%2), i)
	}
	oxygenVal, err := strconv.ParseInt(oxygen[0], 2, 64)
	if err != nil {
		panic(err)
	}
	co2Val, err := strconv.ParseInt(co2[0], 2, 64)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Part 2: %v", co2Val*oxygenVal)
}

func main() {
	input := req.FormattedRequest(3)
	part1(input)
	part2(input)
}
