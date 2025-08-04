package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	reader.Scan()
	T, _ := strconv.Atoi(reader.Text())

	for i := 0; i < T; i++ {
		reader.Scan()
		N, _ := strconv.Atoi(reader.Text())
		fmt.Fprintln(writer, N*N)
	}
}
