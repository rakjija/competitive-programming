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

	var w int
	fmt.Fscan(in, &w)

	var n int
	fmt.Fscan(in, &n)

	fmt.Fprintln(out, (w*5280)/n)
}
