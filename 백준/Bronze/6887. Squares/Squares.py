T = int(input())
num = 0

for i in range(1, 100 + 1):
    if T >= i ** 2:
        num = i
    else:
        break

print("The largest square has side length {}.".format(num))