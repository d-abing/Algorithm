s = input()
is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        is_palindrome = False

if is_palindrome:
    print(1)
else:
    print(0)
