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
	inParts := strings.Split(in.Text(), "")

	outParts := make([]string, n)
	for i := 0; i < n; i++ {
		// J -> O
		// O -> I
		// I -> J
		switch inParts[i] {
		case "J":
			outParts[i] = "O"
		case "O":
			outParts[i] = "I"
		case "I":
			outParts[i] = "J"
		default:
			outParts[i] = inParts[i]
		}
	}
	result := strings.Join(outParts[:], "")
	fmt.Fprintln(out, result)
}
