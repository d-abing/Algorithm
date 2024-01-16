AB = input().strip()
A = B = 0

for num in AB:
    number = int(num)
    if A == 0:
        A = number
    elif B == 0:
        if number != 0:
            B = number
        else:
            A *= 10
    else:
        if number == 0:
            B *= 10

print(A + B)
