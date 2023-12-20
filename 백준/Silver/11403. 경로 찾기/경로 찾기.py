import sys
input = sys.stdin.readline
N = int(input())

D = [list(map(int, input().split())) for _ in range(N)]

for K in range(N):
    for S in range(N):
        for E in range(N):
            if D[S][K] == 1 and D[K][E] == 1:
                D[S][E] = 1

for d in D:
    print(*d)