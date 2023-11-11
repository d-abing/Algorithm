import math
M = int(input())
N = int(input())
M = M + 1 if M == 1 else M
numbers = [i for i in range(M, N + 1)]

for i in range(2, int(math.sqrt(N)) + 1):
    count = N // i
    for j in range(2, count + 1):
        if i * j in numbers:
            numbers[numbers.index(i * j)] = 0

result = -1
if sum(numbers) != 0:
    print(sum(numbers))
    for number in numbers:
        if number != 0:
            result = number
            break

print(result)
