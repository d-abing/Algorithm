import sys
input = sys.stdin.readline

expression = input()
replaced_expression = expression.replace('+', ' ').replace('-', ' ')
numbers = list(map(int, replaced_expression.split()))

index = 0

for e in expression:
    if e == '+':
        index += 1
    elif e == '-':
        index += 1
        break
    elif e == '\n':
        index += 1

result = sum(numbers[0:index]) - sum(numbers[index:])
print(result)
