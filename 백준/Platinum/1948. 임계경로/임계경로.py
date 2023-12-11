import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
D = [0] * (n + 1)
D[0] = -1

for _ in range(m):
    a, b, time = map(int, input().split())
    graph[a].append((b, time))
    reverse_graph[b].append((a, time))
    D[b] += 1

queue = deque()
start, end = map(int, input().split())
queue.append(start)

result = [0] * (n + 1)
while queue:
    out = queue.popleft()
    for pair in graph[out]:
        D[pair[0]] -= 1
        if result[pair[0]] > result[out] + pair[1]:
            result[pair[0]] = result[pair[0]]
        else:
            result[pair[0]] = result[out] + pair[1]
        if D[pair[0]] == 0:
            queue.append(pair[0])


road_count = 0
visited = [False] * (n + 1)
queue.clear()
queue.append(end)
visited[end] = True

while queue:
    out = queue.popleft()
    for pair in reverse_graph[out]:
        if result[pair[0]] + pair[1] == result[out]:
            road_count += 1
            if not visited[pair[0]]:
                visited[pair[0]] = True
                queue.append(pair[0])

print(result[end])
print(road_count)
