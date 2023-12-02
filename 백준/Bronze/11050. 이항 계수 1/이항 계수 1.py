N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= (N - i)

for i in range(K):
    result /= (K - i)

print(int(result))