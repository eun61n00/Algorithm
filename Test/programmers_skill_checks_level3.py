def solution(key, lock):
    answer = True

    key_turn = [[0 for _ in range(len(key))] for _ in range(len(key))]

    # 현재 키가 맞는지 확인
    for i in range(len(lock)):
        for j in range(len(lock)):
            lock_copy = [[c for c in lock[r]] for r in range(len(lock))]
            for key_r in range(i, len(key)):
                for key_c in range(j, len(key)):
                    lock_copy[key_r][key_c] = lock_copy[key_r][key_c] or key[key_r][key_c]
            answer = True
            for row in lock_copy:
                if 0 in row:
                    answer = False
            if answer == True:
                return answer

    for _ in range(3):
        # 키 돌리기
        for i, i_row in enumerate(key):
            for j, val in enumerate(i_row):
                key[j][len(key) - i - 1] = val

        # 차례대로 대보면서 확인
        for i in range(len(lock)):
            for j in range(len(lock)):
                lock_copy = [[c for c in lock[r]] for r in range(len(lock))]
                for key_r in range(i, len(key)):
                    for key_c in range(j, len(key)):
                        lock_copy[key_r][key_c] = lock_copy[key_r][key_c] or key[key_r][key_c]
                answer = True
                for row in lock_copy:
                    if 0 in row:
                        answer = False
                if answer == True:
                    return answer

    return answer