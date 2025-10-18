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

	var input rune
	fmt.Fscanf(in, "%c", &input)

	fmt.Fprintln(out, int(input-'가'+1))
}
