M = int(input())
stones = list(map(int, input().split()))
K = int(input())

combination = 0

for number in stones:
    result = 1

    for i in range(K):
        result *= (number - i)

    for i in range(K):
        result //= (K - i)

    combination += result

total_combination = 1

for i in range(K):
    total_combination *= (sum(stones) - i)

for i in range(K):
    total_combination //= (K - i)

print(combination / total_combination)
