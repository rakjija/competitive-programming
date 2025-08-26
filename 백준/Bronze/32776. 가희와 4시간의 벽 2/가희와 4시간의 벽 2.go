package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	// sAB = station A to station B via train
	in.Scan()
	sAB, _ := strconv.Atoi(in.Text())

	// mA = station A to airport B
	// fAB = airport A to airport B
	// mB = airport B to station B
	in.Scan()
	parts := strings.Fields(in.Text())
	mA, _ := strconv.Atoi(parts[0])
	fAB, _ := strconv.Atoi(parts[1])
	mB, _ := strconv.Atoi(parts[2])

	result := "flight"
	if (sAB <= 240) || (sAB <= mA+fAB+mB) {
		result = "high speed rail"
	}
	fmt.Fprintln(out, result)
}
