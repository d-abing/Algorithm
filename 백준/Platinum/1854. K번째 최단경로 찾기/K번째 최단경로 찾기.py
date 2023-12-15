import sys
from queue import PriorityQueue

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
D = [[200_000_000] * k for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start = 1
D[start][0] = 0
pq = PriorityQueue()
pq.put((0, start))

while pq.qsize() > 0:
    select_d, select_node = pq.get()
    for pair in graph[select_node]:
        total_d = select_d + pair[1]
        if D[pair[0]][k - 1] > total_d:
            D[pair[0]][k - 1] = total_d
            D[pair[0]].sort()
            pq.put((total_d, pair[0]))

for d in D[1:]:
    if d[k - 1] == 200_000_000:
        print(-1)
    else:
        print(d[k - 1])
