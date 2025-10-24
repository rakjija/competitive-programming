package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var s string
	fmt.Fscan(in, &s)

	e := strings.Repeat("e", strings.Count(s, "e")*2)
	fmt.Fprintln(out, "h"+e+"y")
}
