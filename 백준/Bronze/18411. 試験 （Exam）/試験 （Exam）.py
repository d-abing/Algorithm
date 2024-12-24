scores = list(map(int, input().split()))
scores.sort()
print(sum(scores[1:3]))