package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)

	var n int
	fmt.Fscan(in, &n)

	for i := 0; i < n; i++ {
		var d, f, p float64
		fmt.Fscan(in, &d, &f, &p)

		amount := float64(d) * f * p
		rounded := math.Round(amount*100) / 100

		fmt.Fprintf(out, "$%.2f\n", rounded)
		out.Flush()
	}
}
