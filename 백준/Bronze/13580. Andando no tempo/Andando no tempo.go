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

	var a, b, c int
	fmt.Fscan(in, &a, &b, &c)

	if a == b || b == c || c == a {
		// 2번 여행
		fmt.Fprintln(out, "S")
	} else if a+b == c || b+c == a || c+a == b {
		// 3번 여행
		fmt.Fprintln(out, "S")
	} else {
		fmt.Fprintln(out, "N")
	}
}
