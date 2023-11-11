X = int(input())
i = 1
sum = 1
a = 0
b = 0

while X > sum:
    i += 1
    sum += i

sum - X
if i % 2 == 0:
    a = i - (sum - X)
    b = 1 + (sum - X)
else:
    a = 1 + (sum - X)
    b = i - (sum - X)

print(str(a) + '/' + str(b))
