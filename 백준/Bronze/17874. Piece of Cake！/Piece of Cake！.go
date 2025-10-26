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

	var n, h, v int
	fmt.Fscan(in, &n, &h, &v)

	fmt.Fprintln(out, max(h, n-h)*max(v, n-v)*4)
}
