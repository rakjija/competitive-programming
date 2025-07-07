package main

import (
	"fmt"
)

func isTriangle(a, b, c int) bool {
	return a+b > c && b+c > a && c+a > b
}

func isRightTriangle(a, b, c int) bool {
	return a*a == b*b+c*c || b*b == c*c+a*a || c*c == a*a+b*b
}

func main() {
	var a, b, c int

	fmt.Scanf("%d %d %d", &a, &b, &c)

	if !isTriangle(a, b, c) {
		fmt.Println(0)
	} else if a == b && b == c {
		fmt.Println(2)
	} else if isRightTriangle(a, b, c) {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}
