from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
visited = [[False] * N for _ in range(N)]
A = [list(map(int, list(input()[:-1]))) for _ in range(N)]
answer = []

def BFS(x, y):
    count = 0
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    while queue:
        a, b = queue.popleft()
        count += 1
        if a - 1 >= 0 and A[a - 1][b] == 1 and not visited[a - 1][b]: #상
            queue.append((a - 1, b))
            visited[a - 1][b] = True
        if a + 1 < N and A[a + 1][b] == 1 and not visited[a + 1][b]: #하
            queue.append((a + 1, b))
            visited[a + 1][b] = True
        if b % N != 0 and A[a][b - 1] and not visited[a][b - 1]: #좌
            queue.append((a, b - 1))
            visited[a][b - 1] = True
        if (b + 1) % N != 0 and A[a][b + 1] and not visited[a][b + 1]: #우
            queue.append((a, b + 1))
            visited[a][b + 1] = True
    answer.append(count)

for i in range(N):
    for j in range(N):
        if A[i][j] == 1 and not visited[i][j]:
            BFS(i, j)

print(len(answer))
answer.sort()
print(*answer, sep='\n')
