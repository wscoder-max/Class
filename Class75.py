from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Root Window")

def topwindow():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top Level Window")

    label2 = Label(top, text = "This is a Top Level Window")
    label2.pack()

label1 = Label(root, text = "This is the Root Window")
label1.pack()

button1 = Button(root, text = "Open Top Level Window", command = topwindow)
button1.pack()

root.mainloop()