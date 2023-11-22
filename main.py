from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

label = Label(text="My First GUI Program", font=("Arial", 50))
label.config(text="My Text is changed")
label.pack()

entry = Entry(width=30)
entry.insert(END, string="Something to type")
print(entry.get())
entry.pack()

def action():
    print("Do Something")

button = Button(text="CLick Me", command=action)
button.pack()


window.mainloop()