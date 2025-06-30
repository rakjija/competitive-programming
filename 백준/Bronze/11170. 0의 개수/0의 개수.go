package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var T int
	fmt.Scanf("%d", &T)

	for i := 0; i < T; i++ {
		var N int
		var M int
		fmt.Scanf("%d %d", &N, &M)

		count := 0
		for j := N; j <= M; j++ {
			s := strconv.Itoa(j)
			count += strings.Count(s, "0")
		}
		fmt.Println(count)
	}
}
