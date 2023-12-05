import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [i for i in range(n + 1)]

def union(a, b):
    a = find(a)
    b = find(b)
    graph[a] = b

def find(num):
    if graph[num] != num:
        graph[num] = find(graph[num])
        return graph[num]
    else:
        return num

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)

    elif op == 1:
        a = find(a)
        b = find(b)
        if a == b:
            print("YES")
        else:
            print("NO")
