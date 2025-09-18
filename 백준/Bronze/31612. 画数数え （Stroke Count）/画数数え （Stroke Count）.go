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

	var n int
	fmt.Fscan(in, &n)

	var s string
	fmt.Fscan(in, &s)

	result := 0
	for _, ch := range s {
		switch ch {
		case 'i', 'j':
			result += 2
		case 'o':
			result += 1
		}
	}
	fmt.Fprintln(out, result)
}
