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

	var n, c, p int
	fmt.Fscan(in, &n, &c, &p)

	fmt.Fprintln(out, n*p)
}
