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
	runes := []rune(s)

	for i := 0; i < n; i++ {
		if i != 0 && runes[i] == 'J' {
			fmt.Fprintln(out, string(runes[i-1]))
		}
	}
}
