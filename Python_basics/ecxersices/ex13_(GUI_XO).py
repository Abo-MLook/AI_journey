import tkinter as tk
from tkinter import messagebox
import copy

squares = {1: ' ', 2: ' ', 3: ' ',
           4: ' ', 5: ' ', 6: ' ',
           7: ' ', 8: ' ', 9: ' '}

my_symbol = 'X'
rival_symbol = 'O'
i_go_first = True
facing_machine = True
whose_turn = 'me'

cells = {}

def did_someone_win(grid, sym):
    lines = [(1,2,3),(4,5,6),(7,8,9),
             (1,4,7),(2,5,8),(3,6,9),
             (1,5,9),(3,5,7)]
    for line in lines:
        if grid[line[0]] == grid[line[1]] == grid[line[2]] == sym:
            return True
    return False

def all_filled(grid):
    return all(grid[k] != ' ' for k in grid)

def spot_free(grid, n):
    return grid[n] == ' '

def machine_picks():
    global squares, whose_turn

    for n in range(1, 10):
        if spot_free(squares, n):
            trial = copy.deepcopy(squares)
            trial[n] = rival_symbol
            if did_someone_win(trial, rival_symbol):
                squares[n] = rival_symbol
                cells[n].config(text=rival_symbol)
                return n

    for n in range(1, 10):
        if spot_free(squares, n):
            trial = copy.deepcopy(squares)
            trial[n] = my_symbol
            if did_someone_win(trial, my_symbol):
                squares[n] = rival_symbol
                cells[n].config(text=rival_symbol)
                return n

    if spot_free(squares, 5):
        squares[5] = rival_symbol
        cells[5].config(text=rival_symbol)
        return 5

    for n in [1, 3, 7, 9]:
        if spot_free(squares, n):
            squares[n] = rival_symbol
            cells[n].config(text=rival_symbol)
            return n

    for n in range(1, 10):
        if spot_free(squares, n):
            squares[n] = rival_symbol
            cells[n].config(text=rival_symbol)
            return n

def wipe_board():
    global squares
    squares = {k: ' ' for k in range(1, 10)}
    for k in cells:
        cells[k].config(text=' ')

def launch():
    global my_symbol, rival_symbol, i_go_first, facing_machine, whose_turn

    facing_machine = (opponent_choice.get() == 'machine')
    my_symbol = letter_choice.get()
    rival_symbol = 'O' if my_symbol == 'X' else 'X'
    i_go_first = (first_move_choice.get() == 'me')

    wipe_board()

    if facing_machine and not i_go_first:
        whose_turn = 'machine'
        machine_picks()
        if did_someone_win(squares, rival_symbol):
            messagebox.showinfo("Result", "Machine wins!")
            play_again_prompt()
            return
        whose_turn = 'me'
    else:
        whose_turn = 'me'

def my_turn(n):
    global whose_turn

    if not spot_free(squares, n):
        messagebox.showwarning("Oops", "That spot is taken!")
        return

    squares[n] = my_symbol
    cells[n].config(text=my_symbol)

    if did_someone_win(squares, my_symbol):
        messagebox.showinfo("Result", "You win!")
        play_again_prompt()
        return

    if all_filled(squares):
        messagebox.showinfo("Result", "It's a draw!")
        play_again_prompt()
        return

    if facing_machine:
        whose_turn = 'machine'
        picked = machine_picks()
        if picked is None:
            return

        if did_someone_win(squares, rival_symbol):
            messagebox.showinfo("Result", "Machine wins!")
            play_again_prompt()
            return

        if all_filled(squares):
            messagebox.showinfo("Result", "It's a draw!")
            play_again_prompt()
            return

        whose_turn = 'me'
    else:
        if whose_turn == 'me':
            whose_turn = 'second'
        else:
            whose_turn = 'me'

def second_player_turn(n):
    global whose_turn

    if not spot_free(squares, n):
        messagebox.showwarning("Oops", "That spot is taken!")
        return

    sym = my_symbol if whose_turn == 'me' else rival_symbol

    squares[n] = sym
    cells[n].config(text=sym)

    if did_someone_win(squares, sym):
        who_won = "Player 1" if sym == my_symbol else "Player 2"
        messagebox.showinfo("Result", f"{who_won} wins!")
        play_again_prompt()
        return

    if all_filled(squares):
        messagebox.showinfo("Result", "It's a draw!")
        play_again_prompt()
        return

    whose_turn = 'second' if whose_turn == 'me' else 'me'

def square_pressed(n):
    if facing_machine:
        my_turn(n)
    else:
        second_player_turn(n)

def play_again_prompt():
    go_again = messagebox.askyesno("Again?", "Do you want to start another game?")
    if go_again:
        launch()
    else:
        wipe_board()

window = tk.Tk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)

top_area = tk.Frame(window)
top_area.pack(padx=10, pady=5)

tk.Label(top_area, text="Play With").grid(row=0, column=0, sticky='w', pady=3)
opponent_choice = tk.StringVar(value='machine')
tk.Radiobutton(top_area, text="Computer", variable=opponent_choice, value='machine').grid(row=0, column=1, sticky='w')
tk.Radiobutton(top_area, text="Player 2", variable=opponent_choice, value='human').grid(row=0, column=2, sticky='w')

tk.Label(top_area, text="Select").grid(row=1, column=0, sticky='w', pady=3)
letter_choice = tk.StringVar(value='X')
tk.Radiobutton(top_area, text="X", variable=letter_choice, value='X').grid(row=1, column=1, sticky='w')
tk.Radiobutton(top_area, text="O", variable=letter_choice, value='O').grid(row=1, column=2, sticky='w')

tk.Label(top_area, text="Start the game").grid(row=2, column=0, sticky='w', pady=3)
first_move_choice = tk.StringVar(value='me')
tk.Radiobutton(top_area, text="Yes", variable=first_move_choice, value='me').grid(row=2, column=1, sticky='w')
tk.Radiobutton(top_area, text="No", variable=first_move_choice, value='machine').grid(row=2, column=2, sticky='w')

tk.Button(top_area, text="start", command=launch).grid(row=3, column=2, pady=5)

grid_area = tk.Frame(window, bg='gray')
grid_area.pack(padx=20, pady=10)

layout = [(0,0,1),(0,1,2),(0,2,3),
          (1,0,4),(1,1,5),(1,2,6),
          (2,0,7),(2,1,8),(2,2,9)]

for (r, c, n) in layout:
    b = tk.Button(grid_area, text=' ', width=6, height=3,
                  font=('Arial', 18, 'bold'), bg='gray', fg='white',
                  command=lambda pos=n: square_pressed(pos))
    b.grid(row=r, column=c, padx=2, pady=2)
    cells[n] = b

window.mainloop()