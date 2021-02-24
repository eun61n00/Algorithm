s = input()
count = 0
while (s.find("c=") != -1):
    count += 1
    s = s.replace("c=", " ", 1)
while (s.find("c-") != -1):
    count += 1
    s = s.replace("c-", " ", 1)
while (s.find("dz=") != -1):
    count += 1
    s = s.replace("dz=", " ", 1)
while (s.find("d-") != -1):
    count += 1
    s = s.replace("d-", " ", 1)
while (s.find("lj") != -1):
    count += 1
    s = s.replace("lj", " ", 1)
while (s.find("nj") != -1):
    count += 1
    s = s.replace("nj", " ", 1)
while (s.find("s=") != -1):
    count += 1
    s = s.replace("s=", " ", 1)
while (s.find("z=") != -1):
    count += 1
    s = s.replace("z=", " ", 1)
s=s.replace(" ", '')
for i in s:
    count += 1
print(count)
