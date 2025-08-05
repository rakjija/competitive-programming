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

	parts := strings.Split(reader.Text(), " ")

	n, _ := strconv.Atoi(parts[0])
	d, _ := strconv.Atoi(parts[1])

	solved := make([]int, n)
	total := 0

	for i := 0; i < n; i++ {
		reader.Scan()
		solved[i], _ = strconv.Atoi(reader.Text())
		total += solved[i]
	}

	reward := d / total

	for _, v := range solved {
		fmt.Fprintln(writer, v*reward)
	}
}
