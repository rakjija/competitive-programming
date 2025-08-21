package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	result := "JAH"
	for i := 0; i < 3; i++ {
		in.Scan()
		choice, _ := strconv.Atoi(in.Text())

		switch i {
		case 0:
			if choice != 1 && choice != 3 {
				result = "EI"
			}
		case 1:
			if choice != 6 && choice != 8 {
				result = "EI"
			}
		case 2:
			if choice != 2 && choice != 5 {
				result = "EI"
			}
		}
	}

	fmt.Fprintln(out, result)
}
