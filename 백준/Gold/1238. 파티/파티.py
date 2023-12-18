import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
D_go_home = [sys.maxsize] * (N + 1)
D_go_party = [sys.maxsize] * (N + 1)
visited = [False] * (N + 1)

for _ in range(M):
    s, e, T = map(int, input().split())
    graph[s].append((e, T))

D_go_home[X] = 0
pq = PriorityQueue()
pq.put((0, X))

while pq.qsize() > 0:
    village = pq.get()[1]
    if not visited[village]:
        visited[village] = True
        for pair in graph[village]:
            if not visited[pair[0]] and D_go_home[pair[0]] > D_go_home[village] + pair[1]:
                D_go_home[pair[0]] = D_go_home[village] + pair[1]
                pq.put((D_go_home[pair[0]], pair[0]))


def dijkstra(n, X):
    D_go_party = [sys.maxsize] * (N + 1)
    visited = [False] * (N + 1)
    D_go_party[n] = 0
    pq = PriorityQueue()
    pq.put((0, n))

    while pq.qsize() > 0:
        village = pq.get()[1]
        if not visited[village]:
            visited[village] = True
            for pair in graph[village]:
                if not visited[pair[0]] and D_go_party[pair[0]] > D_go_party[village] + pair[1]:
                    D_go_party[pair[0]] = D_go_party[village] + pair[1]
                    pq.put((D_go_party[pair[0]], pair[0]))
    return D_go_party[X]

for i in range(1, N + 1):
    D_go_home[i] += dijkstra(i, X)

print(max(D_go_home[1:]))
