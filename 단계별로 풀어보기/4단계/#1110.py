#1101 더하기 사이클

n = input()
count = 0
new_num = []
if len(n) == 1:
    n = "0" + n
new_num.append(str(int(n[0]) + int(n[1])))

while n != new_num[-1]:
    if len(new_num[-1]) == 1:
        new_num[-1] = "0" + new_num[-1]
    if count == 0:
        new_num.append(str(int(n[1]) + int(new_num[-1][1])))
    else:
        new_num.append(str(int(new_num[-2][1]) + int(new_num[-1][1])))
    count += 1
print(count)
