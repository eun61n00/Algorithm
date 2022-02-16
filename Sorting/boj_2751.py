#using quick sort
def q_sort(num_lst):
	if len(num_lst) <= 1:
		return (num_lst)
	left, right = list(), list()
	pivot = num_lst[0]

	for i in range(1, len(num_lst)):
		if pivot > num_lst[i]:
			left.append(num_lst[i])
		else:
			right.append(num_lst[i])
	return q_sort(left) + [pivot] + q_sort(right)

num_lst = []
for _ in range(int(input())):
	num_lst.append(int(input()))
num_lst = q_sort(num_lst)
[print (_) for _ in num_lst]


#using pypy compiler
num_lst = [int(input()) for i in range(int(input()))]
print('\n'.join(map(str, sorted(num_lst))))