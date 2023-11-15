import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dms = set([input()[:-1] for _ in range(N)])
bms = set([input()[:-1] for _ in range(M)])

dbj = dms.intersection(bms)
list_dbj = list(dbj)
list_dbj.sort()
print(len(list_dbj))
print(*list_dbj, sep='\n')