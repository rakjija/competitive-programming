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

	var w, h float64
	fmt.Fscan(in, &w, &h)

	d := math.Sqrt(math.Pow(w, 2) + math.Pow(h, 2))
	s := w + h

	fmt.Fprintln(out, s-d)
}
