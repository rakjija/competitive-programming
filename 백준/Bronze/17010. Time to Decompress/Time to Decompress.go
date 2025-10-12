package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var l int
	fmt.Fscan(in, &l)

	for i := 0; i < l; i++ {
		var n int
		var char string
		fmt.Fscan(in, &n, &char)

		fmt.Fprintln(out, strings.Repeat(char, n))
	}
}
