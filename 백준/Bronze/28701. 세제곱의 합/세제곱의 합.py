N = int(input())
list = [i for i in range(1, N + 1)]
list2 = [i ** 3 for i in range(1, N + 1)]

result1 = sum(list)
result2 = result1 ** 2
result3 = sum(list2)

print(result1)
print(result2)
print(result3)