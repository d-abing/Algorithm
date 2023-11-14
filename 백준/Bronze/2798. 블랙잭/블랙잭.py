N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards_sum = 0
for _ in range(N):
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                cards_sum = cards[i] + cards[j] + cards[k] \
                    if M - cards_sum > M - (cards[i] + cards[j] + cards[k]) and M >= (cards[i] + cards[j] + cards[k]) \
                    else cards_sum

print(cards_sum)