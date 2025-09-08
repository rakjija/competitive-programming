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

	total := 0
	for {
		var money int
		fmt.Fscan(in, &money)

		if money == -1 {
			break
		}

		total += money
	}

	fmt.Fprintln(out, total)
}
