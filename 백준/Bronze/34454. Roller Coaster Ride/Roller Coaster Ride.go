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
	fmt.Fscan(in, &n)
	fmt.Fscan(in, &c)
	fmt.Fscan(in, &p)

	if c*p >= n {
		fmt.Fprintln(out, "yes")
	} else {
		fmt.Fprintln(out, "no")
	}
}
