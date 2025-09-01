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

	in.Scan()
	n, _ := strconv.Atoi(in.Text())

	for idx := 0; idx < n; idx++ {
		in.Scan()
		parts := strings.Fields(in.Text())
		i, _ := strconv.Atoi(parts[0])
		f, _ := strconv.Atoi(parts[1])

		var result string = "No"
		if (i <= 1 && f <= 2) || (i <= 2 && f <= 1) {
			result = "Yes"
		}
		fmt.Fprintln(out, result)
		out.Flush()
	}
}
