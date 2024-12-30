w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

answer = (h1 + h2) * 2 + (w1 + w2) + 4 + abs(w1 - w2)
print(answer)