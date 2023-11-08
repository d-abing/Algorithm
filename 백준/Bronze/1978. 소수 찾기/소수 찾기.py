import math
N = input()
numbers = list(map(int, input().split()))
check = [True] * len(numbers)

max_num = max(numbers)

for i in range(2, int(math.sqrt(max_num)) + 1):
    for j in range(len(numbers)):
        if numbers[j] != i and numbers[j] % i == 0:
            check[j] = False

for j in range(len(numbers)):
    if numbers[j] == 1:
        check[j] = False

print(check.count(True))
