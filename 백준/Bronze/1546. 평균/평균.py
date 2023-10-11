N = int(input())
scores = list(map(int, input().split()))
max = max(scores)
sum = 0

for i in scores :
    sum += i / max * 100

average = sum / N

print(average)