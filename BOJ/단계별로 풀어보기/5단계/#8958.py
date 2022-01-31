n = int(input())
score = 0
result = 0
for i in range(n):
    OXlist = input()
    for j in range(len(OXlist)):
        if OXlist[j] == "O":
            score += 1
            result += score
        else:
            score = 0
            continue
    print(result)
    score=0
    result=0
