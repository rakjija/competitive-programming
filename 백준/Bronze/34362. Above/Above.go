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

	var n float64
	fmt.Fscan(in, &n)

	fmt.Fprintf(out, "%.4f", n-0.3)
}
