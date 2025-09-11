package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	// t: 테스트 케이스
	var t int
	fmt.Fscan(in, &t)

	for i := 0; i < t; i++ {
		// n: 문제 개수
		var n int
		fmt.Fscan(in, &n)

		for j := 0; j < n; j++ {
			// a, b: 연산 대상 정수
			var a, b int
			fmt.Fscan(in, &a, &b)

			fmt.Fprintf(out, "%d %d\n", a+b, a*b)
		}
	}
}
