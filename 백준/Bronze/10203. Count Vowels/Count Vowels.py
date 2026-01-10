import sys
from typing import cast

t = int(sys.stdin.readline())

for _ in range(t):
    word = cast(str, sys.stdin.readline().strip())
    vowel_count = 0
    for char in word:
        if char.lower() in "aeiou":
            vowel_count += 1
    print(f"The number of vowels in {word} is {vowel_count}.")
