package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	// m: 주차장을 한 바퀴 도는 데 걸리는 시간
	// k: 주차장의 온도(무시)
	// c: 주차 자리를 찾을 때까지 주차장을 돈 바퀴 수
	var m, k, c int
	fmt.Fscan(in, &m)
	fmt.Fscan(in, &k)
	fmt.Fscan(in, &c)

	fmt.Fprintln(out, m*c)
}
