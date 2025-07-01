package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	if n < 5 {
		if n == 0 {
			fmt.Println(1)
		}
		if n == 1 {
			fmt.Println(1)
		}
		if n == 2 {
			fmt.Println(2)
		}
		if n == 3 {
			fmt.Println(6)
		}
		if n == 4 {
			fmt.Println(4)
		}
	} else {
		fmt.Println(0)
	}
}
