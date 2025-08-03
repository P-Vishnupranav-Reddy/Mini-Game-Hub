from tkinter import *
from PIL import Image, ImageTk
import os

from random import randint

game = Tk()
game.title('Rock Paper Scissors Game')

game.geometry("1500x700")

wid = game.winfo_screenwidth()
heig = game.winfo_screenheight()

canvas=Canvas(game, width=wid, height=heig)
canvas.place(x=1,y=1)

img=Image.open("RPS\\rpsbg.png")
resize_img=img.resize((wid, heig))
bg_img=ImageTk.PhotoImage(resize_img)
bg=canvas.create_image(0,0, image=bg_img, anchor=NW)


rock=Image.open("RPS\\rock.png")
resize_rock=rock.resize((250, 225))
new_rock=ImageTk.PhotoImage(resize_rock)

paper=Image.open("RPS\\paper.png")
resize_paper=paper.resize((225, 250))
new_paper=ImageTk.PhotoImage(resize_paper)

scissors=Image.open("RPS\\scissors.png")
resize_scissors=scissors.resize((250, 200))
new_scissors=ImageTk.PhotoImage(resize_scissors)

image_list = [new_rock, new_paper, new_scissors]

pick_number = randint(0,2)

image_label = Label(game, image=image_list[pick_number])
image_label.pack(pady=20)

play_score=0
comp_score=0


def spin():
   global play_score
   global comp_score 
  
   
   pick_number = randint(0,2)
   image_label.config(image=image_list[pick_number])

   user_choice_value = user_var.get()
   

   if user_choice_value == "0":
       if   pick_number == 0:
           win_lose_label.config(text=("It's A Tie! Spin Again..."), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")
       elif pick_number == 1:
           win_lose_label.config(text=("You Lose...., PAPER COVERS ROCK!!...Try Again"), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")
       elif pick_number == 2:
           win_lose_label.config(text=("You Win...., ROCK SMASHES SCISSORS!!"), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")
   
   if user_choice_value == "0" and pick_number == 1:
       comp_score = comp_score + 1
       computer_score.config(text="Computer Score: "+str(comp_score))
   elif user_choice_value == "0" and pick_number == 2:
       play_score = play_score + 1
       player_score.config(text="Player Score: "+str(play_score))
       


   if user_choice_value == "1":
       if pick_number == 0:
           win_lose_label.config(text=("You Win...., PAPER COVERS ROCK!!"), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")
       elif pick_number == 1:
           win_lose_label.config(text=("It's A Tie! Spin Again..."), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")
       elif pick_number == 2:
           win_lose_label.config(text=("You Lose...., SCISSORS CUTS PAPER!!...Try again"), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")

   if user_choice_value == "1" and pick_number == 2:
       comp_score = comp_score + 1
       computer_score.config(text="Computer Score: "+str(comp_score))
   elif user_choice_value == "1" and pick_number == 0:
       play_score = play_score + 1
       player_score.config(text="Player Score: "+str(play_score))



   if user_choice_value == "2":
       if pick_number == 0:
           win_lose_label.config(text=("You Lose...., ROCK SMASHES SCISSORS!!...Try Again"), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")
       elif pick_number == 1:
           win_lose_label.config(text=("You Win...., SCISSORS CUTS PAPER!!"), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")
       elif pick_number == 2:
           win_lose_label.config(text=("It's A Tie! Spin Again..."), font=("Bodoni MT", 25), fg="#000000", bg="#5f6c8e")

   if user_choice_value == "2" and pick_number == 0:
       comp_score = comp_score + 1
       computer_score.config(text="Computer Score: "+str(comp_score))
   elif user_choice_value == "2" and pick_number == 1:
       play_score = play_score + 1
       player_score.config(text="Player Score: "+str(play_score))


   if play_score==5:
       os.startfile("RPS\\Congragulations.pyw")  
       play_score=0 
       comp_score=0
       

   if comp_score==5:
       os.startfile("RPS\\lose.pyw")  
       play_score=0
       comp_score=0


def restart():
    game.destroy()
    os.startfile("RPS\\RPS.pyw")

def exit():
    game.destroy()
  

user_frame=Frame(game, height=6, bg="#5f6c8e")
user_frame.pack(pady=10)   


img_r=Image.open("RPS\\roc(1).png")
resize_img_r=img_r.resize((100, 150))
bg_img_r=ImageTk.PhotoImage(resize_img_r)

img_p=Image.open("RPS\\pape(1).png")
resize_img_p=img_p.resize((100, 150))
bg_img_p=ImageTk.PhotoImage(resize_img_p)

img_s=Image.open("RPS\\scissor(1).png")
resize_img_s=img_s.resize((100, 150))
bg_img_s=ImageTk.PhotoImage(resize_img_s)

   
user_var=StringVar()


user_choice1 = Radiobutton(user_frame, variable=user_var, value="0", image=bg_img_r, command=spin)
user_choice2 = Radiobutton(user_frame, variable=user_var, value="1", image=bg_img_p, command=spin)
user_choice3 = Radiobutton(user_frame, variable=user_var, value="2", image=bg_img_s,command=spin)

user_choice1.pack(side=LEFT, padx=20)
user_choice2.pack(side=LEFT, padx=20)
user_choice3.pack(side=LEFT, padx=20)
                           
player_score = Label(game, text="PLAYER SCORE:0", font=("Algerian",25), bg="#5f6c8e")
player_score.pack(side=LEFT, pady=60)
computer_score = Label(game, text="COMPUTER SCORE:0", font=("Algerian",25), bg="#5f6c8e")
computer_score.pack(side=RIGHT)

win_lose_label =Label(game, text="", font=("Arial" , 18), pady=20)
win_lose_label.pack(pady=30)

img1=Image.open("RPS\\restart.png")
resize_img1=img1.resize((200, 62))
button1=ImageTk.PhotoImage(resize_img1)

img2=Image.open("RPS\\exit.png")
resize_img2=img2.resize((150, 50))
button2=ImageTk.PhotoImage(resize_img2)

reset_button=Button(game, image=button1,  command=restart)
reset_button.pack(pady=15)

exit_button=Button(game, image=button2,  command=exit)
exit_button.pack(pady=15)

game.mainloop()              

