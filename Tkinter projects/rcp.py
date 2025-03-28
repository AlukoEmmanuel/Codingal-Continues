from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import random

def create_image(shape):
    # Create a blank image with white background
    img = Image.new("RGB", (100, 100), "white")
    draw = ImageDraw.Draw(img)
    
    if shape == 'rock':
        # Draw gray circle
        draw.ellipse([20, 20, 80, 80], fill="#808080", outline="black")
    elif shape == 'paper':
        # Draw white rectangle with black X
        draw.rectangle([10, 10, 90, 90], outline="black")
        draw.line([30, 30, 70, 70], fill="black", width=2)
        draw.line([70, 30, 30, 70], fill="black", width=2)
    elif shape == 'scissors':
        # Draw red X
        draw.line([30, 30, 70, 70], fill="red", width=3)
        draw.line([70, 30, 30, 70], fill="red", width=3)
    
    return ImageTk.PhotoImage(img)

T = Tk()
T.title("Rock Paper Scissors")
T.geometry("500x600")

# Generate images using PIL
rock_img = create_image('rock')
paper_img = create_image('paper')
scissors_img = create_image('scissors')

# Rest of the game code (keep the same as before)
# [Paste the remaining game code here including buttons, labels, and game logic]

T.mainloop()