#10871 X보다 작은 수

n, x = map(int, input().split())

input_list = list(map(int, input().split()))
print_list = []
for number in input_list:
    if number < x:
        print_list.append(number)
for i in print_list:
    print(i,end = ' ')
