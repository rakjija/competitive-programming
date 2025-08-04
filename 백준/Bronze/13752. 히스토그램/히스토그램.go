package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		var k int
		fmt.Scanf("%d", &k)

		fmt.Println(strings.Repeat("=", k))
	}
}
