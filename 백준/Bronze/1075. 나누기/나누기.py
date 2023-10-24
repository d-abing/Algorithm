import sys
input = sys.stdin.readline

N = int(input()) // 100 * 100
F = int(input())

needed_num = F - (N % F) if F - (N % F) != F else 0
last_two_num = N % 100

result = str(last_two_num + needed_num)
result = result if len(result) > 1 else "0" + result

print(result)
