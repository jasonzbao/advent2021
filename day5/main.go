package main

import (
	"fmt"
	"math"
	"req"
	"strconv"
	"strings"
)

type Board struct {
	values [][]int
}

type Line struct {
	startX int
	startY int
	endX   int
	endY   int
}

func (l *Line) xIncr() int {
	if l.startX == l.endX {
		return 0
	}
	return (l.endX - l.startX) / int(math.Abs(float64(l.startX-l.endX)))
}

func (l *Line) yIncr() int {
	if l.startY == l.endY {
		return 0
	}
	return (l.endY - l.startY) / int(math.Abs(float64(l.startY-l.endY)))
}

func NewBoard(maxX, maxY int) Board {
	values := make([][]int, maxX+1)
	for i := range values {
		values[i] = make([]int, maxY+1)
	}
	return Board{
		values: values,
	}
}

func (b *Board) AddLines(lines []Line, part2 bool) {
	for _, line := range lines {
		if part2 || line.startX == line.endX || line.startY == line.endY {
			for i := 0; i <= int(math.Max(math.Abs(float64(line.startY-line.endY)), math.Abs(float64(line.startX-line.endX)))); i++ {
				b.values[line.startX+(i*line.xIncr())][line.startY+(i*line.yIncr())] += 1
			}
		}
	}
}

func (b *Board) PointsWithTwoOverlaps() (total int) {
	for _, row := range b.values {
		for _, count := range row {
			if count >= 2 {
				total += 1
			}
		}
	}
	return
}

func convCoord(val string) int {
	ret, err := strconv.Atoi(val)
	if err != nil {
		panic(err)
	}
	return ret
}

func NewLine(coords []string) Line {
	start := strings.Split(coords[0], ",")
	end := strings.Split(coords[1], ",")

	return Line{
		startX: convCoord(start[0]),
		startY: convCoord(start[1]),
		endX:   convCoord(end[0]),
		endY:   convCoord(end[1]),
	}
}

func part1(lines []Line, maxX, maxY float64) {
	board := NewBoard(int(maxX), int(maxY))
	board.AddLines(lines, false)
	fmt.Printf("Part 1: %v", board.PointsWithTwoOverlaps())
}

func part2(lines []Line, maxX, maxY float64) {
	board := NewBoard(int(maxX), int(maxY))
	board.AddLines(lines, true)
	fmt.Printf("Part 2: %v", board.PointsWithTwoOverlaps())
}

func main() {
	input := req.FormattedRequest(5)

	var lines []Line
	maxX, maxY := 0.0, 0.0
	for _, val := range input {
		coords := strings.Split(val, " -> ")
		newLine := NewLine(coords)
		lines = append(lines, newLine)
		maxX = math.Max(maxX, math.Max(float64(newLine.startX), float64(newLine.endX)))
		maxY = math.Max(maxY, math.Max(float64(newLine.startY), float64(newLine.endY)))
	}
	part1(lines, maxX, maxY)
	part2(lines, maxX, maxY)
}
