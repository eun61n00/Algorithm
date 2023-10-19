# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14890 경사로

n, l = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
for i in range(n):
    road = board[i]
    cnt, possible = 0, True
    while cnt < n and possible:
        # 경사로를 놓을 수 있는지 확인
        if cnt + l < n and road[cnt + 1: cnt + l] == [min(road[cnt], road[cnt + l])] * (l - cnt - 1):
            print("1", cnt, road[cnt + 1: cnt + l],
                  [min(road[cnt], road[cnt + l])] * (l - cnt - 1))
            cnt += l

        elif road[cnt + 1: cnt + l + 1] == [road[cnt]] * (cnt + l):

            print("2", cnt, road[cnt + 1: cnt + l + 1],
                  [road[cnt]] * (cnt + l))
            cnt += l

        else:
            possible = False

    if possible == True:
        print(i)
        answer += 1


print(answer)
