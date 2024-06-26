import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import pygame

pygame.init()
click_sound = pygame.mixer.Sound("click.wav")
win_sound = pygame.mixer.Sound("win.wav")
lose_sound = pygame.mixer.Sound("lose.wav")
tie_sound = pygame.mixer.Sound("tie.wav")

def play_sound(sound):
    pygame.mixer.Sound.play(sound)

def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "tie"
    elif (user_choice == "rock" and opponent_choice == "scissors") or \
         (user_choice == "scissors" and opponent_choice == "paper") or \
         (user_choice == "paper" and opponent_choice == "rock"):
        return "user"
    else:
        return "opponent"

def display_result(user_choice, opponent_choice, winner):
    play_sound(click_sound)
    result_message = f"You chose: {user_choice}\nOpponent chose: {opponent_choice}\n"
    if winner == "tie":
        result_message += "It's a tie!"
        play_sound(tie_sound)
    elif winner == "user":
        result_message += "You win!"
        play_sound(win_sound)
    else:
        result_message += "You lose!"
        play_sound(lose_sound)
    
    messagebox.showinfo("Result", result_message)

def play_with_computer(user_choice):
    opponent_choice = random.choice(["rock", "paper", "scissors"])
    winner = determine_winner(user_choice, opponent_choice)
    display_result(user_choice, opponent_choice, winner)

def play_with_friend(user_choice):
    opponent_choice = simpledialog.askstring("Opponent's turn", "Opponent, enter rock, paper, or scissors:").lower()
    while opponent_choice not in ["rock", "paper", "scissors"]:
        opponent_choice = simpledialog.askstring("Invalid choice", "Please enter rock, paper, or scissors:").lower()
    winner = determine_winner(user_choice, opponent_choice)
    display_result(user_choice, opponent_choice, winner)

def on_choice(choice, mode):
    if mode == "computer":
        play_with_computer(choice)
    else:
        play_with_friend(choice)

def start_game(mode):
    game_window = tk.Toplevel(root)
    game_window.title("Rock-Paper-Scissors")

    tk.Label(game_window, text="Choose your move:", font=("Arial", 14)).pack(pady=10)

    frame = tk.Frame(game_window)
    frame.pack(pady=10)

    rock_button = tk.Button(frame, text="Rock", font=("Arial", 14), command=lambda: on_choice("rock", mode))
    rock_button.grid(row=0, column=0, padx=10)

    paper_button = tk.Button(frame, text="Paper", font=("Arial", 14), command=lambda: on_choice("paper", mode))
    paper_button.grid(row=0, column=1, padx=10)

    scissors_button = tk.Button(frame, text="Scissors", font=("Arial", 14), command=lambda: on_choice("scissors", mode))
    scissors_button.grid(row=0, column=2, padx=10)

def main_menu():
    tk.Label(root, text="Welcome to Rock-Paper-Scissors!", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Play with Computer", font=("Arial", 14), command=lambda: start_game("computer")).pack(pady=10)
    tk.Button(root, text="Play with Friend", font=("Arial", 14), command=lambda: start_game("friend")).pack(pady=10)
    tk.Button(root, text="Quit", font=("Arial", 14), command=root.quit).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rock-Paper-Scissors")

    main_menu()

    root.mainloop()
