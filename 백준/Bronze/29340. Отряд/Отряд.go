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

	var a, b string
	fmt.Fscan(in, &a, &b)

	result := make([]byte, len(a))

	for i := 0; i < len(a); i++ {
		if a[i] >= b[i] {
			result[i] = a[i]
		} else {
			result[i] = b[i]
		}
	}

	fmt.Fprintln(out, string(result))
}
