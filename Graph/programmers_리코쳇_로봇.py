from collections import deque


def bfs(x, y, visited, board):

    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        # 위로 이동
        nx, ny = x, y
        while nx > 0 and board[nx - 1][ny] != "D":
            nx -= 1
        if board[nx][ny] == "G":
            return board[x][y]
        if not visited[nx][ny]:
            board[nx][ny] = board[x][y] + 1
            queue.append((nx, ny))
            visited[nx][ny] = True

        # 아래로 이동
        nx, ny = x, y
        while nx < len(board) - 1 and board[nx + 1][ny] != "D":
            nx += 1
        if board[nx][ny] == "G":
            return board[x][y]
        if not visited[nx][ny]:
            board[nx][ny] = board[x][y] + 1
            queue.append((nx, ny))
            visited[nx][ny] = True

        # 왼쪽으로 이동
        nx, ny = x, y
        while ny > 0 and board[nx][ny - 1] != "D":
            ny -= 1
        if board[nx][ny] == "G":
            return board[x][y]
        if not visited[nx][ny]:
            board[nx][ny] = board[x][y] + 1
            queue.append((nx, ny))
            visited[nx][ny] = True

        # 오른쪽으로 이동
        nx, ny = x, y
        while ny < len(board[0]) - 1 and board[nx][ny + 1] != "D":
            ny += 1
        if board[nx][ny] == "G":
            return board[x][y]
        if not visited[nx][ny]:
            board[nx][ny] = board[x][y] + 1
            queue.append((nx, ny))
            visited[nx][ny] = True


def solution(board):
    answer = 0
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        board[i] = list(board[i])
        if "R" in board[i]:
            j = board[i].index("R")
            board[i][j] = 0
            start = (i, j)

    answer = bfs(start[0], start[1], visited, board)
    if answer:
        return answer
    else:
        return -1
