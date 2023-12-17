import sys
input = sys.stdin.readline

N, s_city, e_city, M = map(int, input().split())
graph = []
C = [-sys.maxsize] * N

for _ in range(M):
    s, e, w = map(int, input().split())
    graph.append((s, e, w))

earned_money = list(map(int, input().split()))
C[s_city] = earned_money[s_city]

for i in range(N + 51):
    for s, e, w in graph:
        if C[s] == -sys.maxsize :
            continue
        elif C[e] < C[s] - w + earned_money[e]:
            C[e] = C[s] - w + earned_money[e]
            if i >= N - 1:
                C[e] = sys.maxsize

if C[e_city] == -sys.maxsize:
    print("gg")
elif C[e_city] == sys.maxsize:
    print("Gee")
else:
    print(C[e_city])