import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

D = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    D[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if D[a][b] > c:
        D[a][b] = c

for K in range(1, n + 1):
    for S in range(1, n + 1):
        for E in range(1, n + 1):
            if D[S][E] > D[S][K] + D[K][E]:
                D[S][E] = D[S][K] + D[K][E]

for d in D[1:]:
    for num in d[1:]:
        if num == sys.maxsize:
            num = 0
        print(num, end=' ')
    print()