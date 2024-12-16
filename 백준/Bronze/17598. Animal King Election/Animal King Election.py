votes = [input() for _ in range(9)]

if votes.count("Tiger") >= 5:
    print("Tiger")
else:
    print("Lion")