A = int(input())
B = int(input())

if A + B > 12:
    if (A + B) % 12 == 0:
        print(12)
    else:
        print((A + B) % 12)
else:
    print(A + B)