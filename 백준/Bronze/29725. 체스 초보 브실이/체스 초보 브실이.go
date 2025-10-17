package main

import (
	"bufio"
	"fmt"
	"os"
)

var CHESSMAN = map[byte]int{
	'k': 0,
	'p': 1,
	'n': 3,
	'b': 3,
	'r': 5,
	'q': 9,
}

func lower(c byte) byte {
	if c >= 'A' && c <= 'Z' {
		return c + 32
	}
	return c
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	total := 0
	for i := 0; i < 8; i++ {
		var s string
		fmt.Fscan(in, &s)

		for j := 0; j < 8; j++ {
			ch := s[j]
			key := lower(ch)

			if score, ok := CHESSMAN[key]; ok {
				if ch >= 'a' && ch <= 'z' {
					total -= score
				} else {
					total += score
				}
			}
		}
	}

	fmt.Fprintln(out, total)
}
