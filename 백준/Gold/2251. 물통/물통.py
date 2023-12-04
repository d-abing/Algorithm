from collections import deque

buckets = list(map(int, input().split()))
visited = [[False] * 201 for i in range(201)]
answer = [False] * 201
queue = deque()

# 0 -> 1, 2 / 1 -> 0, 2 / 2 -> 0, 1
sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]

def bfs():
    queue.append((0, 0))
    visited[0][0] = True
    answer[buckets[2]] = True
    while queue:
        water = queue.popleft()
        A = water[0]
        B = water[1]
        C = buckets[2] - (A + B)
        for i in range(6): # 0 ~ 6
            next = [A, B, C]
            next[receiver[i]] += next[sender[i]]
            next[sender[i]] = 0
            if next[receiver[i]] > buckets[receiver[i]]:
                next[sender[i]] = next[receiver[i]]- buckets[receiver[i]]
                next[receiver[i]] = buckets[receiver[i]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0:
                    answer[next[2]] = True

bfs()

for i, a in enumerate(answer):
    if a:
        print(i, end=' ')
