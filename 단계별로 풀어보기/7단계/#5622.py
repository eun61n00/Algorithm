alphabet = input()
list = []
time = []
for i in alphabet:
    list.append(ord(i))
for i in range(len(list)):
    if list[i] <= 67:
        time.append(3)
    elif list[i] <= 70:
        time.append(4)
    elif list[i] <=73:
        time.append(5)
    elif list[i] <= 76:
        time.append(6)
    elif list[i] <= 79:
        time.append(7)
    elif list[i] <= 83:
        time.append(8)
    elif list[i] <= 86:
        time.append(9)
    else:
        time.append(10)
result = sum(time)
print(result)
