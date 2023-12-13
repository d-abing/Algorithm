n = int(input())
S = input().rstrip()
vowels = ["a", "e", "i", "o", "u"]

count = 0
for s in S:
    if s in vowels:
        count += 1
print(count)