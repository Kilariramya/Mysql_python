import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
class log:
    def __init__(self):
        pass
    def mainn(self):
        global window
        window=Tk()
        window.geometry("400x400")
        window.title("HCL EMP SYSTEM")
        menubar=Menu(window)
menubar.add_command(label="Login",command=self.main1)
menubar.add_command(label="Newuser",command=self.main2)
menubar.add_command(label="Search",command=self.main3)
    window.config(menu=menubar)
    window.mainloop()
    def connection(self,user,passw):
        conn=mysql.connector.connect(host='localhost',user='root',password='password',port=3306,db='hcl')
        query="select id from login where username=%s and password=%s"
        vals=(user,passw)
        cur=conn.cursor(prepared,vals)
        result=cur.fetchone()
        cur.close()
        conn.close()
        return result
    def check(self):
        self.u_name=un.get()
        self.pass_word=pw.get()
        data=self.connection(self.u_name,self.pass_word)
        #print(data)
        #print(data[0])
        if data is not None:
            messagebox.showinfo(title="Hello user",message="Welcome")
        else:
            messagebox.showinfo(title="Hello user",message="Welcome")

