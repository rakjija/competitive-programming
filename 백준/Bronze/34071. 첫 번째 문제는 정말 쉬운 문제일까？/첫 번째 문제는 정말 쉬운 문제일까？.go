package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	in.Scan()
	n, _ := strconv.Atoi(in.Text())

	s := make([]int, n)
	for i := 0; i < n; i++ {
		in.Scan()
		x, _ := strconv.Atoi(in.Text())
		s[i] = x
	}
	first := s[0]
	sort.Ints(s)

	idx := sort.SearchInts(s, first)
	var result string
	switch idx {
	case 0:
		result = "ez"
	case n - 1:
		result = "hard"
	default:
		result = "?"
	}

	fmt.Fprintln(out, result)
}
