from tkinter import *
from PIL import Image, ImageTk
import random

T = Tk()
T.title("Rock Paper Scissors")
T.geometry("500x600")

# Game variables
user_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

# Load images
try:
    rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
    paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
    scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))
except:
    rock_img = PhotoImage(file="")  # Fallback if images not found
    paper_img = PhotoImage(file="")
    scissors_img = PhotoImage(file="")

# Game function
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    
    # Update choice labels
    user_choice_label.config(image=eval(f"{user_choice}_img"))
    computer_choice_label.config(image=eval(f"{computer_choice}_img"))
    
    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    
    # Update display
    result_label.config(text=result)
    score_label.config(text=f"You: {user_score}  Computer: {computer_score}")

# GUI Layout
Label(T, text="Choose Your Weapon!", font=('Arial', 16)).pack(pady=10)

# Choice buttons frame
button_frame = Frame(T)
button_frame.pack(pady=10)

Button(button_frame, image=rock_img, command=lambda: play_game('rock')).pack(side=LEFT, padx=10)
Button(button_frame, image=paper_img, command=lambda: play_game('paper')).pack(side=LEFT, padx=10)
Button(button_frame, image=scissors_img, command=lambda: play_game('scissors')).pack(side=LEFT, padx=10)

# Choices display
choices_frame = Frame(T)
choices_frame.pack(pady=20)

Label(choices_frame, text="Your Choice:", font=('Arial', 12)).grid(row=0, column=0)
user_choice_label = Label(choices_frame)
user_choice_label.grid(row=1, column=0, padx=20)

Label(choices_frame, text="Computer's Choice:", font=('Arial', 12)).grid(row=0, column=1)
computer_choice_label = Label(choices_frame)
computer_choice_label.grid(row=1, column=1, padx=20)

# Result and score
result_label = Label(T, text="", font=('Arial', 14))
result_label.pack(pady=10)

score_label = Label(T, text="You: 0  Computer: 0", font=('Arial', 12))
score_label.pack(pady=10)

# Reset button
Button(T, text="Reset Game", command=lambda: [globals().update(user_score=0, computer_score=0), 
                                             score_label.config(text="You: 0  Computer: 0"),
                                             result_label.config(text=""),
                                             user_choice_label.config(image=''),
                                             computer_choice_label.config(image='')]
      ).pack(pady=10)

T.mainloop()