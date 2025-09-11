package main

import (
	"bufio"
	"fmt"
	"os"
)

func minSetNeeded(n, x int) int {
	return (n + x - 1) / x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, a, b, c, d int
	fmt.Fscan(in, &n, &a, &b, &c, &d)

	xCost := minSetNeeded(n, a) * b
	yCost := minSetNeeded(n, c) * d

	if xCost < yCost {
		fmt.Fprintln(out, xCost)
	} else {
		fmt.Fprintln(out, yCost)
	}
}
