from tkinter import *
import random

root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")

rock_button = Button(root, text = "Rock", command = lambda: play("rock"))
rock_button.pack()
paper_button = Button(root, text = "Paper", command = lambda: play("paper"))
paper_button.pack()
scissors_button = Button(root, text = "Scissors", command = lambda: play("scissors"))
scissors_button.pack()
player_choice_label = Label(root, text = "You chose: ")
player_choice_label.pack()
computer_choice_label = Label(root, text = "Computer chose: ")
computer_choice_label.pack()
result_label = Label(root, text = "")
result_label.pack()

def play(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    player_choice_label.config(text = "You chose: {}".format(player_choice))
    computer_choice_label.config(text = "Computer chose: {}".format(computer_choice))

    if player_choice == computer_choice:
        result_label.config(text = "It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text = "You win!")
    else:
        result_label.config(text = "Computer wins!")

root.mainloop()