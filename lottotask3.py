from tkinter import *
from random import sample

#Creating a window
from tkinter import *
from random import sample
import random

def response():
    gen_num1.configure(text=str(random.sample(range(1, 49),1)))
    gen_num2.configure(text=str(random.sample(range(1, 49), 1)))
    gen_num3.configure(text=str(random.sample(range(1, 49), 1)))
    gen_num4.configure(text=str(random.sample(range(1, 49), 1)))
    gen_num5.configure(text=str(random.sample(range(1, 49), 1)))
    gen_num6.configure(text=str(random.sample(range(1, 49), 1)))
    myrandomnumbers=[]
    myrandomnumbers.append[gen_num1, gen_num2, gen_num3,gen_num4,gen_num5,gen_num6]
    mylottonumbers = [int(ent_num1.get()), int(ent_num2.get()),int(ent_num3.get()), int(ent_num4.get()), int(ent_num5.get()),int(ent_num6.get())]
    print(myrandomnumbers)
    print(mylottonumbers)

def die():
    gen_num1.configure(text=str(0))
    gen_num2.configure(text=str(0))
    gen_num3.configure(text=str(0))
    gen_num4.configure(text=str(0))
    gen_num5.configure(text=str(0))
    gen_num6.configure(text=str(0))

    ent_num1.delete(0, END)
    ent_num2.delete(0, END)
    ent_num3.delete(0, END)
    ent_num4.delete(0, END)
    ent_num5.delete(0, END)
    ent_num6.delete(0, END)

def check():
    import LottoTask2
    LottoTask2.mainloop()



#Creating a window
window = Tk()
window.title("Play Lotto!")
window.geometry("850x450")
window.config(background="pink")
#creating the labels
gen_num1 = Label(window, relief='groove', width = 10, bd=6, text="0", fg='white', bg='black')
gen_num1.grid(row = 2, column = 1, padx = 10, pady = 9)
gen_num2 = Label(window, relief='groove', width = 10, bd=6, text="0", fg='white', bg='black')
gen_num2.grid(row = 2, column = 2, padx = 10, pady = 9)
gen_num3 = Label(window, relief='groove', width = 10, bd=6, text="0", fg='white', bg='black')
gen_num3.grid(row = 2, column = 3, padx = 10, pady = 9)
gen_num4 = Label(window, relief='groove', width = 10, bd=6, text="0", fg='white', bg='black')
gen_num4.grid(row = 2, column = 4, padx = 10, pady = 9)
gen_num5 = Label(window, relief='groove', width = 10, bd=6, text="0", fg='white', bg='black')
gen_num5.grid(row = 2, column = 5, padx = 10, pady = 9)
gen_num6 = Label(window, relief='groove', width = 10, bd=6, text="0", fg='white', bg='black')
gen_num6.grid(row = 2, column = 6, padx = 10, pady = 9)

ent_num1 = Entry(window, relief='groove', width = 10, bd=6, text="", fg='white', bg='black')
ent_num1.grid(row = 1, column = 1, padx = 10, pady = 9)
ent_num2 = Entry(window, relief='groove', width = 10, bd=6, text="", fg='white', bg='black')
ent_num2.grid(row = 1, column = 2, padx = 10, pady = 9)
ent_num3 = Entry(window, relief='groove', width = 10, bd=6, text="", fg='white', bg='black')
ent_num3.grid(row = 1, column = 3, padx = 10, pady = 9)
ent_num4 = Entry(window, relief='groove', width = 10, bd=6, text="", fg='white', bg='black')
ent_num4.grid(row = 1, column = 4, padx = 10, pady = 9)
ent_num5 = Entry(window, relief='groove', width = 10, bd=6, text="", fg='white', bg='black')
ent_num5.grid(row = 1, column = 5, padx = 10, pady = 9)
ent_num6 = Entry(window, relief='groove', width = 10, bd=6, text="", fg='white', bg='black')
ent_num6.grid(row = 1, column = 6, padx = 10, pady = 9)



#Creating a button
#Close
closeButton = Button(window)
closeButton.configure(text = "CLOSE", fg = 'white', bg = '#ff0000')
closeButton.grid(row = 5, column = 6, columnspan = 6, pady = 7)
#Generate Numbers
numberGen = Button(window, width=20, text="Generate Numbers", command=response)
numberGen.configure(fg = "White" ,bg = "Red")
numberGen.grid(row = 3, column = 1, padx = 5, pady = 7)
#Reset
reset = Button(window, width=20, text="Reset Numbers", command =die)
reset.configure(fg = "White" ,bg = "Red")
reset.grid(row = 3, column = 6, padx = 5, pady = 7)

check_btn = Button(window, command=check)
check_btn.configure(text = "Check Results", fg = 'white', bg = '#ff0000')
check_btn.grid(row = 5, column = 1, padx = 5, pady = 7)

#defining a function to close the program
def close():
    quit()



#attaching the "close" function to the "close" button
closeButton.configure(command = close)

#This is the line that runs the program until you exit
window.mainloop()


