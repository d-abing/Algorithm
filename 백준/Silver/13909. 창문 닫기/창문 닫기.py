import math
N = int(input())

result = 0

for i in range(1, int(math.sqrt(N)) + 1):
    if i * i <= N:
        result += 1

print(result)