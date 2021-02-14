#1101 더하기 사이클

n = input()
count = 1
new = {}
if len(n) == 1:
    n = "0" + n
new[count] = str(int(n[0]) + int(n[1]))
count += 1
print(new)
print(new[count-1][0])
while (n!=new[count-1]):
    new[count] = int(new[count-1][0]) + int(new[count-1][0])
    count += 1
    print(new)
print(count)
