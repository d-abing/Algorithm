vowels = ["a", "e", "i", "o", "u"]
word = input()
count = 0

for vowel in vowels:
    count += word.count(vowel)

print(count)