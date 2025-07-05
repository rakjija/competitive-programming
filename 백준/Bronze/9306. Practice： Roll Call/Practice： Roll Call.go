package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	for i := 1; i <= n; i++ {
		var firstName string
		var lastName string

		fmt.Scanf("%s", &firstName)
		fmt.Scanf("%s", &lastName)

		fmt.Printf("Case %d: %s, %s\n", i, lastName, firstName)
	}
}
