# usr/bin/env python
# -*- coding: utf8 -*-
# 이것이 코딩 테스트다 Ch11 Q02 곱하기 혹은 더하기

num_list = list(input())
num_list = [int(x) for x in num_list]

result = num_list[0]
for idx, num in enumerate(num_list[1:]):
    num = int(num)
    if num_list[idx] == 0 or num_list[idx] == 1:
        result += num
    else:
        result *= num

print(result)
