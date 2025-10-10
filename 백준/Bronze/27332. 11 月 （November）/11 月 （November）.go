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

	var a, b int
	fmt.Fscan(in, &a, &b)

	if b*7+a > 30 {
		fmt.Fprintln(out, 0)
	} else {
		fmt.Fprintln(out, 1)
	}
}
