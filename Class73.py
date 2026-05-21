from tkinter import *

root = Tk()
root.title("Length Converter")
root.geometry("400x400")

label1 = Label(root, text = "Enter length in inches: ")
label1.pack()
entry1 = Entry(root)
entry1.pack()

def convert():
    inches = float(entry1.get())
    centimeters = inches * 2.54
    label2.config(text = f"{inches} inches is equal to {centimeters} centimeters.", fg = "green")

button = Button(root, text = "Convert", command = convert)
button.pack()
label2 = Label(root, text = "")
label2.pack()

root.mainloop()