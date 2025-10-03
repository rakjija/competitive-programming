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

	var n int64
	fmt.Fscan(in, &n)

	var fact int64 = 1
	for i := int64(2); i <= n; i++ {
		fact *= i
	}

	const weekSeconds int64 = 60 * 60 * 24 * 7

	fmt.Fprintln(out, fact/weekSeconds)
}
