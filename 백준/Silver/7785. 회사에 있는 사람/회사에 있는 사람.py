import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    log = input().split()
    dic[log[0]] = log[1]

name_list = []
for name in dic:
    if dic[name] == 'enter':
        name_list.append(name)

name_list.sort(reverse=True)
print(*name_list, sep='\n')