from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")

def greet():
    print("\nHello, World!")

button = Button(window, text = "Click Me!")
button.pack()
button.bind("<Button-1>", handle_click)
Button1 = Button(window, text = "Click Me Too!", command = greet)
Button1.pack()

window.mainloop()