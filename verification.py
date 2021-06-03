from tkinter import *
from tkinter import messagebox


def clear_entry():

    accountentry.delete(0, 'end')


def qualify():
    amount = accountentry.get()
    try:
        amount = int(amount)
        if amount > 3000:
            messagebox.showinfo("feedback", "congragulations! you qualify for maleysia")
        else:
            messagebox.showinfo("feedback", "Sorry you don't qualify for maleysia")
    except ValueError:
        messagebox.showinfo("Error", "please enter amount as number")







def exit():
    mgbox=messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        root.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")
root = Tk()
root.title("log in")
root.geometry("500x400")

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

lblaccont = Label(frame, text=" please enter amount in your account")
lblaccont.grid(row=1, column=1)

accountentry = Entry(frame,)
accountentry.grid(row=2, column=1, pady=5)


reset_btn = Button(frame, text='clear', bg='#346ab3', command=clear_entry)
reset_btn.grid(row=3, column=2, pady=2)
exit_btn = Button(frame, text='Exit', bg='#346ab3', command=exit)
exit_btn.grid(row=3, column=3, pady=2)

cal_btn = Button(frame, text='check qualification', bg='#346ab3', command=qualify)
cal_btn.grid(row=3, column=1, pady=2)


root.mainloop()