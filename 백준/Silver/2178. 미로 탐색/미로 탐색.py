import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input()[:-1])) for _ in range(N)]


def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        if x - 1 >= 0 and maze[x - 1][y] == 1: # 상
            queue.append((x - 1, y))
            maze[x - 1][y] = maze[x][y] + 1
        if x + 1 < N and maze[x + 1][y] == 1: # 하
            queue.append((x + 1, y))
            maze[x + 1][y] = maze[x][y] + 1
        if y - 1 >= 0 and maze[x][y - 1] == 1: # 좌
            queue.append((x, y - 1))
            maze[x][y - 1] = maze[x][y] + 1
        if (y + 1) % M > 0 and maze[x][y + 1] == 1:  # 우
            queue.append((x, y + 1))
            maze[x][y + 1] = maze[x][y] + 1
        if x == 0 and y == 0:
            maze[x][y] = 0


bfs(0, 0)
print(maze[N - 1][M - 1])
