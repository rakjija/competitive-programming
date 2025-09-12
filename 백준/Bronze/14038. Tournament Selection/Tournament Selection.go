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

	count := 0
	for i := 0; i < 6; i++ {
		var result string
		fmt.Fscan(in, &result)
		if result == "W" {
			count += 1
		}
	}

	switch count {
	case 5, 6:
		fmt.Fprintln(out, 1)
	case 3, 4:
		fmt.Fprintln(out, 2)
	case 1, 2:
		fmt.Fprintln(out, 3)
	default:
		fmt.Fprintln(out, -1)
	}
}
