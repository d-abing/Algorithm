scores = input()
who = ""
score_dic = {
    "A" : [],
    "B" : []
}

for s in scores:
    if s.isalpha():
        who = s
    else:
        score_dic[who].append(int(s))

a_sum = sum(score_dic["A"])
b_sum = sum(score_dic["B"])

if a_sum > b_sum:
    print("A")
else:
    print("B")