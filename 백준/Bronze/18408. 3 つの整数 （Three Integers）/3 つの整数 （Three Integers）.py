list = list(map(int, input().split()))
answer = 1 if list.count(1) > list.count(2) else 2
print(answer)