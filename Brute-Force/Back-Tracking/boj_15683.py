# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15683 감시

from collections import defaultdict
from copy import deepcopy

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if office[i][j] in [1, 2, 3, 4, 5]:
            cctv.append((office[i][j], i, j))

# 북 - 동 - 남 - 서
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
options = [
    [],
    [[0], [1], [2], [3]],
    [(0, 2), (1, 3)],
    [(0, 1), (1, 2), (2, 3), (3, 0)],
    [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    [(0, 1, 2, 3)]
]


# office 만들기
def monitor(direction, y, x, office):  # direction: (0, 2)
    for d in direction:
        ny, nx = y, x
        while True:
            ny += dy[d]  # 해당 방향(d)대로 한칸씩 이동
            nx += dx[d]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:  # 범위 넘어가면 중단
                break
            elif office[ny][nx] == 6:  # 벽이면 중단
                break
            # elif office[ny]
            elif office[ny][nx] == 0:
                office[ny][nx] = '#'


def dfs(depth, office):
    global answer
    if depth == len(cctv):  # 모든 cctv 방향 설정 완료
        answer = min(
            answer, len([(i, j) for j in range(m)
                        for i in range(n) if office[i][j] == 0])
        )
        return

    tmp = deepcopy(office)  # 사무실 복제
    num, y, x = cctv[depth]
    for direction in options[num]:
        monitor(direction, y, x, tmp)  # 여기서 사무실 정보가 바뀜
        dfs(depth + 1, tmp)  # 바뀐 사무실 정보로 다음 cctv 탐색 들어감
        tmp = deepcopy(office)  # 바꾼 사무실 정보를 원래대로


answer = int(1e9)
dfs(0, office)
print(answer)
