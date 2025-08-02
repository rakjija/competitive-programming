package main

import (
	"fmt"
)

func AbsInt(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func main() {
	var a, b, c, d int

	fmt.Scanf("%d %d %d %d", &a, &b, &c, &d)

	fmt.Println(AbsInt((a + d) - (b + c)))
}
