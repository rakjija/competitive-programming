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

	for true {
		in.Scan()
		input := in.Text()
		if input == "0" {
			break
		}
		n, _ := strconv.Atoi(input)

		in.Scan()
		parts := strings.Split(in.Text(), " ")

		max := 0
		cur := 0
		for i := 0; i < n; i++ {
			a, _ := strconv.Atoi(parts[i])

			if i < 3 {
				cur += a
			} else {
				grad, _ := strconv.Atoi(parts[i-3])
				cur -= grad
				cur += a
			}

			if max < cur {
				max = cur
			}
		}

		fmt.Fprintln(out, max)
		out.Flush()
	}
}
