# usr/bin/env python
# -*- coding: utf8 -*-
# 2023 소프트웨어마에스트로 1차 코딩테스트 4번 젓가락

# 4
# BC DB AA CD
# 정답: 4

# 4
# AA BD CC BD
# 정답: 3

# 2
# AB BA
# 정답: 1

# 2
# AA BB
# 정답: 0

import sys

input = sys.stdin.readline

n = int(input().rstrip())
chopsticks = list(input().split())
chopsticks = [list(x) for x in chopsticks]

def check(chopsticks, i, j):

    # 원소 구성이 완전히 다른 경우
    if chopsticks[i][0] not in chopsticks[j] and chopsticks[i][1] not in chopsticks[j]:
        print("a != chopsticks[j]")
        chopsticks[i]
        return 1, chopsticks # 바꾸기

    # 원소 구성이 하나만 다른 경우


    # 한 번 swap 하면 짝이 맞춰지는 경우
    a_swap = [chopsticks[i][1], chopsticks[i][0]]
    if a_swap == chopsticks[j]:
        print("swap a == b")
        return 1, chopsticks # 바꾸기

    print("a == b")
    return 0, chopsticks

answer = 0

while True:
    cnt = 0
    for i in range(n):
        if i == n - 1:
            res, chopsticks = check(chopsticks, i, 0)

        else:
            res, chopsticks = check(chopsticks, i, i + 1)
        cnt += res
    if cnt == 0:
        break
    answer += cnt

print(answer)