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

def die():
    gen_num1.configure(text=str(0))
    gen_num2.configure(text=str(0))
    gen_num3.configure(text=str(0))
    gen_num4.configure(text=str(0))
    gen_num5.configure(text=str(0))
    gen_num6.configure(text=str(0))





#Creating a window
window = Tk()
window.title("Play Lotto!")
window.geometry("500x250")
window.config(background="pink")
#creating the labels
gen_num1 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='black')
gen_num1.grid(row = 1, column = 1, padx = 5, pady = 7)
gen_num2 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='black')
gen_num2.grid(row = 1, column = 2, padx = 5, pady = 7)
gen_num3 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='black')
gen_num3.grid(row = 1, column = 3, padx = 5, pady = 7)
gen_num4 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='black')
gen_num4.grid(row = 1, column = 4, padx = 5, pady = 7)
gen_num5 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='black')
gen_num5.grid(row = 1, column = 5, padx = 5, pady = 7)
gen_num6 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='black')
gen_num6.grid(row = 1, column = 6, padx = 5, pady = 7)



#Creating a button
#Close
closeButton = Button(window)
closeButton.configure(text = "CLOSE", fg = 'white', bg = '#ff0000')
closeButton.grid(row = 3, column = 1, columnspan = 6, pady = 7)
#Generate Numbers
numberGen = Button(window, width=20, text="Generate Numbers", command=response)
numberGen.configure(fg = "White" ,bg = "Red")
numberGen.grid(row = 2, column = 1, padx = 5, pady = 7)
#Reset
reset = Button(window, width=10, text="Reset", command =die)
reset.configure(fg = "White" ,bg = "Red")
reset.grid(row = 2, column = 2, padx = 5, pady = 7)

#defining a function to close the program
def close():
    quit()



#attaching the "close" function to the "close" button
closeButton.configure(command = close)

#This is the line that runs the program until you exit
window.mainloop()


