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
	a, _ := strconv.Atoi(reader.Text())

	reader.Scan()
	b, _ := strconv.Atoi(reader.Text())

	fmt.Fprintln(writer, len(strconv.Itoa(a+b)))
}
