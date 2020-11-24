from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("300x300")
window.title("Lottery")
window.configure(background="pink")

def check():
    age = int(ent_age_entry.get())
    if age>=18:
        messagebox.showinfo("Qualify", "You're old enough to play the lottery!!!")
        window.withdraw()

        import LottoTask2
        LottoTask2.mainloop()

    elif age<18:
        messagebox.showerror("You Do Not Qualify", "You're too young to play the lottery.")

    enter_age_lbl.delete(0, END)
    enter_age_lbl.Entry.delete(0, END)

enter_age_lbl = Label(window, text='Enter your age:')
enter_age_lbl.grid(row=2, column=1, padx=5, pady=7)

ent_age_entry = Entry(window, borderwidth=4)
ent_age_entry.grid(row=3, column=1)

next_btn=Button(window, text="Check", command=check, bg='purple', fg='white')
next_btn.grid(row=6, column=3)


window.mainloop()