import sys
input = sys.stdin.readline

N, M = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]
graph = [i for i in range(N + 1)]

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

parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)
    for i in range(1, len(party)):
        union(party[0], party[i])

count = 0
for party in parties:
    can_lie = True
    for man in know_truth:
        if find(party[0]) == find(man):
            can_lie = False
            break
    if can_lie:
        count += 1

print(count)