# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 18808 스티커붙이기

def rotate(sticker):
    # 스티커를 시계방향으로 90도 회전하여 리턴해주는 함수
    rotated = [list(row) for row in zip(*sticker[::-1])]
    return rotated


n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]
stickers = []

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)


for i in range(len(stickers)):
    sticker = stickers[i]
    rotate_num = 0

    found = False
    while not found:  # 찾을때까지 반복
        r, c = len(sticker), len(sticker[0])
        # 차례대로 비교해보면서 붙여보기
        # 붙일 수 있으면 바로 break
        for x in range(0, n - r + 1):
            for y in range(0, m - c + 1):
                notebook_portion = [notebook[x + _][y: y + c]
                                    for _ in range(r)]  # 스티커 부분만큼 노트북도 떼어냄
                # 둘이 비교
                result = [[a + b for a, b in zip(row1, row2)]
                          for row1, row2 in zip(sticker,  notebook_portion)]
                found = not any(2 in row for row in result)
                if found:
                    # notebook에 result를 붙여넣기
                    for X in range(x, x + r):
                        notebook[X][y: y + c] = result[X - x]
                    break
            if found:
                break
        if found:
            break

        # 방향 전환
        # stickers 자체를 갱신
        rotate_num += 1
        if rotate_num == 4:
            break  # 스티커 버리기
        sticker = rotate(sticker)

answer = 0
for i in range(n):
    for j in range(m):
        if notebook[i][j] == 1:
            answer += 1

print(answer)
