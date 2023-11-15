import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

count = -1


def dfs(v):
    global count
    if not visited[v]:
        visited[v] = True
        count += 1
        for computer in graph[v]:
            dfs(computer)


dfs(1)
print(count)
