from tkinter import *

window = Tk()
window.title("Practice Question No:02")
window.geometry("500x200")
#window.maxsize(540, 200)
#$window.minsize(300, 200)

var1 = IntVar()
var1.set(0)

var2 = IntVar()
var2.set(0)

var3 = IntVar()
var3.set(0)


def add():
    var3.set(var1.get() + var2.get())


def sub():
    var3.set(var1.get() - var2.get())


def mul():
    var3.set(var1.get() * var2.get())


def div():
    var3.set(var1.get() / var2.get())


label1 = Label(window, text="Enter First No:", bg="orange", fg="black", font=("Times New Roman", 20))
label1.grid(column=0, row=0)

txtbox1 = Entry(window, textvariable=var1, font=("Times New Roman", 15), bg="yellow", fg="blue", width=20)
txtbox1.grid(column=1, row=0)

label2 = Label(window, text="Enter Second No:", bg="orange", fg="black", font=("Times New Roman", 20))
label2.grid(column=0, row=1)

txtbox2 = Entry(window, textvariable=var2, font=("Times New Roman", 15), bg="yellow", fg="blue", width=20)
txtbox2.grid(column=1, row=1)

label3 = Label(window, textvariable=var3, text="Wait for the Answer:", bg="cyan", fg="red",
               font=("Times New Roman", 20))
label3.grid(column=0, row=2)

btnadd = Button(window, text="Addition", font=("Times New Roman", 15), bg="black", fg="white", command=add)
btnadd.grid(column=0, row=4)

btndel = Button(window, text="Subtraction", font=("Times New Roman", 15), bg="black", fg="white", command=sub)
btndel.grid(column=1, row=4)

btnmul = Button(window, text="Multiplication", font=("Times New Roman", 15), bg="black", fg="white", command=mul)
btnmul.grid(column=0, row=5)

btndiv = Button(window, text="Division", font=("Times New Roman", 15), bg="black", fg="white", command=div)
btndiv.grid(column=1, row=5)


window.mainloop()
