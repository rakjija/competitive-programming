package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewScanner(os.Stdin)

	in.Scan()
	parts := strings.Fields(in.Text())

	var counts [3]int
	var max int
	for i := 0; i < 3; i++ {
		counts[i], _ = strconv.Atoi(parts[i])
		if max < counts[i] {
			max = counts[i]
		}
	}

	var needs int
	for i := 0; i < 3; i++ {
		needs += max - counts[i]
	}

	fmt.Println(needs)
}
