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

	var d, e int
	fmt.Fscan(in, &d)

	fmt.Fscan(in, &e)
	for i := 0; i < e; i++ {
		var o string
		var q int
		fmt.Fscan(in, &o)
		fmt.Fscan(in, &q)

		switch o {
		case "+":
			d += q
		case "-":
			d -= q
		}
	}

	fmt.Fprintln(out, d)
}
