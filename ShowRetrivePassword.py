from tkinter import *


def showPasswords(passwordCollection):
    root2 = Tk()

    labelYourPaswords = Label(root2, text="Your Stored Passwords are:", font=(
        'arial', 20, 'bold'), fg='black')

    labelShowPasswords = Label(
        root2, text=passwordCollection, font=('arial', 12, ), fg='red')

    labelYourPaswords.grid(row=0, column=1)
    labelShowPasswords.grid(row=1, column=1)

    root2.mainloop()
