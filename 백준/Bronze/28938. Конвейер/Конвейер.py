n = int(input())
sq = list(map(int, input().split()))
sum_sq = sum(sq)

if sum_sq > 0:
    print("Right")
elif sum_sq < 0:
    print("Left")
else:
    print("Stay")