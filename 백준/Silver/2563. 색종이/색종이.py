import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append((a, b))

paper = [[0] * 100 for _ in range(100)]

for i in range(N):
    x = A[i][0]
    y = A[i][1]
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            paper[j][k] = 1

count = 0
for p_list in paper:
    for p in p_list:
        if p == 1:
            count += 1

print(count)
