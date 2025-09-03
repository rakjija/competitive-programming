package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func absInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)

	in.Scan()
	scoreBoard := strings.Split(in.Text(), "")

	var a, b int
	isTenTen := false
	for i := 0; i < len(scoreBoard); i += 2 {
		score, _ := strconv.Atoi(scoreBoard[i+1])

		if scoreBoard[i] == "A" {
			a += score
		} else {
			b += score
		}

		if a == 10 && b == 10 {
			isTenTen = true
		}

		if isTenTen {
			if absInt(a-b) >= 2 {
				break
			}
		} else {
			if a >= 11 || b >= 11 {
				break
			}
		}
	}

	var result string
	if a > b {
		result = "A"
	} else {
		result = "B"
	}

	fmt.Fprintln(out, result)
	out.Flush()
}
