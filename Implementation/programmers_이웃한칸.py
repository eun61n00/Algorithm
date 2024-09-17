def solution(board, h, w):
    answer = 0
    ny = (-1, 1, 0, 0)
    nx = (0, 0, -1, 1)

    for i in range(4):
        dy, dx = h + ny[i], w + nx[i]
        if dy < 0 or dx < 0 or dy >= len(board) or dx >= len(board[0]):
            continue
        if board[dy][dx] == board[h][w]:
            answer += 1
    return answer
