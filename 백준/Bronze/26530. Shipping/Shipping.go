package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)

	var n int
	fmt.Fscan(in, &n)

	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(in, &x)

		var total float64
		for j := 0; j < x; j++ {
			var name string
			var count int
			var price float64
			fmt.Fscan(in, &name, &count, &price)
			total += float64(count) * price
		}
		fmt.Fprintf(out, "$%.2f\n", total)
		out.Flush()
	}
}
