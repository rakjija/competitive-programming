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

	var m, v int
	fmt.Fscan(in, &m, &v)

	var n int
	fmt.Fscan(in, &n)

	var k int
	fmt.Fscan(in, &k)

	fmt.Fprintln(out, (n+20)*2)
}
