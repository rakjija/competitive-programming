package main

import (
	"fmt"
)

func getExamResult(S, I, T int) string {
	if S+I+T < 55 {
		return "FAIL"
	}

	if float32(S) < 35*0.3 {
		return "FAIL"
	}

	if float32(I) < 30*0.25 {
		return "FAIL"
	}

	if float32(T) < 30*0.40 {
		return "FAIL"
	}

	return "PASS"
}

func main() {
	var N int
	fmt.Scanf("%d", &N)

	for i := 0; i < N; i++ {
		var examNumber, S, I, T int
		fmt.Scanf("%d %d %d %d", &examNumber, &S, &I, &T)

		fmt.Printf("%d %d %s\n", examNumber, S+I+T, getExamResult(S, I, T))
	}
}
