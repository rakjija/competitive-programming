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

	result := "True"
	for i := 0; i < n; i++ {
		var t int
		fmt.Fscan(in, &t)

		if result == "False" {
			continue
		}

		if t < 48 {
			result = "False"
		}
	}

	fmt.Fprintln(out, result)
}
