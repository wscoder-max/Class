from tkinter import *

root = Tk()
root.title("Interest Calculator")
root.geometry("400x400")

label1 = Label(root, text = "Enter principal amount: ")
label1.pack()
entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text = "Enter annual interest rate (in %): ")
label2.pack()
entry2 = Entry(root)
entry2.pack()

label3 = Label(root, text = "Enter time (in years): ")
label3.pack()
entry3 = Entry(root)
entry3.pack()   

def calculate():
    principal = float(entry1.get())
    rate = float(entry2.get())
    time = float(entry3.get())
    interest = (principal * rate * time) / 100
    label4.config(text = f"The interest is: {interest}", fg = "blue")
    label5.config(text = f"The total amount is: {principal + interest}", fg = "red")
button = Button(root, text = "Calculate", command = calculate)
button.pack()
label4 = Label(root, text = "")
label4.pack()
label5 = Label(root, text = "")
label5.pack()

root.mainloop()