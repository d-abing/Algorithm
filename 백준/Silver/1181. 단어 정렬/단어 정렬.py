N = int(input())
words = []
for _ in range(N):
    word = input()
    if (len(word), word) not in words:
        words.append((len(word), word))

words.sort()

for word in words:
    print(word[1])
