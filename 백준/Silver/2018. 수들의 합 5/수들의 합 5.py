from sys import stdin
input = stdin.readline

N = int(input())
sum = 0
i = 1
j = 1
count = 1

while j <= (N // 2):
    if sum <= N:
        if sum == N:
            count += 1
        sum += i
        i += 1
    elif sum > N:
        sum -= j
        j += 1

print(count)