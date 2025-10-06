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
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)

	count := 0
	for i := 1; i <= n; i++ {
		count += int(math.Pow(float64(i), 3))
	}

	fmt.Fprintln(out, count)
}
