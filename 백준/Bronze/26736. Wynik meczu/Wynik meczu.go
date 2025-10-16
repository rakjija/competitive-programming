package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var s string
	fmt.Fscan(in, &s)

	aScore, bScore := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'A' {
			aScore++
		}
		if s[i] == 'B' {
			bScore++
		}
	}

	fmt.Fprintln(out, strconv.Itoa(aScore)+" : "+strconv.Itoa(bScore))
}
