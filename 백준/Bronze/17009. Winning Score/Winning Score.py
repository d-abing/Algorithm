apples = [ int(input()) for _ in range(3) ]
bananas = [ int(input()) for _ in range(3) ]
apples_score = apples[0] * 3 + apples[1] * 2 + apples[2]
bananas_score = bananas[0] * 3 + bananas[1] * 2 + bananas[2]

if  apples_score > bananas_score:
    print("A")
elif apples_score < bananas_score:
    print("B")
else:
    print("T")