import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
D = [0] * (N + 1)
D[0] = -1

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    D[B] += 1

queue = deque()
for i in range(1, N + 1):
    if D[i] == 0:
        queue.append(i)

result = []

while queue:
    out = queue.popleft()
    result.append(out)
    for i in graph[out]:
        D[i] -= 1
        if D[i] == 0:
            queue.append(i)

print(*result)
