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
	parts := strings.Split(reader.Text(), "/")
	k, _ := strconv.Atoi(parts[0])
	d, _ := strconv.Atoi(parts[1])
	a, _ := strconv.Atoi(parts[2])

	result := "gosu"
	if k+a < d || d == 0 {
		result = "hasu"
	}
	fmt.Fprintln(writer, result)
}
