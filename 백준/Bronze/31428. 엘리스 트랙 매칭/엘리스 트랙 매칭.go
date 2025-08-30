package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)

	var n int
	fmt.Fscan(r, &n)

	applyTracks := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &applyTracks[i])
	}

	var hellobitTrack string
	fmt.Fscan(r, &hellobitTrack)

	count := 0
	for _, t := range applyTracks {
		if t == hellobitTrack {
			count++
		}
	}

	fmt.Println(count)
}
