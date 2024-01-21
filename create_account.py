from tkinter import *
import tkinter as tk
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="1a_marba"
)

cursor = db.cursor()

class CreateAcc:
    def __init__(self):
        self.root = tk.Tk()
        self.username = ""
        self.password = ""
        self.gmail = ""
        self.font = ("cooper black",11,"bold")

    def enternames(self):
        self.root.geometry("500x500")
        self.root.configure(bg='aqua')
        self.root.title('enter a name')







        self.labelname = tk.Label(
            self.root,
            text="Username",
            fg="green",
            bg="black",
            font=self.font


            )
        self.labelname.pack(padx=100,pady=10)
        self.entry1 = tk.Entry(self.root,width=50)
        self.entry1.pack()

        self.passlabel = tk.Label(
            self.root,
            text="Password",
            fg="green",
            bg="black",
            font=self.font


            )
        self.passlabel.pack(padx=100,pady=10)
        self.entry2 = tk.Entry(self.root,width=50)
        self.entry2.pack()

        self.gmaillabel = Label(self.root,text="email Account",font=self.font,fg='green',bg='black').pack()
        self.entry3 = tk.Entry(self.root,width=50)
        self.entry3.pack()

        def save():

            self.username = self.entry1.get()
            self.password = self.entry2.get()
            self.gmail = self.entry3.get()

            return self.username and self.password and self.gmail





        self.button = Button(self.root,text="save",command=save,font=self.font,fg='green',bg='black').pack()



        self.root.mainloop()



        cursor.execute("INSERT INTO `create_account`(`username`, `password`,`gmail`) VALUES (%s, %s, %s)",
                       (self.username, self.password,self.gmail))
        db.commit()
        print('succesfuly added in database')





p=CreateAcc()
p.enternames()



