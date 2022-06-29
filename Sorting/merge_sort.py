def merge(left, right):
	merged = list()
	left_idx, right_idx = 0, 0

	# case1 - left/right 둘 다 있을 때
	while len(left) > left_idx and len(right) > right_idx:
		if left[left_idx] > right[right_idx]:
			merged.append(right[right_idx])
			right_idx += 1
		else:
			merged.append(left[left_idx])
			left_idx += 1

	# case2 - right에 남아있는 데이터가 없을 때
	while len(left) > left_idx:
		merged.append(left[left_idx])
		left_idx += 1

	# case3 - left에 남아있는 데이터가 없을 때
	while len(right) > right_idx:
		merged.append(right[right_idx])
		right_idx += 1

	return merged


def mergesplit(data):
	if len(data) <= 1:
		return data

	mid = len(data) // 2
	left = mergesplit(data[:mid])
	right = mergesplit(data[mid:])

	return merge(left, right)

if __name__ == '__main__':
	print(mergesplit([9, 4, 1, 2, 6, 7, 100]))