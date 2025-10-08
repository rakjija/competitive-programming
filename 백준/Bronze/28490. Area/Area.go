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

	largest := 0
	for i := 0; i < n; i++ {
		var h, w int
		fmt.Fscan(in, &h, &w)

		if largest < h*w {
			largest = h * w
		}
	}

	fmt.Fprintln(out, largest)
}
