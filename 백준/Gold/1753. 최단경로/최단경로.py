import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
D = [3_000_000] * (V + 1)
visited = [False] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

D[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while pq.qsize() > 0:
    select_node = pq.get()[1]
    if visited[select_node]:
        continue
    visited[select_node] = True
    for pair in graph[select_node]:
        D[pair[0]] = min(D[select_node] + pair[1], D[pair[0]])
        pq.put((D[pair[0]], pair[0]))


for d in D[1:]:
    if d == 3_000_000:
        print("INF")
    else:
        print(d)
