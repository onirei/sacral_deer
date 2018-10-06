from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Сакральный олень")


def roll():
    i = str(random.randint(0, 9999999999))
    while len(i) < 10:
        i = '0'+i
    label1['text'] = i


def help43():
    messagebox.showinfo("Ответы", "Задавай вопрос и жми")

canvas = Canvas(root, width=640, height=380, bg='white')
canvas.pack()
image = Image.open("pic.jpg")
photo = ImageTk.PhotoImage(image)
canvas.create_image(320, 190, image=photo)

button1 = Button(root, width=30,  height=2, text='Roll')
button2 = Button(root,width=10, height=2, text='?')
button1.pack(side='left')
button2.pack(side='right')
button1.bind("<Button-1>", roll)
button2.bind("<Button-1>", help43)
label1 = Label(root, height=3, text='')
label1.pack()


root.mainloop()