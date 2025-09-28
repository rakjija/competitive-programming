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

	var x, y, z int
	var u, v, w int

	fmt.Fscan(in, &x, &y, &z)
	fmt.Fscan(in, &u, &v, &w)

	a := (u / 100) * x
	b := (v / 50) * y
	c := (w / 20) * z

	fmt.Fprintln(out, a+b+c)
}
