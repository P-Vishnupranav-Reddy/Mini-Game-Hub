from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title("MINI GAME HUB")
root.geometry("1500x700")

wid = root.winfo_screenwidth()
heig = root.winfo_screenheight()

canvas=Canvas(root, width=wid, height=heig)
canvas.place(x=1,y=1)

img=Image.open("RPS\\bg.png")
resize_img=img.resize((wid, heig))
bg_img=ImageTk.PhotoImage(resize_img)
bg=canvas.create_image(0,0, image=bg_img, anchor=NW)



def RPS():
    os.startfile("RPS\\RPS.pyw")
def Crashy_Plane():
    os.startfile("crpl\\game.pyw")




img1=PhotoImage(file="RPS\\rpsic.png")
img2=PhotoImage(file="RPS\\crplic.png")

RPS_button = Button(text="RPS", image=img1, command=RPS, borderwidth=0)
RPS_button.pack(side=TOP, pady=50)

Crashy_Plane_button = Button(text="CRASHY PLANE", image=img2, command=Crashy_Plane)
Crashy_Plane_button.pack(side=BOTTOM, pady=50)



root.mainloop()