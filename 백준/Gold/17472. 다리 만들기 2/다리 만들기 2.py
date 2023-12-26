import sys
from collections import deque
from queue import PriorityQueue

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

islands = []

def bfs(a, b, island_num):
    queue = deque()
    one_island = []
    visited[a][b] = True
    graph[a][b] = island_num
    queue.append((a, b))
    one_island.append((a, b))
    while queue:
        a, b = queue.popleft()
        for d in range(4):
            r = dr[d]
            c = dc[d]
            if 0 <= a + r < N and 0 <= b + c < M:
                if graph[a + r][b + c] == 1 and not visited[a + r][b + c]:
                    visited[a + r][b + c] = True
                    graph[a + r][b + c] = island_num
                    queue.append((a + r, b + c))
                    one_island.append((a + r, b + c))
    return one_island


island_num = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            island_num += 1
            islands.append(bfs(i, j, island_num))

pq = PriorityQueue()

for coordinate in islands:
    for a, b in coordinate:
        now = graph[a][b]
        for d in range(4):
            r = dr[d]
            c = dc[d]
            bridge = 0
            while 0 <= a + r < N and 0 <= b + c < M:
                if graph[a + r][b + c] == now:
                    break
                elif graph[a + r][b + c] != 0:
                    if bridge > 1:
                        pq.put((bridge, now, graph[a + r][b + c]))
                    break
                else:
                    bridge += 1

                if r < 0:
                    r -= 1
                elif r > 0:
                    r += 1
                elif c < 0:
                    c -= 1
                elif c > 0:
                    c += 1


union_find_list = [i for i in range(island_num + 1)]


def union(a, b):
    a = find(a)
    b = find(b)
    union_find_list[a] = b


def find(num):
    if union_find_list[num] != num:
        union_find_list[num] = find(union_find_list[num])
        return union_find_list[num]
    else:
        return num


result = 0
linked_edge = 0
while linked_edge < island_num - 1 and pq.qsize() > 0:
    c, a, b = pq.get()
    if find(a) != find(b):
        union(a, b)
        result += c
        linked_edge += 1


if linked_edge == island_num - 1:
    print(result)
else:
    print(-1)
