t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())

result1 = t1 * 3 + e1 * 20 + f1 * 120
result2 = t2 * 3 + e2 * 20 + f2 * 120

if result1 > result2:
    print("Max")
elif result1 < result2:
    print("Mel")
else:
    print("Draw")