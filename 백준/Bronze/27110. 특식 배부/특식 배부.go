package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func minInt(x int, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	reader := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	reader.Scan()
	n, _ := strconv.Atoi(reader.Text())

	reader.Scan()
	parts := strings.Split(reader.Text(), " ")
	a, _ := strconv.Atoi(parts[0])
	b, _ := strconv.Atoi(parts[1])
	c, _ := strconv.Atoi(parts[2])

	result := minInt(n, a) + minInt(n, b) + minInt(n, c)
	fmt.Fprintln(writer, result)
}
