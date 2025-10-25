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

	var l, t int
	for i := 0; i < 9; i++ {
		var s string
		fmt.Fscan(in, &s)

		switch s {
		case "Lion":
			l++
		case "Tiger":
			t++
		}
	}

	if l > t {
		fmt.Fprintln(out, "Lion")
	} else {
		fmt.Fprintln(out, "Tiger")
	}
}
