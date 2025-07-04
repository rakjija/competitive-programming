package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)

	var min int
	if a > b {
		min = b
	} else {
		min = a
	}

	var result int
	if (a*b)%2 == 0 {
		result = 0
	} else {
		result = min
	}

	fmt.Println(result)
}
