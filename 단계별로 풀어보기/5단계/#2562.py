#2562 최댓값

num_list = []
for i in range(9):
    n = int(input())
    num_list.append(n)
print(max(num_list))
print(num_list.index(max(num_list))+1)
