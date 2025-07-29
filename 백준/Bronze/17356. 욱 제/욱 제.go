package main

import (
	"fmt"
	"math"
)

func main() {
	var A, B int
	fmt.Scanf("%d %d", &A, &B)

	M := float64(B-A) / 400.0
	result := 1.0 / (1.0 + math.Pow(10, M))

	fmt.Printf("%.15f\n", result)
}
