number = [int(input()) for _ in range(4)]
isTMN = False

if number[0] == 8 or number[0] == 9:
    if number[3] == 8 or number[3] == 9:
        if number[1] == number[2]:
            isTMN = True


if isTMN:
    print("ignore")
else:
    print("answer")