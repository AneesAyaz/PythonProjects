import tkinter as tk
import random

class DiceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Game")
        
        self.scores = {"Player 1": 0, "Player 2": 0}
        self.current_player = "Player 1"
        self.turn_total = 0

        self.status_label = tk.Label(root, text=f"{self.current_player}'s turn. Current score: {self.scores[self.current_player]}", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, columnspan=2)

        self.roll_button = tk.Button(root, text="Roll", command=self.roll_die, font=("Arial", 14))
        self.roll_button.grid(row=1, column=0)

        self.hold_button = tk.Button(root, text="Hold", command=self.hold_score, font=("Arial", 14))
        self.hold_button.grid(row=1, column=1)

        self.turn_label = tk.Label(root, text=f"Turn total: {self.turn_total}", font=("Arial", 14))
        self.turn_label.grid(row=2, column=0, columnspan=2)

        self.score_label = tk.Label(root, text=f"Scores: {self.scores}", font=("Arial", 14))
        self.score_label.grid(row=3, column=0, columnspan=2)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.grid(row=4, column=0, columnspan=2)

    def roll_die(self):
        roll = random.randint(1, 6)
        if roll == 1:
            self.turn_total = 0
            self.result_label.config(text=f"{self.current_player} rolled a 1! Turn over.")
            self.switch_player()
        else:
            self.turn_total += roll
            self.result_label.config(text=f"{self.current_player} rolled a {roll}.")
        
        self.update_labels()

    def hold_score(self):
        self.scores[self.current_player] += self.turn_total
        self.turn_total = 0
        if self.scores[self.current_player] >= 100:
            self.result_label.config(text=f"{self.current_player} wins with a score of {self.scores[self.current_player]}!")
            self.roll_button.config(state=tk.DISABLED)
            self.hold_button.config(state=tk.DISABLED)
        else:
            self.switch_player()
        
        self.update_labels()

    def switch_player(self):
        self.current_player = "Player 1" if self.current_player == "Player 2" else "Player 2"
        self.update_labels()

    def update_labels(self):
        self.status_label.config(text=f"{self.current_player}'s turn. Current score: {self.scores[self.current_player]}")
        self.turn_label.config(text=f"Turn total: {self.turn_total}")
        self.score_label.config(text=f"Scores: {self.scores}")

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()

