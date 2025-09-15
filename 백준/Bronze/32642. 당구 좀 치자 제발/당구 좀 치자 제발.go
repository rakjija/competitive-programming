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

	ws := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &ws[i])
	}

	total := 0
	anger := 0
	for _, w := range ws {
		if w == 0 {
			anger--
		} else {
			anger++
		}
		total += anger
	}

	fmt.Fprintln(out, total)
}
