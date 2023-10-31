import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

for i in range(1, N):
    for j in range(i):
        if P[i] < P[j]:
            P.insert(j, P.pop(i))
            break

prefix_sum = [0]

for i in range(N):
    prefix_sum.append(prefix_sum[i] + P[i])

result = sum(prefix_sum)

print(result)
