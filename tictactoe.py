from tkinter import *


def update(i, j):
    global matrix, current_player, players, boxes_checked
    global winner_label, play_again
    matrix[i][j].config(
        text=players[current_player],
        fg="red",  #
        state="disabled",
    )
    boxes_checked += 1
    if checkWinner():
        winner_label.config(text=players[current_player] + " wins!")
        winner_label.grid(row=3, column=0, columnspan=3)
        play_again.grid(row=4, column=0, columnspan=3)
    elif boxes_checked == 9:
        winner_label.config(text="Tie!")
        winner_label.grid(row=3, column=0, columnspan=3)
        play_again.grid(row=4, column=0, columnspan=3)
        changeColor(row=False, column=False, firstDiagonal=False, secondDiagonal=False)
    current_player *= -1


def checkWinner():
    global matrix
    for i in range(0, 3):
        if matrix[i][0].cget("text") == matrix[i][1].cget("text"):
            if matrix[i][1].cget("text") == matrix[i][2].cget("text") != "":
                changeColor(
                    row=i, column=False, firstDiagonal=False, secondDiagonal=False
                )
                disableAll()
                return True
    for i in range(0, 3):
        if matrix[0][i].cget("text") == matrix[1][i].cget("text"):
            if matrix[1][i].cget("text") == matrix[2][i].cget("text") != "":
                changeColor(
                    row=False, column=i, firstDiagonal=False, secondDiagonal=False
                )
                disableAll()
                return True
    if matrix[0][0].cget("text") == matrix[1][1].cget("text"):
        if matrix[1][1].cget("text") == matrix[2][2].cget("text") != "":
            changeColor(
                row=False, column=False, firstDiagonal=True, secondDiagonal=False
            )
            disableAll()
            return True
    if matrix[0][2].cget("text") == matrix[1][1].cget("text") != "":
        if matrix[1][1].cget("text") == matrix[2][0].cget("text"):
            changeColor(
                row=False, column=False, firstDiagonal=False, secondDiagonal=True
            )
            disableAll()
            return True


def changeColor(row, column, firstDiagonal, secondDiagonal):
    global matrix
    if row:
        for i in range(0, 3):
            matrix[row][i].config(bg="green")
    elif column:
        for i in range(0, 3):
            matrix[i][column].config(bg="green")
    elif firstDiagonal:
        for i in range(0, 3):
            matrix[i][i].config(bg="green")
    elif secondDiagonal:
        for i in range(0, 3):
            matrix[i][2 - i].config(bg="green")
    else:
        for i in range(0, 3):
            for j in range(0, 3):
                matrix[i][j].config(bg="lightyellow")


def disableAll():
    global matrix
    for i in range(0, 3):
        for j in range(0, 3):
            matrix[i][j].config(state="disabled")


def reset():
    global boxes_checked, winner_label, play_again
    boxes_checked = 0
    winner_label.grid_forget()
    play_again.grid_forget()
    for i in range(0, 3):
        for j in range(0, 3):
            matrix[i][j].config(text="", bg="white", state="normal")


boxes_checked = 0
current_player = 1
players = {1: "x", -1: "o"}
matrix = [[], [], []]

window = Tk()
window.title("TicTacToe")

for i in range(0, 3):
    for j in range(0, 3):
        matrix[i].append(None)
        matrix[i][j] = Button(
            master=window,
            text="",
            fg="red",  #
            font=("Arial", 25, "bold"),
            width=8,
            height=4,
            command=lambda row=i, column=j: update(row, column),
        )
        matrix[i][j].grid(row=i, column=j)
winner_label = Label(
    master=window,
    text="... wins!",
    font=("Arial", 25),
)
play_again = Button(
    master=window,
    text="Play again?",
    font=("Arial", 25),
    command=reset,
)

window.mainloop()
