c = int(input())
sum = 0
avg = 0
result = 0

for i in range(c):
    num_list = list(map(int, input().split()))
    student = num_list[0]
    del num_list[0]
    for j in range(student):
        sum += num_list[j]
        avg = sum/student
        isBiggerThanAvg = [x for x in num_list if x>avg]
        result = (len(isBiggerThanAvg)/len(num_list))*100
    print(format(result, ".3f"),"%", sep='')
    sum = 0
    avg = 0
    result = 0
