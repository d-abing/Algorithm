import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pocketmon = [input()[:-1] for _ in range(N)]

for _ in range(M):
    question = input()[:-1]
    if question.isalpha():
        print(pocketmon.index(question) + 1)
    else:
        print(pocketmon[int(question) - 1])
