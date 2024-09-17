# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers N으로 표현

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers N으로 표현

def solution(N, number):
    answer = 0

    dp = [[int(i * str(N))] for i in range(1, 9)]

    for i in range(1, 8):
        for val in dp[i - 1]:

            if abs(number) in dp[i - 1]:
                return i

            if abs(number) in [abs(val + N), abs(val - N), abs(val * N), abs(val // N)]:
                return i + 1

            dp[i].append(val + N)
            dp[i].append(val - N)
            dp[i].append(val * N)
            dp[i].append(val // N)

    for val in dp[7]:
        if abs(val) == abs(number):
            return 8

    return -1

solution(5, 12)
solution(5, 31168)
solution(5, 5)
print(solution(2, 11))