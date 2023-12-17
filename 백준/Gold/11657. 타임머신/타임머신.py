import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
D = [sys.maxsize] * (N + 1)
D[1] = 0

for _ in range(M):
    s, e, w = map(int, input().split())
    graph.append((s, e, w))

for _ in range(N - 1):
    for s, e, w in graph:
        if D[s] != sys.maxsize and D[e] > D[s] + w:
            D[e] = D[s] + w


negative = False

for s, e, w in graph:
    if D[s] != sys.maxsize and D[e] > D[s] + w:
        negative = True

if not negative:
    for d in D[2:]:
        if d != sys.maxsize:
            print(d)
        else:
            print(-1)
else:
    print(-1)
