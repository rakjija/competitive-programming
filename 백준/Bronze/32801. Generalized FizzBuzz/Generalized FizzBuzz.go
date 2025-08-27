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
	n, _ := strconv.Atoi(parts[0])
	a, _ := strconv.Atoi(parts[1])
	b, _ := strconv.Atoi(parts[2])

	fizz, buzz, fizzbuzz := 0, 0, 0
	for i := 1; i < n+1; i++ {
		if i%a == 0 && i%b == 0 {
			fizzbuzz++
			continue
		}
		if i%a == 0 {
			fizz++
			continue
		}
		if i%b == 0 {
			buzz++
			continue
		}
	}

	fmt.Fprintln(out, fizz, buzz, fizzbuzz)
}
