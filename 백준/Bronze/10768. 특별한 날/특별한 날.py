M = int(input())
D = int(input())
result = ''

if M < 2:
    result = 'Before'
elif M > 2:
    result = 'After'
else:
    if D < 18:
        result = 'Before'
    elif D > 18:
        result = 'After'
    else:
        result = 'Special'

print(result)