A, B, C = map(int, input().split())

result = [0] * (A + B + C + 1)

for i in range(1, A + 1):
    for j in range(1, B + 1):
        for k in range(1, C + 1):
            result[i + j + k] += 1

print(result.index(max(result)))
