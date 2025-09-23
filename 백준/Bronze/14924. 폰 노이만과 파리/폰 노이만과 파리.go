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

	var s, t, d int
	fmt.Fscan(in, &s, &t, &d)

	fmt.Fprintln(out, d/(s*2)*t)
}
