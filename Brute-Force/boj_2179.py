# usr/bin/env python
# -*- coding: utf8 -*-
# boj 2179 비슷한 단어

import sys

input = sys.stdin.readline
n = int(input().rstrip())
words = [(input().rstrip(), i) for i in range(n)]
words_sorted = sorted(words)

max_prefix = 0
answer = [(None, 20001), (None, 20001)]
for i in range(len(words_sorted) - 1):
    cnt = 0
    word1 = list(words_sorted[i][0])
    word2 = list(words_sorted[i + 1][0])

    if word1 == word2:
        continue

    while word1 and word2 and word1.pop(0) == word2.pop(0):
        cnt += 1

    # 처음부터 돌면서 비교하고 같은 때는 싸그리 무시하자 -> 니가 이미 순서를 다 섞여놨다 멍충아 (처음에 순서 섞을 때 인덱스 같이 저장해야 함)
    if cnt == max_prefix:
        word1_idx, word2_idx = min(words_sorted[i][1], words_sorted[i + 1][1]), max(words_sorted[i][1], words_sorted[i + 1][1])
        word1 = words[word1_idx][0]
        word2 = words[word2_idx][0]

        # 입력 받은 순서대로 출력
        cur_word1_idx, cur_word2_idx = answer[0][1], answer[1][1]

        if word1_idx < cur_word1_idx:
            answer[0] = word1, word1_idx
            answer[1] = word2, word2_idx

        elif word1_idx == cur_word1_idx:
            if word2_idx < cur_word2_idx:
                answer[1] = (word2, word2_idx)

    elif cnt > max_prefix:
        max_prefix = cnt
        word1_idx, word2_idx = min(words_sorted[i][1], words_sorted[i + 1][1]), max(words_sorted[i][1], words_sorted[i + 1][1])
        word1 = words[word1_idx][0]
        word2 = words[word2_idx][0]
        answer[0] = word1, word1_idx
        answer[1] = word2, word2_idx

print(answer[0][0])
print(answer[1][0])
