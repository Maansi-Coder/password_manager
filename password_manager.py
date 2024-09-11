import mysql.connector as sqltor
mycon= sqltor.connect(host="localhost",user="root",passwd="*****",database="password")

      
cursor=mycon.cursor()

from cryptography.fernet import Fernet   
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox as mg
window= tk.Tk()
window.title("Password Manager")
window.geometry("750x450")
window.config(bg="skyblue")

def key_generator():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet, key

def encryption(text,f):
    token = f.encrypt(text.encode()) 
    return token

def decrypt(cipher,fr):
    f=Fernet(fr)
    return f.decrypt(cipher).decode()


def Add():
    f1 = tk.Frame(window, bg="skyblue")
    f1.place(relwidth=1, relheight=1)
    
    w1= tk.Label(f1, text="Password manager", fg= "dark blue",font="Verdana 30 bold italic ",bg="skyblue")
    w1.place(relx=.5, rely=.1,anchor= "center")
    
    name_lable= tk.Label(f1, text="Username",font="Verdana 15 bold italic ",bg="skyblue")
    name_lable.place(relx=.1,rely=.3)
    
    name= tk.StringVar()
    name_entry= tk.Entry(f1, width= 30, textvariable= name)
    name_entry.place(relx=.3,rely=.32)
    
    email_lable= tk.Label(f1, text="Website",font="Verdana 15 bold italic ",bg="skyblue")
    email_lable.place(relx=.1,rely=.4)
    
    web= tk.StringVar()
    web_entry= tk.Entry(f1, width= 30, textvariable= web)
    web_entry.place(relx=.3,rely=.42)
    
    pswd_lable= tk.Label(f1, text="Password",font="Verdana 15 bold italic ",bg="skyblue")
    pswd_lable.place(relx=.1,rely=.5)
    
    pswd= tk.StringVar()
    pswd_entry= tk.Entry(f1, width= 30, textvariable= pswd)
    pswd_entry.place(relx=.3,rely=.52)
    
    def add():
        un = name.get()
        wb = web.get()
        fernet, key = key_generator()
        encrypted_password = encryption(pswd.get(), fernet)
        
        query = "INSERT INTO pwd (username, email, password, pwd_key) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (un, wb, encrypted_password, key))
        mycon.commit()
        
        mg.showinfo("Success", "Added successfully")
        
    
    add_btn=tk.Button(f1, text= "Add Password", font="Verdana 15 bold italic ",relief="ridge",command= add)
    add_btn.place(relx=.7, rely=.7)
    
    back_btn=tk.Button(f1, text= "Back", font="Verdana 15 bold italic ")
    back_btn.place(relx=.8, rely=.8)
    
def Show():
    f1 = tk.Frame(window, bg="skyblue")
    f1.place(relwidth=1, relheight=1)
    
    w1= tk.Label(f1, text="Password manager", fg= "dark blue",font="Verdana 30 bold italic ",bg="skyblue")
    w1.place(relx=.5, rely=.1,anchor= "center")
    
    name_lable= tk.Label(f1, text="Username",font="Verdana 15 bold italic ",bg="skyblue")
    name_lable.place(relx=.1,rely=.3)
    
    name= tk.StringVar()
    name_entry= tk.Entry(f1, width= 30, textvariable= name)
    name_entry.place(relx=.3,rely=.32)
    
    email_lable= tk.Label(f1, text="Website",font="Verdana 15 bold italic ",bg="skyblue")
    email_lable.place(relx=.1,rely=.4)
    
    web= tk.StringVar()
    web_entry= tk.Entry(f1, width= 30, textvariable= web)
    web_entry.place(relx=.3,rely=.42)
    
    def show():
        un = name.get()
        wb = web.get()
        
        
        query = "Select * from pwd where username='"+str(un)+"' and email='"+str(wb)+"'"
        cursor.execute(query)
        result=cursor.fetchone()
        if result:
            encrypted_password = result[2].encode()
            key = result[3].encode()
            pwd = decrypt(encrypted_password, key)
            mg.showinfo("Password", f"The password is: {pwd}")
        else:
            mg.showerror("Error", "No matching record found")
        
    
    add_btn=tk.Button(f1, text= "Show Password", font="Verdana 15 bold italic ",relief="ridge",command= show)
    add_btn.place(relx=.7, rely=.7)
    
    back_btn=tk.Button(f1, text= "Back", font="Verdana 15 bold italic ")
    back_btn.place(relx=.8, rely=.8)


Intro= tk.Label(window, text="Password manager", fg= "dark blue",font="Verdana 30 bold italic ",bg="skyblue")

Intro.place(relx=.5, rely=.1,anchor= "center")

add_btn=tk.Button(window, text= "Add Password", font="Verdana 15 bold italic ",relief="ridge",command= Add)
add_btn.place(relx=.15, rely=.45)

get_btn=tk.Button(window, text= "Get Password", font="Verdana 15 bold italic ",relief="ridge",command= Show)
get_btn.place(relx=.6, rely=.45)


    

window.mainloop()
mycon.close()


