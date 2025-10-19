package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)

	for i := 0; i < t; i++ {
		var x, y int
		fmt.Fscan(in, &x, &y)

		for j := 0; j < y; j++ {
			fmt.Fprint(out, strings.Repeat("X", x))
			fmt.Fprint(out, "\n")
		}
		fmt.Fprint(out, "\n")
	}
}
