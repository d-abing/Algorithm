import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


has_five_friends = False


def dfs(v, depth):
    global has_five_friends
    if depth == 5:
        has_five_friends = True
        return
    visited[v] = True
    for num in graph[v]:
        if not visited[num]:
            dfs(num, depth + 1)
    visited[v] = False


for i in range(N):
    dfs(i, 1)
    if has_five_friends:
        break

if has_five_friends:
    print(1)
else:
    print(0)
