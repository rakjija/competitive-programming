package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func timeToSeconds(timeString string) int {
	parts := strings.Split(timeString, ":")
	h, _ := strconv.Atoi(strings.TrimSpace(parts[0]))
	m, _ := strconv.Atoi(strings.TrimSpace(parts[1]))
	s, _ := strconv.Atoi(strings.TrimSpace(parts[2]))
	return (h * 60 * 60) + (m * 60) + s
}

func main() {
	reader := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	reader.Scan()
	start_seconds := timeToSeconds(reader.Text())

	reader.Scan()
	end_seconds := timeToSeconds(reader.Text())

	result := end_seconds - start_seconds
	if result < 0 {
		result += 24 * 60 * 60
	}

	fmt.Fprintln(writer, result)
}
