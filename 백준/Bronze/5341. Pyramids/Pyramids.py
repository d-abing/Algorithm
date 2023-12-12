while(True):
    floor = int(input())
    if floor == 0:
        break
        
    sum = 0
    for i in range(1, floor + 1):
        sum += i
    print(sum)