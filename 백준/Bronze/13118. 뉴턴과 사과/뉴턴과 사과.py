people = list(map(int, input().split()))
apple = list(map(int, input().split()))

answer = 0

for i, person in enumerate(people):
    if person == apple[0]:
        answer = i + 1

print(answer)