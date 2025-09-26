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

	var a, b, c, d int
	fmt.Fscan(in, &a, &b, &c, &d)

	result := "answer"
	if (a == 8 || a == 9) && (d == 8 || d == 9) && b == c {
		result = "ignore"
	}

	fmt.Fprintln(out, result)
}
