import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatoes = [[[] for _ in range(M)] for _ in range(N)]
visited = [[[False] * H for _ in range(M)] for _ in range(N)]
all_complete = 0
queue = deque()
queue.append([])
result = 0

for h in range(H):
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            tomatoes[i][j].append(line[j])
            if line[j] == 1:
                all_complete += 1
                visited[i][j][h] = True
                queue[0].append((i, j, h))
            elif line[j] == -1:
                all_complete += 1

if all_complete != M * N * H:
    def bfs():
        global result
        while queue:
            one_day_tomatoes = []
            for tomato in queue.popleft():
                a, b, c = tomato  # a 행 , b 열, c 층
                # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
                if a > 0 and not visited[a - 1][b][c] and tomatoes[a - 1][b][c] == 0:
                    tomatoes[a - 1][b][c] = 1
                    visited[a - 1][b][c] = True
                    one_day_tomatoes.append((a - 1 , b, c))
                if a + 1 < N and not visited[a + 1][b][c] and tomatoes[a + 1][b][c] == 0:
                    tomatoes[a + 1][b][c] = 1
                    visited[a + 1][b][c] = True
                    one_day_tomatoes.append((a + 1, b, c))
                if b > 0  and not visited[a][b - 1][c] and tomatoes[a][b - 1][c] == 0:
                    tomatoes[a][b - 1][c] = 1
                    visited[a][b - 1][c] = True
                    one_day_tomatoes.append((a, b - 1, c))
                if b + 1 < M and not visited[a][b + 1][c] and tomatoes[a][b + 1][c] == 0:
                    tomatoes[a][b + 1][c] = 1
                    visited[a][b + 1][c] = True
                    one_day_tomatoes.append((a, b + 1, c))
                if c > 0 and not visited[a][b][c - 1] and tomatoes[a][b][c - 1] == 0:
                    tomatoes[a][b][c - 1] = 1
                    visited[a][b][c - 1] = True
                    one_day_tomatoes.append((a, b, c - 1))
                if c + 1 < H and not visited[a][b][c + 1] and tomatoes[a][b][c + 1] == 0:
                    tomatoes[a][b][c + 1] = 1
                    visited[a][b][c + 1] = True
                    one_day_tomatoes.append((a, b, c + 1))
            if one_day_tomatoes:
                queue.append(one_day_tomatoes)
                result += 1

    bfs()

    for line in tomatoes:
        for layer in line:
            for tomato in layer:
                if tomato == 0:
                    result = -1
                    break

print(result)
