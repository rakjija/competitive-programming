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
	n, _ := strconv.Atoi(in.Text())

	in.Scan()
	parts := strings.Split(in.Text(), " ")

	totalPage := 0
	for i := 0; i < n; i++ {
		page, _ := strconv.Atoi(parts[i])
		totalPage += page/2 + page%2
	}

	fmt.Fprintln(out, totalPage)
}
