import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
dic = dict()
for a in A:
    if str(a) in dic:
        dic[str(a)] += 1
    else:
        dic[str(a)] = 1

sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1]))
keys = list(sorted_dic.keys())
values = list(sorted_dic.values())

max_start = 0
for i, value in enumerate(values):
    max_start = i if value > values[max_start] else max_start

if max_start != len(values) - 1:
    max_start += 1

print(round(sum(A) / N))
print(A[N // 2])
print(keys[max_start])
print(A[-1] - A[0])