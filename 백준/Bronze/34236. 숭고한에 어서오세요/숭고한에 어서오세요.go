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

	years := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &years[i])
	}

	diff := years[1] - years[0]
	next := years[n-1] + diff

	fmt.Fprintln(out, next)
}
