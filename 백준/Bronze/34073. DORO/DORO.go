package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	reader.Scan()
	n, _ := strconv.Atoi(reader.Text())

	reader.Scan()
	parts := strings.Split(reader.Text(), " ")

	for i := 0; i < n; i++ {
		parts[i] += "DORO"
	}
	result := strings.Join(parts, " ")

	fmt.Fprintln(writer, result)
}
