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
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	// P km까지는, 1km 당 A 엔
	// 이후부터는, 1km 당 B 엔
	// Q km 승차

	in.Scan()
	firstParts := strings.Fields(in.Text())
	p, _ := strconv.Atoi(firstParts[0])
	q, _ := strconv.Atoi(firstParts[1])

	in.Scan()
	secondParts := strings.Fields(in.Text())
	a, _ := strconv.Atoi(secondParts[0])
	b, _ := strconv.Atoi(secondParts[1])

	result := 0
	if q-p < 0 {
		result += q * a
	} else {
		result += p * a
		result += (q - p) * b
	}

	fmt.Fprintln(out, result)
}
