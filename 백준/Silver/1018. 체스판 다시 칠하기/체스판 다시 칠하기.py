import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chessboard = [input()[:-1] for _ in range(N)]
result = []

for m in range(2):
    if m == 0:
        color = 'W'
    else:
        color = 'B'
    for i in range(N - 8 + 1):
        for j in range(M - 8 + 1):
            count = 0
            for k in chessboard[i:i + 8]:
                for l in k[j:j + 8]:
                    if l != color:
                        count += 1
                    if color == 'W':
                        color = 'B'
                    else:
                        color = 'W'
                if color == 'W':
                    color = 'B'
                else:
                    color = 'W'
            result.append(count)

print(min(result))
