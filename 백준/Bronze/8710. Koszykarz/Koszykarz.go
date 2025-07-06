package main

import (
	"fmt"
)

func main() {
	var k, w, m int

	fmt.Scanf("%d %d %d", &k, &w, &m)

	count := 0
	for k < w {
		count += 1
		k += m
	}

	fmt.Println(count)
}
