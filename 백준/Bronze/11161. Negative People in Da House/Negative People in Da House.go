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
		reader.Scan()
		M, _ := strconv.Atoi(reader.Text())

		cur := 0
		minCur := 0
		for j := 0; j < M; j++ {
			reader.Scan()
			parts := strings.Split(reader.Text(), " ")
			p1, _ := strconv.Atoi(parts[0])
			p2, _ := strconv.Atoi(parts[1])

			cur += p1 - p2

			if cur < minCur {
				minCur = cur
			}
		}

		need := 0
		if minCur < 0 {
			need = -minCur
		}
		fmt.Fprintln(writer, need)
	}
}
