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

	// w: 직사각형의 너비
	// l: 직사각형의 길이
	var w, l int
	fmt.Fscan(in, &w)
	fmt.Fscan(in, &l)

	fmt.Fprintln(out, w*l)
}
