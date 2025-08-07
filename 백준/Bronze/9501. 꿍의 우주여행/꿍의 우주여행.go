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
	T, _ := strconv.Atoi(reader.Text())

	for i := 0; i < T; i++ {
		count := 0

		reader.Scan()
		parts := strings.Split(reader.Text(), " ")
		N, _ := strconv.Atoi(parts[0])
		D, _ := strconv.Atoi(parts[1])

		for j := 0; j < N; j++ {
			reader.Scan()
			parts := strings.Split(reader.Text(), " ")
			v, _ := strconv.Atoi(parts[0])
			f, _ := strconv.Atoi(parts[1])
			c, _ := strconv.Atoi(parts[2])

			if D*c <= v*f {
				count += 1
			}
		}

		fmt.Fprintln(writer, count)
	}
}
