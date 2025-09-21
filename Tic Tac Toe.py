import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.create_board()

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            b = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                          command=lambda i=i: self.make_move(i))
            b.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(b)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
                return
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_game()
                return

            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in win_combos:
            if self.board[a] != "" and self.board[a] == self.board[b] == self.board[c]:
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for b in self.buttons:
            b.config(text="")

# Run game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
