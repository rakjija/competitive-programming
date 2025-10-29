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

	var s string
	fmt.Fscan(in, &s)

	seen := make([]bool, 26)
	for _, r := range s {
		if r >= 'A' && r <= 'Z' {
			seen[r-'A'] = true
		}
	}

	for i := 0; i < 26; i++ {
		if !seen[i] {
			fmt.Fprintln(out, string('A'+i))
			return
		}
	}
}
