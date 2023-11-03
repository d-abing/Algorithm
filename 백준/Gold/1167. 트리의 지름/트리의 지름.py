import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
distance = [0] * (V + 1)

for _ in range(V):
    data = list(map(int, input().split()))
    for i in range(1, len(data), 2):
        if data[i] == -1:
            break
        graph[data[0]].append((data[i], data[i + 1]))

max_length_node = 0


def bfs(v):
    global max_length_node
    queue = deque()
    visited[v] = True
    queue.append(v)
    while queue:
        out = queue.popleft()
        for data_set in graph[out]:
            n, d = data_set
            if not visited[n]:
                visited[n] = True
                queue.append(n)
                distance[n] = distance[out] + d
    max_length_node = distance.index(max(distance))


bfs(1)
visited = [False for _ in range(V + 1)]
distance = [0] * (V + 1)
bfs(max_length_node)
print(max(distance))
