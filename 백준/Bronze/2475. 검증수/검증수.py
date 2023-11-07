numbers = list(map(int, input().split()))
sum = 0
for num in numbers:
    sum += num ** 2

print(sum % 10)
