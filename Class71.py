from tkinter import *

root = Tk()
root.title("Product of Two Numbers")
root.geometry("400x300")

label1 = Label(root, text = "Enter two numbers:", fg = "blue", height = 2, width = 20)
label1.pack()

entry1 = Entry(root, bg = "white", fg = "black", width = 20)
entry1.pack()
entry2 = Entry(root, bg = "white", fg = "black", width = 20)
entry2.pack()

def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    result_label.config(text = "Product: " + str(product))

button = Button(root, text = "Calculate Product", command = calculate_product)
button.pack()

result_label = Label(root, text = "Product: ", fg = "green", font = ("Sample", 14))
result_label.pack()

root.mainloop()