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

	var x, d int
	fmt.Fscan(in, &x, &d)

	if x <= d/2 {
		fmt.Fprintln(out, "double it")
	} else {
		fmt.Fprintln(out, "take it")
	}
}
