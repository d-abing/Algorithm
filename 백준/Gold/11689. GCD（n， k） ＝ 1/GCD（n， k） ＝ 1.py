import math

N = int(input())
result = N

for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        result -= result // i
        while N % i == 0:
            N //= i

if N > 1:
    result -= result // N

print(result)
