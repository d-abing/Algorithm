import sys
input = sys.stdin.readline


def convert_grade(str_grade):
    if str_grade == "A+":
        return 4.5
    elif str_grade == "A0":
        return 4.0
    elif str_grade == "B+":
        return 3.5
    elif str_grade == "B0":
        return 3.0
    elif str_grade == "C+":
        return 2.5
    elif str_grade == "C0":
        return 2.0
    elif str_grade == "D+":
        return 1.5
    elif str_grade == "D0":
        return 1.0
    elif str_grade == "F":
        return 0.0


credits = []
result = 0

for _ in range(20):
    credit, grade = (input().split())[1:]
    if grade != "P":
        result += float(credit) * convert_grade(grade)
        credits.append(float(credit))

print(result / sum(credits))
