from tkinter import *

import mysql.connector

import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_10"
        )

print(create_conn())

def insert_data():
    if e_name.get()=="" or e_contact.get()=="" or e_email.get()=="" or e_dep.get()=="" or e_jobrol.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into employee(name, contact, email, dep, jobrol) values(%s,%s,%s,%s,%s)"
        args=(e_name.get(),e_contact.get(),e_email.get(),e_dep.get(),e_jobrol.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_name.delete(0,'end')
        e_contact.delete(0,'end')
        e_email.delete(0,'end')
        e_dep.delete(0,'end')
        e_jobrol.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")
        

def search_data():
    e_name.delete(0,'end')
    e_contact.delete(0,'end')
    e_email.delete(0,'end')
    e_dep.delete(0,'end')
    e_jobrol.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("Search Status","Id is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from employee where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            e_name.insert(0,row[0][1])
            e_contact.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_dep.insert(0,row[0][4])
            e_jobrol.insert(0,row[0][5])
        else:
            msg.showinfo("Search Status","Id Not Found")
        conn.close()
        #msg.showinfo("Insert Status","Data Inserted Successfully")

def update_data():
    if e_id.get()=="" or e_name.get()=="" or e_contact.get()=="" or e_email.get()=="" or e_dep.get()=="" or e_jobrol.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update employee set name=%s, contact=%s, email=%s, dep=%s, jobrol=%s where id=%s"
        args=(e_name.get(),e_contact.get(),e_email.get(),e_dep.get(),e_jobrol.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_name.delete(0,'end')
        e_contact.delete(0,'end')
        e_email.delete(0,'end')
        e_dep.delete(0,'end')
        e_jobrol.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","Id is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from employee where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_name.delete(0,'end')
        e_contact.delete(0,'end')
        e_email.delete(0,'end')
        e_dep.delete(0,'end')
        e_jobrol.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")


root=Tk()
root.geometry("440x500")
root.title("Employee DataBase")
root.resizable(width=False, height=False)

l_id=Label(root, text="ID")
l_id.place(x=50, y=50)

l_name=Label(root, text="Employee Name")
l_name.place(x=50, y=100)

l_contact=Label(root, text="Contact")
l_contact.place(x=50, y=150)

l_email=Label(root, text="Email")
l_email.place(x=50, y=200)

l_dep=Label(root, text="Department")
l_dep.place(x=50, y=250)

l_jobrol=Label(root, text="Job Title")
l_jobrol.place(x=50, y=300)

#Text box

e_id=Entry(root)
e_id.place(x=200, y=50)

e_name=Entry(root)
e_name.place(x=200, y=100)

e_contact=Entry(root)
e_contact.place(x=200, y=150)

e_email=Entry(root)
e_email.place(x=200, y=200)

e_dep=Entry(root)
e_dep.place(x=200, y=250)

e_jobrol=Entry(root)
e_jobrol.place(x=200, y=300)

insert=Button(root, text="INSERT", bg="aqua", fg="green", font=("Roboto", 12), command=insert_data)
insert.place(x=51, y=350)

search=Button(root, text="SEARCH", bg="aqua", fg="green", font=("Roboto", 12), command=search_data)
search.place(x=125, y=350)

update=Button(root, text="UPDATE", bg="aqua", fg="green", font=("Roboto", 12), command=update_data)
update.place(x=205, y=350)

delete=Button(root, text="DELETE", bg="aqua", fg="green", font=("Roboto", 12), command=delete_data)
delete.place(x=285, y=350)
