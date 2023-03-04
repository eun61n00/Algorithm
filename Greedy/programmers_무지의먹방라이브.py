# usr/bin/env python
# -*- coding: utf8 -*-
# 2019 카카오 신입 공치 - 무지의 먹방 라이브

def solution_0(food_times, k):
    answer = 0

    n, m = k // len(food_times), k % len(food_times)

    food_times[0:n+1] = [x - (n + 1) for x in food_times[0:n+1]]
    food_times[n+1:] = [x - n for x in food_times[n+1:]]

    print(food_times)


    negatives = [(idx, x) for idx, x in enumerate(food_times) if x < 0]
    while negatives:
        i, t = negatives[0]
        food_times[i + 1: i - t + 1] = [x - 1 for x in food_times[i + 1 :i - t + 1]]
        food_times[i] = 0
        negatives = [(idx, x) for idx, x in enumerate(food_times) if x < 0]

    print(food_times)

# solution_0([3, 1, 2], 5)

food_times = [3, 1, 3]
cnt = 0
cnt = len(food_times) - food_times.count(0)
while cnt > 0:
    food_times_update = [x - 1 if x > 0 else x for x in food_times]    # 먹음(업데이트)
    cnt = len(food_times) - food_times_update.count(0)
    # if cnt <= 0:


print(food_times)