quiz = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

scoreboard = [[8, 10], [1, 3, 9, 10], [1, 3, 9, 10], [3, 8, 9, 10], [1, 3, 8, 9, 10],
              [1, 3, 8, 9, 10], [1, 3, 8, 9, 10], [1, 3, 8, 9, 10], [1, 3, 8, 9, 10],
              [3, 4, 8, 9, 10]]

N = int(input()) - 1
answer = []

for i in range(12 + 1):
    if i not in scoreboard[N]:
        answer += quiz[i]

print(13 - len(scoreboard[N]))
print(" ".join(answer))
