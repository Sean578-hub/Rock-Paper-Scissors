import tkinter as tk
from tkinter.messagebox import showinfo
import random

window = tk.Tk()
window.geometry("800x800")
window.title("Rock Paper Scissors")

photo1 = tk.PhotoImage(file = "Rock.png")
photo2 = tk.PhotoImage(file = "paper.png")
photo3 = tk.PhotoImage(file = "scissors.png")
my_choise = 0
life = 3
score = 0
def rock():
    global my_choise
    my_choise = 1
    label_Rock.configure(image = photo1)
    label_paper.configure(image = "")
    label_scissors.configure(image = "")
    label_random.configure(image = "")
    button_play.place(relx=0.5, rely=0.7)

def paper():
    global my_choise
    my_choise = 2
    label_paper.configure(image = photo2)
    label_Rock.configure(image= "")
    label_scissors.configure(image= "")
    label_random.configure(image="")
    button_play.place(relx=0.5, rely=0.7)

def scissors():
    global my_choise
    my_choise = 3
    label_scissors.configure(image = photo3)
    label_paper.configure(image = "")
    label_Rock.configure(image = "")
    label_random.configure(image="")
    button_play.place(relx=0.5, rely=0.7)

def random1():
    global my_choise
    global images
    global life
    global score

    images = random.randint(1, 3)
    if images == 1:
        label_random.configure(image = photo1)
    elif images == 2:
        label_random.configure(image = photo2)
    else:
        label_random.configure(image = photo3)
    button_play.place_forget()

    if images == 1 and my_choise == 1:
        label_game.configure(text = "Tie", font = ("Comic Sans MS", 20))
        label_life.configure(text = f"lifes : {life}", font = ("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    elif images == 1 and my_choise == 2:
        label_game.configure(text = "You won", font=("Comic Sans MS", 20))
        score +=1
        label_life.configure(text=f"lifes : {life}", font=("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    elif images == 1 and my_choise == 3:
        label_game.configure(text="I won", font=("Comic Sans MS", 20))
        life -=1
        label_life.configure(text=f"lifes : {life}", font=("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    elif images == 2 and my_choise == 2:
        label_game.configure(text="Tie", font=("Comic Sans MS", 20))
        label_life.configure(text=f"lifes : {life}", font=("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    elif images == 2 and my_choise == 1:
        label_game.configure(text="I won", font=("Comic Sans MS", 20))
        life -=1
        label_life.configure(text=f"lifes : {life}", font=("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    elif images == 2 and my_choise == 3:
        label_game.configure(text="You won", font=("Comic Sans MS", 20))
        score +=1
        label_life.configure(text=f"lifes : {life}", font=("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    elif images == 3 and my_choise == 3:
        label_game.configure(text="Tie", font=("Comic Sans MS", 20))
        label_life.configure(text=f"lifes : {life}", font=("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    elif images == 3 and my_choise == 2:
        label_game.configure(text="I won", font=("Comic Sans MS", 20))
        life -=1
        label_life.configure(text=f"lifes : {life}", font=("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    elif images == 3 and my_choise == 1:
        label_game.configure(text="You won", font=("Comic Sans MS", 20))
        score +=1
        label_life.configure(text=f"lifes : {life}", font=("Comic Sans MS", 20))
        label_score.configure(text=f"score : {score}", font=("Comic Sans MS", 20))
    if life == 0:
        showinfo(title = "GAME OVER", message = f"You lost, your score was {score}, have a good day")
        window.destroy()








label_title = tk.Label(text = "Rock Paper Scissors", font = ("Comic Sans MS", 20))
label_title.place(relx = 0.5, rely = 0.1, anchor = "center")

button_rock = tk.Button(text = "Rock", font = ("Comic Sans MS", 20), command = rock)
button_rock.place(relx = 0.5, rely = 0.5, anchor = "center")
label_Rock = tk.Label(text = "", font = ("Comic Sans MS", 20))
label_Rock.place(relx = 0.4, rely = 0.5, anchor = "center")

button_paper = tk.Button(text = "Paper", font = ("Comic Sans MS", 20), command = paper)
button_paper.place(relx = 0.6, rely = 0.5, anchor = "center")
label_paper = tk.Label(text = "", font = ("Comic Sans MS", 20))
label_paper.place(relx = 0.4, rely = 0.5, anchor = "center")

button_scissors = tk.Button(text = "Scissors", font = ("Comic Sans MS", 20), command = scissors)
button_scissors.place(relx = 0.7, rely = 0.5, anchor = "center")
label_scissors = tk.Label(text = "", font = ("Comic Sans MS", 20))
label_scissors.place(relx = 0.4, rely = 0.5, anchor = "center")

button_play = tk.Button(text = "Play", font = ("Comic Sans MS", 20), command = random1)

label_random = tk.Label(text = "", font = ("Comic Sans MS", 20))
label_random.place(relx = 0.2, rely = 0.5, anchor = "center")

label_life = tk.Label(text = f"lifes : {life}", font = ("Comic Sans MS", 20))
label_life.place(relx = 0.5, rely = 0.8, anchor = "center")

label_score = tk.Label(text = f"score : {score}", font = ("Comic Sans MS", 20))
label_score.place(relx = 0.5, rely = 0.85, anchor = "center")

label_game = tk.Label(text = "", font = ("Comic Sans MS", 20))
label_game.place(relx = 0.3, rely = 0.85, anchor = "center")





window.mainloop()

