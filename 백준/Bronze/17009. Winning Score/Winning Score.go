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

	var a, b, total int

	for i := 3; i > 0; i-- {
		fmt.Fscan(in, &a)
		total += i * a
	}

	for i := 3; i > 0; i-- {
		fmt.Fscan(in, &b)
		total -= i * b
	}

	if total > 0 {
		fmt.Fprintln(out, "A")
	} else if total < 0 {
		fmt.Fprintln(out, "B")
	} else {
		fmt.Fprintln(out, "T")
	}
}
