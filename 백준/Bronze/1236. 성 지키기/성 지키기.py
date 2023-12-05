import sys
input = sys.stdin.readline

N, M = map(int, input().split())
castle = [input().rstrip() for _ in range(N)]
security_row = [i for i in range(N)]
security_column = [i for i in range(M)]

for i, row in enumerate(castle):
    for j, column in enumerate(row):
        if column == 'X':
            if i in security_row:
                security_row.remove(i)
            if j in security_column:
                security_column.remove(j)


print(max(len(security_row), len(security_column)))