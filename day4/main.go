package main

import (
	"fmt"
	"req"
	"strconv"
	"strings"
)

type Board struct {
	values [][]string
	marked [][]int
}

func NewBoard() Board {
	marked := make([][]int, 5)
	for i := range marked {
		marked[i] = make([]int, 5)
	}
	values := make([][]string, 5)
	for i := range values {
		values[i] = make([]string, 5)
	}

	return Board{
		values: values,
		marked: marked,
	}
}

func (b *Board) isComplete() bool {
	for i := 0; i < 5; i++ {
		complete1, complete2 := 1, 1
		for j := 0; j < 5; j++ {
			complete1 *= b.marked[i][j]
			complete2 *= b.marked[j][i]
		}
		if complete1 == 1 || complete2 == 1 {
			return true
		}
	}
	return false
}

func (b *Board) mark(number string) {
	for i, row := range b.values {
		for j, num := range row {
			if num == number {
				b.marked[i][j] = 1
			}
		}
	}
}

func (b *Board) sum() (sum int) {
	for i, row := range b.marked {
		for j, num := range row {
			if num == 0 {
				numInt, err := strconv.Atoi(b.values[i][j])
				if err != nil {
					panic(err)
				}
				sum += numInt
			}
		}
	}
	return
}

func part1(input []string) {
	commands := strings.Split(input[0], ",")
	boards := []Board{}
	for i, val := range input {
		// first 2 lines are for commands
		if i == 0 || i == 1 {
			continue
		}

		shiftI := i - 2 // shift for commands
		if shiftI%6 == 0 {
			boards = append(boards, NewBoard())
		}
		if shiftI%6 != 5 {
			splitI := 0
			for _, val := range strings.Split(val, " ") {
				if val == "" {
					continue
				}
				boards[len(boards)-1].values[shiftI%6][splitI] = val
				splitI += 1
			}
		}
	}

	for _, command := range commands {
		for _, board := range boards {
			board.mark(command)
		}
		for _, board := range boards {
			if board.isComplete() {
				lastNum, err := strconv.Atoi(command)
				if err != nil {
					panic(err)
				}
				fmt.Printf("Part 1: %v", board.sum()*lastNum)
				return
			}
		}
	}

}

func main() {
	input := req.FormattedRequest(4)
	part1(input)
	// part2(input)
}
