package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	var N int
	fmt.Fscan(reader, &N)

	var max_name string
	max_score := -1

	for i := 0; i < N; i++ {
		var name string
		var score int
		fmt.Fscan(reader, &name, &score)

		if score > max_score {
			max_name = name
			max_score = score
		} else if score == max_score && name < max_name {
			max_name = name
		}
	}

	fmt.Println(max_name)
}
