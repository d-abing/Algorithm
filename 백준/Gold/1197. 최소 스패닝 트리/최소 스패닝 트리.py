import sys

input = sys.stdin.readline

V, E = map(int, input().split())
union_find_list = [i for i in range(V + 1)]
graph = []

def union(a, b):
    a = find(a)
    b = find(b)
    union_find_list[a] = b

def find(num):
    if union_find_list[num] != num:
        union_find_list[num] = find(union_find_list[num])
        return union_find_list[num]
    else:
        return num

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

graph.sort()
result = 0

for c, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        result += c

print(result)