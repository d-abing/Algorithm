import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra (s):
    D = [sys.maxsize] * (N + 1)
    D[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))

    while pq.qsize() > 0:
        select_node = pq.get()[1]
        for pair in graph[select_node]:
            if D[pair[0]] > D[select_node] + pair[1]:
                D[pair[0]] = D[select_node] + pair[1]
                pq.put((D[pair[0]], pair[0]))
    return D

D_1 = dijkstra(1)
D_v1 = dijkstra(v1)
D_v2 = dijkstra(v2)

v1_v2 = D_1[v1] + D_v1[v2] + D_v2[N]
v2_v1 = D_1[v2] + D_v2[v1] + D_v1[N]

if min(v1_v2, v2_v1) >= sys.maxsize:
    print(-1)
else:
    print(min(v1_v2, v2_v1))