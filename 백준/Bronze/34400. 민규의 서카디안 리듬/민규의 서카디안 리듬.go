package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)

	var T int
	fmt.Fscan(in, &T)

	for i := 0; i < T; i++ {
		var t int
		fmt.Fscan(in, &t)

		if t%25 >= 17 {
			fmt.Fprintln(out, "OFFLINE")
		} else {
			fmt.Fprintln(out, "ONLINE")
		}

		out.Flush()
	}
}
