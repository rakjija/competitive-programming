def base12(n):
    digits = "0123456789ab"  # 12진수에선 10=A, 11=B
    result = ""
    while n > 0:
        result = digits[n % 12] + result
        n //= 12
    return result or "0"


for n in range(1000, 10000):
    dec_sum = sum(int(c) for c in str(n))
    base12_sum = sum(int(c, 12) for c in base12(n))
    hex_sum = sum(int(c, 16) for c in hex(n)[2:])

    if dec_sum == base12_sum == hex_sum:
        print(n)
