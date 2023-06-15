# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 달리기 경주

from collections import defaultdict

def solution(players, callings):

    player_dict = {player : rank for rank, player in enumerate(players)}
    rank_dict = {rank : player for rank, player in enumerate(players)}

    for calling in callings:
        n = player_dict[calling]
        player_dict[calling] -= 1
        player_dict[rank_dict[n - 1]] += 1

        rank_dict[n - 1], rank_dict[n] = rank_dict[n], rank_dict[n - 1]

    return list(rank_dict.values())

# 시간초과 코드
def solution(player, callings):
    answer = []
    for calling in callings:
        n = player.index(calling)
        player[n], player[n - 1] = player[n - 1], player[n]
    return player