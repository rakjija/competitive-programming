package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scanf("%s", &s)

	splits := strings.Split(s, "(^0^)")
	left := strings.Count(splits[0], "@=")
	right := strings.Count(splits[1], "=@")

	fmt.Println(left, right)
}
