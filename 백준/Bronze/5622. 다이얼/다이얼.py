S = input()
A = [[],[],['A','B','C'],['D','E','F'],['G','H','I'],\
     ['J','K','L'],['M','N','O'],['P','Q','R','S'],\
     ['T','U','V'],['W','X','Y','Z']]

numbers = []

for s in S:
    for i, a in enumerate(A):
        if s in a:
            numbers.append(i)

times = 0

for number in numbers:
    times += number + 1

print(times)
