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

	var a, b, c int
	fmt.Fscan(in, &a, &b, &c)

	if a+b+c == 1 || a+b+c == 2 {
		if a == b {
			fmt.Fprintln(out, "C")
		} else if b == c {
			fmt.Fprintln(out, "A")
		} else if c == a {
			fmt.Fprintln(out, "B")
		}
	} else {
		fmt.Fprintln(out, "*")
	}
}
