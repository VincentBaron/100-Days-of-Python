from tkinter import *

FONT = ("Arial", 24, "bold")

window = Tk()
window.title("My First window")
window.minsize(500, 500)
my_label = Label(text="I am a Label", font=FONT)
my_label.pack()


def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)
    print("I got clicked")


entry = Entry(width=10)
entry.pack()

button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
