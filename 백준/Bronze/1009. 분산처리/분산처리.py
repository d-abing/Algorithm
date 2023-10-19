from sys import stdin
input = stdin.readline

T = int(input())

result = ""

for i in range(T):
    a, b = input().split()
    last_a = a[-1]
    order = int(b) % 4 if int(b) % 4 != 0 else 4
    count = int(last_a) ** order
    result += (str(count)[-1] if str(count)[-1] != "0" else "10") + "\n"

print(result)
