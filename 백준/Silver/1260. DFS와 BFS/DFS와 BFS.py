import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
queue = deque()

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for nodes in graph:
    nodes.sort()


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for num in graph[v]:
        if not visited[num]:
            dfs(num)


def bfs(v):
    visited[v] = True
    queue.append(v)
    while queue:
        out = queue.popleft()
        print(out, end=' ')
        for num in graph[out]:
            if not visited[num]:
                visited[num] = True
                queue.append(num)


dfs(V)
print()
visited = [False for _ in range(N + 1)]
bfs(V)
