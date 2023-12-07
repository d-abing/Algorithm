import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
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

for i in range(N):
    link = list(map(int, input().split()))
    for j, islinked in enumerate(link):
        if islinked == 1:
            union(i + 1, j + 1)

plan_counties = list(map(int, input().split()))
for country in plan_counties:
    find(country)

main_country = 0
can_travel = True
for country in plan_counties:
    if main_country == 0:
        main_country = graph[country]
    elif main_country != graph[country]:
        can_travel = False

if can_travel:
    print("YES")
else:
    print("NO")