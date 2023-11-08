while True:
    word = input()
    if word == '0':
        break

    is_palindrome = 'yes'

    for i in range(len(word)// 2):
        if word[i] != word[-(i + 1)]:
            is_palindrome = 'no'
            break

    print(is_palindrome)
