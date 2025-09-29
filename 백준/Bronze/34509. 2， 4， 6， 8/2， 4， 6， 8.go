package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	for i := 11; i < 100; i++ {
		a := i / 10
		b := i % 10

		if ((b*10)+a)%4 != 0 {
			continue
		}

		if (a+b)%6 != 0 {
			continue
		}

		if a == 8 || b == 8 {
			continue
		}

		fmt.Fprintln(out, i)
		break
	}
}
