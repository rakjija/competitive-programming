package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "#" {
			break
		}

		char := string(line[0])
		sentence := strings.ToLower(line[2:])

		count := 0
		for _, r := range sentence {
			if string(r) == char {
				count++
			}
		}
		fmt.Printf("%s %d\n", char, count)
	}
}
