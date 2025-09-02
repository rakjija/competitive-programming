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
	for idx := 0; idx < n; idx++ {
		in.Scan()
		inputParts := strings.Fields(in.Text())
		textParts := strings.Split(inputParts[0], "")
		i, _ := strconv.Atoi(inputParts[1])
		j, _ := strconv.Atoi(inputParts[2])

		resultText := strings.Join(append(textParts[:i], textParts[j:]...), "")

		fmt.Fprintln(out, resultText)
	}
}
