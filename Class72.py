from tkinter import *
import datetime

root = Tk()
root.title("Age Calculator")
root.geometry("400x400")

label1 = Label(root, text = "Hello! Please enter your date of birth below (in YYYY-MM-DD format): ")
label1.pack()

label2 = Label(root, text = "Name: ")
label2.place(x = 50, y = 50)
entry1 = Entry(root)
entry1.place(x = 150, y = 50)
label3 = Label(root, text = "Day: ")
label3.place(x = 50, y = 80)
entry2 = Entry(root)
entry2.place(x = 150, y = 80)
label4 = Label(root, text = "Month: ")
label4.place(x = 50, y = 110)
entry3 = Entry(root)
entry3.place(x = 150, y = 110)
label5 = Label(root, text = "Year: ")
label5.place(x = 50, y = 140)
entry4 = Entry(root)
entry4.place(x = 150, y = 140)

def calculate_age():
    name = entry1.get()
    day = int(entry2.get())
    month = int(entry3.get())
    year = int(entry4.get())
    
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    result_label.config(text = f"{name}, you are {age} years old.")

button = Button(root, text = "Calculate Age", command = calculate_age)
button.place(x = 150, y = 180)
result_label = Label(root, text = "", font = ("Sample", 12))
result_label.place(x = 50, y = 220)

root.mainloop()