package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	in.Scan()
	parts := strings.Fields(in.Text())
	k, _ := strconv.Atoi(parts[0])
	n, _ := strconv.Atoi(parts[1])

	min := n + 1
	max := (k * n) + 1

	fmt.Fprintln(out, min, max)
}
