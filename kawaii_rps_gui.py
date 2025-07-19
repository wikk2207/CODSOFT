import tkinter as tk
import random

# Colors and styles
BG_COLOR = "#f6f0f8"
BUTTON_COLOR = "#d1b3ff"
HOVER_COLOR = "#c9a0ff"
TEXT_COLOR = "#5a189a"
GLASS_WHITE = "#ffffff"
GLASS_ALPHA = "#ffffffcc"

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
comp_score = 0

# Game logic
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a Tie!"
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Scissors" and comp_choice == "Paper") or
        (user_choice == "Paper" and comp_choice == "Rock")
    ):
        return "You Win!"
    else:
        return "You Lose!"

# Play a round
def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    result = determine_winner(user_choice, comp_choice)

    if result == "You Win!":
        user_score += 1
    elif result == "You Lose!":
        comp_score += 1

    user_choice_label.config(text=f"You chose: {user_choice}")
    comp_choice_label.config(text=f"Computer chose: {comp_choice}")
    result_label.config(text=result)
    score_label.config(text=f"🎀 Your Score: {user_score}  |  CPU Score: {comp_score}")

# Reset game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Let's play again!")
    user_choice_label.config(text="")
    comp_choice_label.config(text="")
    score_label.config(text=f"🎀 Your Score: {user_score}  |  CPU Score: {comp_score}")

# Exit game
def exit_game():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Chibi Rock-Paper-Scissors 🎮")
root.geometry("450x500")
root.config(bg=BG_COLOR)

title = tk.Label(root, text="🌸Rock Paper Scissors🌸", font=("Comic Sans MS", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
title.pack(pady=15)

frame = tk.Frame(root, bg=GLASS_WHITE, bd=0, relief="flat")
frame.pack(pady=10, padx=20, ipadx=20, ipady=20)

user_choice_label = tk.Label(frame, text="", font=("Comic Sans MS", 12), fg=TEXT_COLOR, bg=GLASS_WHITE)
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(frame, text="", font=("Comic Sans MS", 12), fg=TEXT_COLOR, bg=GLASS_WHITE)
comp_choice_label.pack(pady=5)

result_label = tk.Label(frame, text="Choose your move!", font=("Comic Sans MS", 14, "bold"), fg="#7209b7", bg=GLASS_WHITE)
result_label.pack(pady=15)

score_label = tk.Label(frame, text=f"🎀 Your Score: 0  |  CPU Score: 0", font=("Comic Sans MS", 11), fg="#4a148c", bg=GLASS_WHITE)
score_label.pack(pady=5)

btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=20)

def make_choice_button(text):
    return tk.Button(
        btn_frame, text=text, font=("Comic Sans MS", 12), width=10,
        bg=BUTTON_COLOR, fg="white", activebackground=HOVER_COLOR,
        command=lambda: play(text), relief="raised", bd=3
    )

rock_btn = make_choice_button("Rock")
paper_btn = make_choice_button("Paper")
scissors_btn = make_choice_button("Scissors")

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

# Play again & Exit
action_frame = tk.Frame(root, bg=BG_COLOR)
action_frame.pack(pady=10)

play_again_btn = tk.Button(action_frame, text="🔁 Play Again", font=("Comic Sans MS", 11), bg="#c084fc", fg="white", command=reset_game)
exit_btn = tk.Button(action_frame, text="❌ Exit", font=("Comic Sans MS", 11), bg="#f87171", fg="white", command=exit_game)

play_again_btn.grid(row=0, column=0, padx=15)
exit_btn.grid(row=0, column=1, padx=15)

root.mainloop()
