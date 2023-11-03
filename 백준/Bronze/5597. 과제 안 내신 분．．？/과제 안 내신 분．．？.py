import sys
input = sys.stdin.readline

students = [False] * (30 + 1)

for _ in range(28):
    student_number = int(input())
    students[student_number] = True

for i in range(1, 30 + 1):
    if not students[i]:
        print(i)
