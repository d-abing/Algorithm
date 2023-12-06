import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
computer = [0] * (N + 1)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        out = queue.popleft()
        for num in graph[out]:
            if not visited[num]:
                visited[num] = True
                computer[v] += 1
                queue.append(num)


for _ in range(M):
    s, e = map(int, input().split())
    graph[e].append(s)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    bfs(i)

max_value = 0
for i in range(1, N + 1):
    max_value = max(max_value, computer[i])

for i in range(1, N + 1):
    if computer[i] == max_value:
        print(i, end=' ')
