package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var a, b, c, d int
	fmt.Fscan(in, &a, &b, &c, &d)

	m := a * b
	p := c * d

	switch {
	case m > p:
		fmt.Fprintln(out, "M")
	case m < p:
		fmt.Fprintln(out, "P")
	default:
		fmt.Fprintln(out, "E")
	}
}
