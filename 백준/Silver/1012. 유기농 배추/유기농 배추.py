import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    checkindex = []
    group = 0

    stack = []

    for n in range(N):
        for m in range(M):
            if [n, m] not in checkindex and ground[n][m] == 1:
                stack.append((n, m))
                while stack:
                    x_index, y_index = stack.pop()
                    checkindex.append([x_index, y_index])
                    if x_index - 1 >= 0 and ground[x_index - 1][y_index] == 1 and [x_index - 1, y_index] not in checkindex:
                        stack.append((x_index - 1, y_index)) # 상
                    if x_index + 1 < N and ground[x_index + 1][y_index] == 1 and [x_index + 1, y_index] not in checkindex:
                        stack.append((x_index + 1, y_index)) # 하
                    if y_index % M != 0 and ground[x_index][y_index - 1] == 1 and [x_index, y_index - 1] not in checkindex:
                        stack.append((x_index, y_index - 1)) # 좌
                    if (y_index + 1) % M != 0 and ground[x_index][y_index + 1] == 1 and [x_index, y_index + 1] not in checkindex:
                        stack.append((x_index, y_index + 1)) # 우


                group += 1

    print(group)
