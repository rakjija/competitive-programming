package main

import (
	"fmt"
)

func main() {
	var x int
	var op string
	var y int

	fmt.Scanf("%d", &x)
	result := x

	for true {
		fmt.Scanf("%s", &op)
		if op == "=" {
			break
		}

		fmt.Scanf("%d", &y)
		switch op {
		case "+":
			result += y
		case "-":
			result -= y
		case "*":
			result *= y
		case "/":
			result /= y
		}
	}

	fmt.Println(result)
}
