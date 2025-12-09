import tkinter as tk
from tkinter import font

def set_tile(row, column):
    global curr_player

    if game_over:
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player

    if curr_player == playerX:
        board[row][column].config(image=img_X, bg=color_gray) ## Add image of red canes to cell
    else:
        board[row][column].config(image=img_O, bg=color_gray) ## Add image of green ornament to cell

    curr_player = playerO if curr_player == playerX else playerX
    label["text"] = curr_player + "'s turn"

    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Check horizontal
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and 
            board[row][0]["text"] != ""):
            highlight_winner(row, 0, row, 1, row, 2) ## highlight who is winner
            label.config(text=board[row][0]["text"] + " wins!", fg=color_yellow)
            game_over = True
            return

    # Check vertical
    for col in range(3):
        if (board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] and 
            board[0][col]["text"] != ""):
            highlight_winner(0, col, 1, col, 2, col) ## highlight who is winner
            label.config(text=board[0][col]["text"] + " wins!", fg=color_yellow)
            game_over = True
            return

    # Check diagonals
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and 
        board[0][0]["text"] != ""):
        highlight_winner(0, 0, 1, 1, 2, 2) ## highlight who is winner
        label.config(text=board[0][0]["text"] + " wins!", fg=color_yellow)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and 
        board[0][2]["text"] != ""):
        highlight_winner(0, 2, 1, 1, 2, 0) ## highlight who is winner
        label.config(text=board[0][2]["text"] + " wins!", fg=color_yellow)
        game_over = True
        return
    
    # Check for Tie
    if turns == 9:
        game_over = True
        label.config(text="It's a Tie!", fg=color_yellow)

def highlight_winner(r1, c1, r2, c2, r3, c3): ## created function that highlights winners cells
    board[r1][c1].config(bg=color_light_gray)
    board[r2][c2].config(bg=color_light_gray)
    board[r3][c3].config(bg=color_light_gray)

# Reset everything for new game
def new_game():
    global turns, game_over, curr_player
    
    turns = 0
    game_over = False
    curr_player = playerX
    
    label.config(text=curr_player + "'s turn", fg="white", bg=color_gray)
    
    for row in range(3):
        for col in range(3):
            board[row][col].config(
                text="", 
                image="", ## reset image that was added
                bg=color_gray,
                relief="raised"
            )

# Game setup
playerX = "X"
playerO = "O"
curr_player = playerX
turns = 0
game_over = False

# Colors
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

# Window setup
window = tk.Tk()
window.title("Christmas Tic Tac Toe") ## New game title
window.configure(bg=color_gray)
window.resizable(True, True)
window.minsize(350, 400) 

## Load images with error handling
try:
    img_X = tk.PhotoImage(file="x.png")
    img_O = tk.PhotoImage(file="o.png")
except:
    img_X = None
    img_O = None

custom_font = font.Font(family="Consolas", size=18, weight="bold")

# Main frame
main_frame = tk.Frame(window, bg=color_gray, padx=10, pady=10)
main_frame.pack(expand=True, fill="both")

# Title label
title_label = tk.Label(
    main_frame,
    text="CHRISTMAS TIC TAC TOE",
    font=("Consolas", 22, "bold"),
    bg=color_gray,
    fg="white",
    pady=5
)
title_label.pack()

# Game info label
label = tk.Label(
    main_frame,
    text=curr_player + "'s turn",
    font=("Consolas", 14),
    bg=color_gray,
    fg="white",
    pady=5
)
label.pack()

# Game board frame
board_frame = tk.Frame(main_frame, bg=color_gray, padx=5, pady=5)
board_frame.pack(expand=True)

# Create board buttons
board = []

TILE_SIZE = 90

for row in range(3):
    board_row = []
    for col in range(3):
        cell_frame = tk.Frame(board_frame, width=TILE_SIZE, height=TILE_SIZE)
        cell_frame.grid(row=row, column=col, padx=3, pady=3)
        
        cell_frame.grid_propagate(False)
        cell_frame.pack_propagate(False)

        btn = tk.Button(
            cell_frame,
            text="",
            font=custom_font,
            bg=color_gray,
            fg=color_blue,
            activebackground=color_light_gray,
            relief="raised",
            borderwidth=3,
            command=lambda r=row, c=col: set_tile(r, c)
        )
        btn.pack(fill="both", expand=True)
        
        board_row.append(btn)
        
    board.append(board_row)

# Control buttons frame
control_frame = tk.Frame(main_frame, bg=color_gray, pady=10)
control_frame.pack(fill="x")

# Restart button
restart_btn = tk.Button(
    control_frame,
    text="NEW GAME",
    font=("Consolas", 12, "bold"),
    bg=color_blue,
    fg="white",
    activebackground=color_light_gray,
    activeforeground="white",
    relief="raised",
    borderwidth=2,
    padx=20,
    pady=8,
    command=new_game
)
restart_btn.pack()

## Exit button for exit
exit_btn = tk.Button(
    control_frame,
    text="EXIT",
    font=("Consolas", 11),
    bg=color_gray,
    fg="white",
    activebackground=color_light_gray,
    activeforeground="white",
    relief="raised",
    borderwidth=2,
    padx=20,
    pady=4,
    command=window.quit
)
exit_btn.pack(pady=(10, 0))

## Credit for framework that was used
status_label = tk.Label(
    control_frame,
    text="Made with Tkinter",
    font=("Consolas", 8),
    bg=color_gray,
    fg=color_light_gray,
    pady=5
)
status_label.pack()

# Center window on screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

window.mainloop()
