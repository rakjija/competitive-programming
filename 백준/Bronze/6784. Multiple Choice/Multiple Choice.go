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
	N, _ := strconv.Atoi(reader.Text())

	responses := make([]string, N)
	for i := 0; i < N; i++ {
		reader.Scan()
		responses[i] = reader.Text()
	}

	correctCount := 0
	for i := 0; i < N; i++ {
		reader.Scan()
		correct := reader.Text()
		if responses[i] == correct {
			correctCount += 1
		}
	}

	fmt.Fprintln(writer, correctCount)
}
