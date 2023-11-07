T = int(input())
for _ in range(T):
    scores = input().split('X')
    total_score = 0
    for score in scores:
        for i in range(1, len(score) + 1):
            total_score += i
    print(total_score)
