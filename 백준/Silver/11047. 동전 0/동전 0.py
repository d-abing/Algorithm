import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
count = 0

for coin in coins[-1:-(N + 1):-1]:
    if coin <= K:
        count += K // coin
        K = K % coin
        if K == 0:
            break

print(count)
