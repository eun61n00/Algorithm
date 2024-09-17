# !usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1027 고층건물

import sys
INF = sys.maxsize
n = int(input())
buildings = list(map(int, input().split()))

def calc_gradient(x1, y1, x2, y2):
    if x1 == x2:
        return 0
    gradient = (y2 - y1) / (x2 - x1)
    return gradient

results = []
for idx in range(len(buildings)):
    cnt = 0

    # 왼쪽 건물들
    min_gradient = INF # 앞에서 가장 작았던 것보다 기울기 크면 안보임
    for i in range(idx - 1, -1, -1):
        gradient = calc_gradient(i, buildings[i], idx, buildings[idx])
        if gradient < min_gradient:
            cnt += 1
            min_gradient = gradient

    # 오른쪽 건물들
    max_gradient = -INF # 앞에서 기울기가 가장 컸던 것보다 작으면 안보임
    for i in range(idx + 1, len(buildings)):
        gradient = calc_gradient(i, buildings[i], idx, buildings[idx])
        if gradient > max_gradient:
            cnt += 1
            max_gradient = gradient

    results.append(cnt)

print(max(results))