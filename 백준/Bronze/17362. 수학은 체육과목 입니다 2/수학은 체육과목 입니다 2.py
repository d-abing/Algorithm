n = int(input())
if n <= 5:
    print(n)
else:
    tmp = n - 5
    tmp_quotient = tmp // 4
    tmp_remainder = tmp % 4
    result = 0
    if tmp_quotient % 2 == 0:
        result = 5 - tmp_remainder
    else:
        result = 1 + tmp_remainder
    print(result)
        
        