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

	var a float64
	fmt.Fscan(in, &a)

	fmt.Fprintln(out, math.Sqrt(a)*4)
}
