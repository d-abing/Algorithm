import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D = [[sys.maxsize for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    D[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    D[a][b] = 1
    D[b][a] = 1

for K in range(1, N + 1):
    for S in range(1, N + 1):
        for E in range(1, N + 1):
            if D[S][E] > D[S][K] + D[K][E]:
                D[S][E] = D[S][K] + D[K][E]

result = []

for d in D[1:]:
    result.append(sum(d[1:]))

print(result.index(min(result)) + 1)