L = int(input())
S = int(input())

if L >= S:
    print("Congratulations, you are within the speed limit!")
else:
    F = 0
    if S - L in range(1, 21):
        F = 100
    elif S - L in range(21, 31):
        F = 270
    else:
        F = 500

    print("You are speeding and your fine is ${}.".format(F))