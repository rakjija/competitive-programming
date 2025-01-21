"""
"체크 배열"
1) 모든 값 0, 길이 42개 배열 생성
2) 0 -> 1 or 1 -> 1
3) 종류의 개수 = 배열 요소의 총합
"""

check = [0] * 42
for i in range(10):
    n = int(input())
    check[n % 42] = 1

sum = 0
for i in range(42):
    sum += check[i]

print(sum)
