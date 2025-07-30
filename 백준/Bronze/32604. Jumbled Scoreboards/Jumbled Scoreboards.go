package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	prevA, prevB := 0, 0
	isTimeSeries := true

	for i := 0; i < n; i++ {
		var a, b int
		fmt.Scanf("%d %d", &a, &b)

		if prevA > a || prevB > b {
			isTimeSeries = false
		}

		prevA = a
		prevB = b
	}

	if isTimeSeries {
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}
}
