from tkinter import *
import password_generator

LENGTH_MIN = 20
LENGTH_MAX = 128
WINDOW = Tk()

#Label
label = Label(WINDOW, text="La longeur du mot de passe (20-128)", bg="yellow")
label.pack()

# Spin
s = Spinbox(WINDOW, from_=LENGTH_MIN, to=LENGTH_MAX)
s.pack()

WINDOW.mainloop()

