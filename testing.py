from tkinter import *
from random import sample

# Creating a window
from tkinter import *
from random import sample
import random
from datetime import *



myrandomnumbers = []


def response():
    """
    gen_num1.configure(text=str(random.sample(range(1, 49),1)))
    gen_num2.configure(text=str(random.sample(range(1, 49), 1)))
    gen_num3.configure(text=str(random.sample(range(1, 49), 1)))
    gen_num4.configure(text=str(random.sample(range(1, 49), 1)))
    gen_num5.configure(text=str(random.sample(range(1, 49), 1)))
    gen_num6.configure(text=str(random.sample(range(1, 49), 1)))
    """
    for x in range(6):
        newwrandomnumbers = random.randint(1, 49)
        myrandomnumbers.append((newwrandomnumbers))

    mylottonumbers = [int(ent_num1.get()), int(ent_num2.get()), int(ent_num3.get()), int(ent_num4.get()),
                      int(ent_num5.get()), int(ent_num6.get())]
    print(myrandomnumbers)
    gen_num1.config(text=myrandomnumbers[0])
    gen_num2.config(text=myrandomnumbers[1])
    gen_num3.config(text=myrandomnumbers[2])
    gen_num4.config(text=myrandomnumbers[3])
    gen_num5.config(text=myrandomnumbers[4])
    gen_num6.config(text=myrandomnumbers[5])
    print(mylottonumbers)
    #result = [x for x in myrandomnumbers if x in mylottonumbers]
    count=0
    for i in myrandomnumbers:
        if i in mylottonumbers:
            count+=1

    print(count)

    prizemoney = {6: "R10 000 000", 5: "R8 584", 4: "R2384", 3: "R100.50", 2: "R20", 1: "Nothing", 0: "Nothing"}
    out_lbl['text'] = "You got "+str(count)+" number(s) correct, you won "+prizemoney[count]

    today = datetime.now()
    date = today.strftime("%d %B %Y")
    time = today.strftime("%H:%M %p")


    f = open("MyFile.txt","a+")
    text = "\nDate: "+str(date)+"\nTime: "+str(time)+"\nLotto Numbers: "+str(myrandomnumbers)+"\nUser numbers: "+str(mylottonumbers)+"\nCorrect numbers: "+str(count)+"\n"
    f.write(text)
    f.close()


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



# Creating a window
window = Tk()
window.title("Play Lotto!")
window.geometry("1200x450")
window.config(background="pink")
# creating the labels
gen_num1 = Label(window, relief='groove', width=10, bd=6, text="0", fg='white', bg='black')
gen_num1.grid(row=2, column=1, padx=10, pady=9)
gen_num2 = Label(window, relief='groove', width=10, bd=6, text="0", fg='white', bg='black')
gen_num2.grid(row=2, column=2, padx=10, pady=9)
gen_num3 =Label(window, relief='groove', width=10, bd=6, text="0", fg='white', bg='black')
gen_num3.grid(row=2, column=3, padx=10, pady=9)
gen_num4 = Label(window, relief='groove', width=10, bd=6, text="0", fg='white', bg='black')
gen_num4.grid(row=2, column=4, padx=10, pady=9)
gen_num5 = Label(window, relief='groove', width=10, bd=6, text="0", fg='white', bg='black')
gen_num5.grid(row=2, column=5, padx=10, pady=9)
gen_num6 = Label(window, relief='groove', width=10, bd=6, text="0", fg='white', bg='black')
gen_num6.grid(row=2, column=6, padx=10, pady=9)

ent_num1 = Entry(window, relief='groove', width=10, bd=6, text="", fg='white', bg='black')
ent_num1.grid(row=1, column=1, padx=10, pady=9)
ent_num2 = Entry(window, relief='groove', width=10, bd=6, text="", fg='white', bg='black')
ent_num2.grid(row=1, column=2, padx=10, pady=9)
ent_num3 = Entry(window, relief='groove', width=10, bd=6, text="", fg='white', bg='black')
ent_num3.grid(row=1, column=3, padx=10, pady=9)
ent_num4 = Entry(window, relief='groove', width=10, bd=6, text="", fg='white', bg='black')
ent_num4.grid(row=1, column=4, padx=10, pady=9)
ent_num5 = Entry(window, relief='groove', width=10, bd=6, text="", fg='white', bg='black')
ent_num5.grid(row=1, column=5, padx=10, pady=9)
ent_num6 = Entry(window, relief='groove', width=10, bd=6, text="", fg='white', bg='black')
ent_num6.grid(row=1, column=6, padx=10, pady=9)

out_lbl = Label(window, bg='pink',font="Helvetica 15 bold")
out_lbl.place(x=20,y=250)#.grid(row=6, column=1)

date = datetime.now()
dlb = Label(window)
dlb.grid(row=0, column=0)
dlb.config(text="Date: " + date.strftime("%d/%m/%y %H:%M"))

# Creating a button
# Close
closeButton = Button(window)
closeButton.configure(text="CLOSE", fg='white', bg='#ff0000')
closeButton.grid(row=5, column=1, columnspan=6, pady=7)
# Generate Numbers
numberGen = Button(window, width=20, text="Generate Numbers", command=response)
numberGen.configure(fg="White", bg="Red")
numberGen.grid(row=3, column=1, padx=5, pady=7)
# Reset
reset = Button(window, width=20, text="Reset Numbers", command=die)
reset.configure(fg="White", bg="Red")
reset.grid(row=3, column=6, padx=5, pady=7)



# defining a function to close the program
def close():
    quit()
'''le=[int(ent_num1.get()),int(ent_num2.get()),int(ent_num3.get()),int(ent_num4.get()),int(ent_num5.get()),int(ent_num6.get())]'''
#lg=[int(gen_num1.get()),int(gen_num2.get()),int(gen_num3.get()),int(gen_num4.get()),int(gen_num5.get()),int(gen_num6.get())]

# attaching the "close" function to the "close" button
closeButton.configure(command=close)
'''lbl_res=Label(window,text=str(le)+"\n"+str(lg))'''

# This is the line that runs the program until you exit
window.mainloop()
