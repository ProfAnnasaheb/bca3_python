from tkinter import *

def login():
    uid = txtbox1.get()
    password = txtbox2.get()
    label_result.config(text=f"Login ID: {uid}, Password: {password}")
    
window = Tk()
window.title("Login Form")
window.geometry("500x200")
label1 = Label(window, text="Enter login ID:", bg="cyan", fg="black", font=("Times New Roman", 20))
label1.grid(column=0, row=0)
txtbox1 = Entry(window, font=("Times New Roman", 15), bg="yellow", fg="blue", width=20)
txtbox1.grid(column=1, row=0)
label2 = Label(window, text="Password:", bg="cyan", fg="black", font=("Times New Roman", 20))
label2.grid(column=0, row=1)
txtbox2 = Entry(window, font=("Times New Roman", 15), bg="yellow", fg="blue", width=20)
txtbox2.grid(column=1, row=1)
btnadd = Button(window, text="Login", font=("Times New Roman", 15), bg="black", fg="white", command=login)
btnadd.grid(column=1, row=3)
label_result = Label(window, text="Type Inputs", bg="cyan", fg="black", font=("Times New Roman", 16))
label_result.grid(column=0, row=4, columnspan=2)
window.mainloop()
