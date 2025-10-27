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

	var n int
	fmt.Fscan(in, &n)

	for i := 0; i < n; i++ {
		var a, b float64
		fmt.Fscan(in, &a, &b)

		h := (2 * a) / b
		fmt.Fprintf(out, "The height of the triangle is %.2f units\n", h)
	}
}
