import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [-1 for _ in range(N + 1)]
queue = deque()

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)


def bfs(v):
    visited[v] = 0
    queue.append(v)
    while queue:
        pre_num = queue.popleft()
        for num in graph[pre_num]:
            if visited[num] == -1:
                visited[num] = visited[pre_num] + 1
                queue.append(num)

bfs(X)
answer = []

for i, distance in enumerate(visited):
    if distance == K:
        answer.append(i)

answer.sort()

if len(answer) != 0:
    print(*answer, sep='\n')
else:
    print(-1)
