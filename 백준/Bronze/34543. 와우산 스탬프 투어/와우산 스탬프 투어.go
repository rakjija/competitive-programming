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

	var n, w int
	fmt.Fscan(in, &n, &w)

	score := n * 10
	if n >= 3 {
		score += 20
	}
	if n == 5 {
		score += 50
	}
	if w > 1000 {
		score -= 15
	}
	if score < 0 {
		score = 0
	}

	fmt.Fprintln(out, score)
}
