import sys
input = sys.stdin.readline

TC = int(input())

def bellman_ford(N, M, W, graph):
    D = [sys.maxsize] * (N + 1)

    for _ in range(M + W - 1):
        for S, E, T in graph:
            if D[E] > D[S] + T:
                D[E] = D[S] + T

    for S, E, T in graph:
        if D[E] > D[S] + T:
            return True

for _ in range(TC):
    N, M, W = map(int, input().split())

    graph = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph.append((S, E, T))
        graph.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph.append((S, E, -T))

    negative_cycle = bellman_ford(N, M, W, graph)

    if negative_cycle:
        print("YES")
    else:
        print("NO")