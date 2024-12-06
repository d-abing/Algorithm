while True:
    try:
        name = str(input())
        answer = ""

        for i in range(len(name)):
            C = name[i]
            if C == "i":
                answer += "e"
            elif C == "e":
                answer += "i"
            elif C == "I":
                answer += "E"
            elif C == "E":
                answer += "I"
            else:
                answer += C

        print(answer)

    except:
        break