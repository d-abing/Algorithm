from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
numbers = [[0] * (N + 1)]

for _ in range(N):
    line = list(map(int, input().split()))
    numbers.append([0] + line)

for i in range(N * N):
    numbers[i // N + 1][i % N + 1] = numbers[i // N][i % N + 1] + numbers[i // N + 1][i % N] - numbers[i // N][i % N] + numbers[i // N + 1][i % N + 1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])