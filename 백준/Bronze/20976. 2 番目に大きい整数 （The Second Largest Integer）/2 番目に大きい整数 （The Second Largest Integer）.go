package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	numbers := make([]int, 3)
	fmt.Fscan(in, &numbers[0], &numbers[1], &numbers[2])

	sort.Slice(numbers, func(i, j int) bool {
		return numbers[i] > numbers[j]
	})

	fmt.Fprintln(out, numbers[1])
}
