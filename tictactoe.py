import curses

def draw_board(stdscr, board):
    stdscr.clear()
    stdscr.addstr(0, 0, "Tic-Tac-Toe")
    stdscr.addstr(2, 0, " {} | {} | {} ".format(board[0], board[1], board[2]))
    stdscr.addstr(3, 0, "---+---+---")
    stdscr.addstr(4, 0, " {} | {} | {} ".format(board[3], board[4], board[5]))
    stdscr.addstr(5, 0, "---+---+---")
    stdscr.addstr(6, 0, " {} | {} | {} ".format(board[6], board[7], board[8]))
    stdscr.refresh()

def get_move(stdscr):
    while True:
        stdscr.addstr(8, 0, "Enter your move (1-9): ")
        stdscr.refresh()
        try:
            key = stdscr.getkey()
            move = int(key)
            if 1 <= move <= 9:
                return move - 1
        except (ValueError, curses.error):
            pass

def check_winner(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            return board[pos[0]]
    return None

def full_tictactoe(stdscr):
    board = [" "] * 9
    player = "X"
    game_over = False

    curses.curs_set(0)
    stdscr.nodelay(1)

    while not game_over:
        draw_board(stdscr, board)
        move = get_move(stdscr)
        if board[move] == " ":
            board[move] = player
            if check_winner(board):
                game_over = True
            else:
                player = "O" if player == "X" else "X"

    draw_board(stdscr, board)
    winner = check_winner(board)
    if winner:
        stdscr.addstr(8, 0, "Player {} wins!".format(winner))
    else:
        stdscr.addstr(8, 0, "It's a draw!")

    stdscr.addstr(10, 0, "Press any key to exit...")
    stdscr.getch()

#curses.wrapper(full_tictactoe)