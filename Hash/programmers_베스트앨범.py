# -*- coding: utf-8 -*-
# 프로그래머스 베스트앨범

def solution(genres, plays):

    res = []

    streaming_dict = {genre: [] for genre in genres}
    total_plays = []

    for i, genre in enumerate(genres):
        streaming_dict[genre].append([plays[i], i])
        streaming_dict[genre].sort(key = lambda x: (-x[0], x[1]))

    for genre in streaming_dict.keys():
        total_plays.append(
            [sum(cnt[0] for cnt in streaming_dict[genre]),
            genre])
    total_plays.sort(reverse = True)

    for genre in [total_play[1] for total_play in total_plays]:
        res.append(streaming_dict[genre][0][1])
        if len(streaming_dict[genre]) > 1:
            res.append(streaming_dict[genre][1][1])

    return res