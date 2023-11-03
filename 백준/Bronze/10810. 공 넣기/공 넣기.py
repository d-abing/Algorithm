import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bucket = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i, j + 1):
        bucket[index] = k

print(*bucket[1:], sep=' ')
