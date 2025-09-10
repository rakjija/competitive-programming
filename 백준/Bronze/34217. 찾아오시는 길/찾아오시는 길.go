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

	// 출발지 -> 한양대역: a
	// 출발지 -> 용답역: b
	// 한양대역 -> ITBT : c
	// 용답역 -> ITBT: d
	var a, b, c, d int
	fmt.Fscan(in, &a, &b)
	fmt.Fscan(in, &c, &d)

	if a+c < b+d {
		fmt.Fprintln(out, "Hanyang Univ.")
	} else if a+c > b+d {
		fmt.Fprintln(out, "Yongdap")
	} else {
		fmt.Fprintln(out, "Either")
	}
}
