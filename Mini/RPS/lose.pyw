from tkinter import*
from PIL import Image, ImageTk
import pygame

root=Tk()
root.title("OH NO")

win_width=580
win_height=450

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=(screen_width/2)-(win_width/2)
y=(screen_height/2)-(win_height/2)


root.geometry(f'{win_width}x{win_height}+{int(x)}+{int(y)}')

img=Image.open("C:\\Users\\vishn\\Desktop\\MINI GAME HUB\\Mini\\RPS\\lose.png")
bg_img=ImageTk.PhotoImage(img)

label=Label(root, image=bg_img)
label.place(x=0, y=0)

def exit():
    root.destroy()

img2=Image.open("C:\\Users\\vishn\\Desktop\\MINI GAME HUB\\Mini\\RPS\\ok.png")
resize_img2=img2.resize((100, 50))
button2=ImageTk.PhotoImage(resize_img2)

reset_button=Button(root, image=button2,  command=exit)
reset_button.pack(side=RIGHT, padx=15)

pygame.mixer.init()

pygame.mixer.music.load("C:\\Users\\vishn\\Desktop\\MINI GAME HUB\\Mini\\RPS\\lose.mp3")
pygame.mixer.music.play()


root.mainloop()






 

 



