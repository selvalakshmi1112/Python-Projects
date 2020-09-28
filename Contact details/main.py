from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

def login():

    username=usrentry.get()
    password=pasentry.get()
    if(username=="" or password==""):
        MessageBox.showinfo("Insert status","All fields are require")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="logindetails")
        cursor=con.cursor()
        cursor.execute("insert into  loginids values('"+username+"','"+password+"')")
        cursor.execute("commit")

        usrentry.delete(0,'end')
        pasentry.delete(0,'end')

        MessageBox.showinfo("login Status","login sucess")
        con.close()
root=Tk()
root.configure(background = "purple")
root.title("login form")
root.geometry("250x150")

usr=Label(root, text="username")
usr.grid(row = 0, column = 0)

usrentry=Entry(root)
usrentry.grid(row = 0, column = 1)

pas=Label(root ,text="password")
pas.grid(row = 1, column = 0)

pasentry=Entry(root,show="*")
pasentry.grid(row = 1 , column = 1)

submit = Button(root, text = "submit", command=login )
submit.grid(row = 3,column = 1)

root.mainloop()