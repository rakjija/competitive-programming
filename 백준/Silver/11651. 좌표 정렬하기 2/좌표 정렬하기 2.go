package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type Coord struct {
	x int
	y int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)

	var n int
	fmt.Fscan(in, &n)

	coords := make([]Coord, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &coords[i].x, &coords[i].y)
	}

	sort.Slice(coords, func(i int, j int) bool {
		if coords[i].y == coords[j].y {
			return coords[i].x < coords[j].x
		}
		return coords[i].y < coords[j].y
	})

	for _, coord := range coords {
		fmt.Fprintln(out, coord.x, coord.y)
	}
	out.Flush()
}
