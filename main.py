# -*- coding: utf-8 -*-
"""
@author: HamzaEren
"""

#%% Modules
from tkinter import Tk, Button, Label, LabelFrame, PhotoImage
from random import choice, randint


#%% Global Variables
YOUR_CHOICE = ""
PC_CHOICE = ""
NUMBER = 0
X = 0
OPTIONS = ["Paper", "Scissors"]
RESULT = ""


#%% Functions
def Select(selected, image):
    global YOUR_CHOICE, PC_CHOICE, NUMBER
    
    rock_btn.place_forget()
    paper_btn.place_forget()
    scissors_btn.place_forget()
    
    #selected_lbl["image"] = image
    selected_lbl.config(image=image)
    selected_lbl.place(x=30, y=110, width=60, height=60)
    
    if selected == "Rock":
        YOUR_CHOICE = "Rock"
    elif selected == "Paper":
        YOUR_CHOICE = "Paper"
    else:
        YOUR_CHOICE = "Scissors"
        
    rock_lbl.place(x=270, y=110, width=60, height=60)    
    
    NUMBER = randint(20, 30)
    SelectOfPc()



def SelectOfPc():
    global PC_CHOICE, NUMBER, X, OPTIONS
    
    PC_CHOICE = choice(OPTIONS)
    if PC_CHOICE == "Rock":
        paper_lbl.place_forget()
        scissors_lbl.place_forget()
        rock_lbl.place(x=270, y=110, width=60, height=60)
        OPTIONS = ["Paper", "Scissors"]
    elif PC_CHOICE == "Paper":
        rock_lbl.place_forget()
        scissors_lbl.place_forget()
        paper_lbl.place(x=270, y=110, width=60, height=60)
        OPTIONS = ["Rock", "Scissors"]
    else:
        paper_lbl.place_forget()
        rock_lbl.place_forget()
        scissors_lbl.place(x=270, y=110, width=60, height=60)
        OPTIONS = ["Rock", "Paper"]

    if X < NUMBER:
        X += 1
        app.after(100, SelectOfPc)
        
    else:
        Result()
        
def Result():
    global YOUR_CHOICE, PC_CHOICE, RESULT
    
    if YOUR_CHOICE == "Rock":
        if PC_CHOICE == "Rock":
            RESULT = "Draw"
        elif PC_CHOICE == "Paper":
            RESULT = "You Lose"
        else:
            RESULT = "You Win"
    elif YOUR_CHOICE == "Paper":
        if PC_CHOICE == "Rock":
            RESULT = "You Win"
        elif PC_CHOICE == "Paper":
            RESULT = "Draw"
        else:
            RESULT = "You Lose"
    else:
        if PC_CHOICE == "Rock":
            RESULT = "You Lose"
        elif PC_CHOICE == "Paper":
            RESULT = "You Win"
        else:
            RESULT = "Draw"
            
    result_lbl.config(text=RESULT)
    result_frame.place(x=110, y=90, width=140, height=100)
            

def Exit():
    global VALUE
    app.attributes("-alpha", VALUE)
    
    if VALUE > 0:
        VALUE -= 0.1
        app.after(50, Exit)
        
    else:
        app.destroy()


def Restart():
    global X
    
    X = 0
    rock_btn.place(x=30, y=30, width=60, height=60)
    paper_btn.place(x=30, y=110, width=60, height=60)
    scissors_btn.place(x=30, y=190, width=60, height=60)
    selected_lbl.place_forget()
    rock_lbl.place_forget()
    paper_lbl.place_forget()
    scissors_lbl.place_forget()
    result_frame.place_forget()
    


#%% Main App
app = Tk()
app.title("Rock - Paper - Scissors")
app.configure(bg="#444")
app.geometry("360x280")
app.resizable(0, 0)

rock_img = PhotoImage(file = "images/rock.png")
rock_btn = Button(app, image=rock_img, borderwidth=0, background="#444", activebackground="#444", command=lambda: Select("Rock", rock_img))
rock_btn.place(x=30, y=30, width=60, height=60)
paper_img = PhotoImage(file = "images/paper.png")
paper_btn = Button(app, image=paper_img, borderwidth=0, background="#444", activebackground="#444", command=lambda: Select("Paper", paper_img))
paper_btn.place(x=30, y=110, width=60, height=60)
scissors_img = PhotoImage(file = "images/scissors.png")
scissors_btn = Button(app, image=scissors_img, borderwidth=0, background="#444", activebackground="#444", command=lambda: Select("Scissors", scissors_img))
scissors_btn.place(x=30, y=190, width=60, height=60)

selected_lbl = Label(app, text="")
selected_lbl.place_forget()

vs_img = PhotoImage(file = "images/vs.png")
vs_btn = Label(app, image=vs_img, borderwidth=0, background="#444", activebackground="#444")
vs_btn.place(x=150, y=110, width=60, height=60)

rock_lbl = Button(app, image=rock_img, borderwidth=0, background="#444", activebackground="#444")
rock_lbl.place_forget() #(x=140, y=60, width=30, height=30)
paper_lbl = Button(app, image=paper_img, borderwidth=0, background="#444", activebackground="#444")
paper_lbl.place_forget()
scissors_lbl = Button(app, image=scissors_img, borderwidth=0, background="#444", activebackground="#444")
scissors_lbl.place_forget()

result_frame = LabelFrame(app, text="Result", labelanchor="se", bg="#444", fg="#FFF")
result_frame.place_forget()

result_lbl = Label(result_frame, text="", bg="#444", fg="#FFF")
result_lbl.place(x=20, y=20, width=100, height=20)

close_btn = Button(result_frame, text="Kapat", bg="#444", fg="#FFF", command=Exit)
close_btn.place(x=20, y=60, width=40, height=20)

restart_btn = Button(result_frame, text="Tekrar", bg="#444", fg="#FFF", command=Restart)
restart_btn.place(x=80, y=60, width=40, height=20)

app.mainloop()
