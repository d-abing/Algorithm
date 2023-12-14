import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
D = [1_000_000_000_000] * (N + 1)
visited = [False] * (N + 1)

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())
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

print(D[end])
