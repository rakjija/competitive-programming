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

	var s, d, t float64
	fmt.Fscan(in, &s, &d, &t)

	if (s*5280/(60*60))*t >= d {
		fmt.Fprintln(out, "MADE IT")
	} else {
		fmt.Fprintln(out, "FAILED TEST")
	}
}
