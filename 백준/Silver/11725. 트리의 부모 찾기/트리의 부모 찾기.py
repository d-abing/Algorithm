import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
result = [0] * (N + 1)
def bfs(v):
    queue = deque()
    visited[v] = True
    queue.append(v)
    while queue:
        p = queue.popleft()
        for c in graph[p]:
            if not visited[c]:
                visited[c] = True
                result[c] = p
                queue.append(c)


bfs(1)
print(*result[2:], sep='\n')