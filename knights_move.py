with open("input.txt', "r") as file:
    N, M = list(map(int, file.read().split()))
    if N == M == 1:
        print(1)
    else:
        board = [[0 for _ in range(M)] for _ in range(N)]
        if N >= 3 and M >= 2:
            board[2][1] = 1
        if M >= 3 and N >= 2:
            board[1][2] = 1
        if N >= 3 and M >= 3:
            for i in range(2, N):
                for j in range(2, M):
                    board[i][j] = board[i - 1][j - 2] + board[i - 2][j - 1]
        print(board[-1][-1])
