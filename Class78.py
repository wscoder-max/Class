from tkinter import *

root = Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

password_label = Label(root, text = "Enter your password: ")
password_label.pack()

password_entry = Entry(root, fg = ("black"), bg = ("white"), width = 50)
password_entry.pack()

evaluation = Label(root, text = "")
evaluation.pack()

def check_password_strength():
    password = password_entry.get()

    if len(password) <= 5:
        evaluation.config(text = "Weak Password", fg = ("red"))
    elif len(password) > 5 and len(password) <= 8:
        evaluation.config(text = "Medium Password", fg = ("yellow"))
    elif len(password) > 8 and len(password) <= 12:
        evaluation.config(text = "Strong Password", fg = ("green"))
    else:
        evaluation.config(text = "Very Strong Password", fg = ("dark green"))

check_button = Button(root, text = "Check Password Strength", command = check_password_strength)
check_button.pack()

root.mainloop()