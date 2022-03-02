# coding=utf-8
# <이것이 코딩 테스트다>(나동빈, 한빛미디어) 예제 4-1
from sys import stdin

n = int(stdin.readline())
plans = ['R', 'R', 'R', 'U', 'D', 'D']
# plan = list(map(int, input().split()))
loc_x = 1
loc_y = 1
dir_x = [0, 0, -1, 1]
dir_y = [-1, 1, 0, 0]

for plan in plans:
    if plan == 'L':
        loc_x += dir_x[0]
        loc_y += dir_y[0]
    elif plan == 'R':
        loc_x += dir_x[1]
        loc_y += dir_y[1]
    elif plan == 'U':
        loc_x += dir_x[2]
        loc_y += dir_y[2]
    else:
        loc_x += dir_x[3]
        loc_y += dir_y[3]