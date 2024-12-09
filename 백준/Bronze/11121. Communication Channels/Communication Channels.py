T = int(input())

for _ in range(T):
    i, o = input().split()

    if i == o:
        print("OK")
    else:
        print("ERROR")