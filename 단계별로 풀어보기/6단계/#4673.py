#4673 셀프 넘버

def d(n):
    result = n
    n = str(n)
    for i in range(len(n)):
        result += int(n[i])
    return result
  
d_list = []
for i in range(10000):
    d_list.append(d(i+1))
d_list = set(d_list)

list10000 = []
for i in range(10000):
    list10000.append(i+1)
list10000.sort()
list10000 = set(list10000)

list = list10000-d_list
list = sorted(list)

for i in range(len(list)):
    print(list[i])
