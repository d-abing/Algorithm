from sys import stdin
input = stdin.readline

N = int(input())

filenames = []

for _ in range(N):
    filenames.append(input())

indexsofquestionmark = []
samplefilename = filenames[0]

for i in range(len(samplefilename)):
    letter = ""
    issame = True
    for j in range(N):
        if letter == "":
            letter = filenames[j][i]
        elif letter != filenames[j][i]:
            issame = False
    if not issame:
        indexsofquestionmark.append(i)

result = ""

for i in range(len(samplefilename)):
    if i in indexsofquestionmark:
        result += "?"
    else:
        result += samplefilename[i]

print(result)
