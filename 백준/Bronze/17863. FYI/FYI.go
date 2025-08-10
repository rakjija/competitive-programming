package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	reader.Scan()
	N := reader.Text()

	result := "NO"
	if N[:3] == "555" {
		result = "YES"
	}

	fmt.Fprintln(writer, result)
}
