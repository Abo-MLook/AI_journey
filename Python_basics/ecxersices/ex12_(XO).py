import random


# display the board
def show_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# check if position is free
def is_free(board, pos):
    return board[pos] == " "


# check win
def check_win(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for combo in win_positions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


# check draw
def check_draw(board):
    return " " not in board


# player move
def player_move(board, player):
    while True:
        try:
            pos = int(input(f"Choose position (1-9) for {player}: ")) - 1
            if pos >= 0 and pos <= 8:
                if is_free(board, pos):
                    board[pos] = player
                    break
                else:
                    print("Position already taken.")
            else:
                print("Choose number between 1 and 9.")
        except:
            print("Invalid input.")


# computer move (random)
def computer_move(board, player):
    free_positions = [i for i in range(9) if board[i] == " "]
    pos = random.choice(free_positions)
    board[pos] = player


# main game
def play_game():
    while True:
        board = [" "] * 9

        mode = input("Play with (1) Computer or (2) Player? ")
        player1 = input("Choose X or O: ").upper()
        player2 = "O" if player1 == "X" else "X"

        turn = input("Who starts? (1 or 2): ")

        show_board(board)

        while True:
            if turn == "1":
                player_move(board, player1)
                show_board(board)

                if check_win(board, player1):
                    print("Player 1 wins!")
                    break

                if check_draw(board):
                    print("Draw!")
                    break

                turn = "2"

            else:
                if mode == "1":
                    computer_move(board, player2)
                    print("Computer played.")
                else:
                    player_move(board, player2)

                show_board(board)

                if check_win(board, player2):
                    if mode == "1":
                        print("Computer wins!")
                    else:
                        print("Player 2 wins!")
                    break

                if check_draw(board):
                    print("Draw!")
                    break

                turn = "1"

        again = input("Play again? (y/n): ")
        if again.lower() != "y":
            break


# run game
play_game()