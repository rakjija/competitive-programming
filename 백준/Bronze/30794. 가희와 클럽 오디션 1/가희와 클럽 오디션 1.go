package main

import (
	"fmt"
)

var judgeScore = map[string]int{
	"miss":    0,
	"bad":     200,
	"cool":    400,
	"great":   600,
	"perfect": 1000,
}

func main() {
	var lv int
	var judge string
	fmt.Scanf("%d %s", &lv, &judge)

	score, _ := judgeScore[judge]
	fmt.Println(lv * score)
}
