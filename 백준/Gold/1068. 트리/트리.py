import sys
input = sys.stdin.readline

N = int(input())
p_nodes = list(map(int, input().split()))
root_node = 0

graph = [[] for _ in range(N)]
for i, p in enumerate(p_nodes):
    if p != -1:
        graph[p].append(i)
    else:
        root_node = i

result = []
for i, c_nodes in enumerate(graph):
    if not c_nodes:
        result.append(i)

visited = [False] * N

def dfs(v):
    visited[v] = True
    if v in result:
        result.remove(v)
        if len(graph[p_nodes[v]]) == 1:
            result.append(p_nodes[v])
    for num in graph[v]:
        if not visited[num]:
            dfs(num)


e_node = int(input())
if e_node == root_node:
    print(0)
else:
    dfs(e_node)
    print(len(result))
