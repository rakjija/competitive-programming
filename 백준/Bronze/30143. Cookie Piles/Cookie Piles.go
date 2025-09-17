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

	var t int
	fmt.Fscan(in, &t)

	for i := 0; i < t; i++ {
		var n, a, d int
		fmt.Fscan(in, &n, &a, &d)

		total := 0
		for j := 0; j < n; j++ {
			total += a + (j * d)
		}

		fmt.Fprintln(out, total)
	}
}
