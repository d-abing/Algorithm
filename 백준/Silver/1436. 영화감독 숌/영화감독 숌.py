N = int(input())

count = 0
for i in range(666, 20000000):
    if str(i).find('666') > -1:
        count += 1
    if N == count:
        print(i)
        break
