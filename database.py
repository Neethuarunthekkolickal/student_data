from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql
root= Tk()
root.geometry("500x500")
root.title("Application")
def save():
    regno=txt1.get()
    name=txt2.get()
    address=txt3.get()
    phone=txt4.get()
    if regno=='' or name=='' or address=='' or phone=='':
        messagebox.showinfo("Insert Data","Please fill all feilds.")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='mkd123')
        cursor=conn.cursor()
        cursor.execute("insert into student values('%s','%s','%s','%s')"%(regno,name,address,phone))
        conn.commit()
        messagebox.showinfo("Insert Status","Inserted Successfully")
        txt1.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        txt4.delete(0,END)
        cursor.close()
        conn.close()
def delete():
    regno=txt1.get()
    if regno =='':
        messagebox.showinfo("Insert Data","Please enter your register number.")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='mkd123')
        cursor=conn.cursor()
        cursor.execute("delete from student where regno='%s'"%regno)
        conn.commit()
        messagebox.showinfo("Delete Status","Deleted Successfully")
        txt1.delete(0,END)
        cursor.close()
        conn.close()
def edit():
    regno=txt1.get()
    name=txt2.get()
    address=txt3.get()
    phone=txt4.get()
    if regno=='' or name=='' or address=='' or phone=='':
        messagebox.showinfo("Insert Data","Please fill all feilds.")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='mkd123')
        cursor=conn.cursor()
        cursor.execute("update student set name='%s', address='%s', phone='%s' where regno='%s'"%(name,address,phone,regno))
        conn.commit()
        messagebox.showinfo("Update Status","Updated Successfully")
        txt1.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        txt4.delete(0,END)
        cursor.close()
        conn.close()
def show():
    regno=txt1.get()
    if regno =='':
        messagebox.showinfo("Insert Data","Please enter your register number.")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='mkd123')
        cursor=conn.cursor()
        cursor.execute("select *from student where regno='%s'"%regno)
        rows=cursor.fetchall()
        for result in rows:
            txt2.insert(0,result[1])
            txt3.insert(0,result[2])
            txt4.insert(0,result[3])

lbl=Label(text="Register No:")
lbl.place(x=50,y=50)
lbl2=Label(text="Name :")
lbl2.place(x=50,y=100)
lbl3=Label(text="Address:")
lbl3.place(x=50,y=150)
lbl4=Label(text="Phone No:")
lbl4.place(x=50,y=200)
txt1=Entry()
txt1.place(x=200,y=50)
txt2=Entry()
txt2.place(x=200,y=100)
txt3=Entry()
txt3.place(x=200,y=150)
txt4=Entry()
txt4.place(x=200,y=200)
btn1=Button(text="Save", command=save)
btn1.place(x=200,y=250)
btn2=Button(text="Delete",command=delete)
btn2.place(x=250,y=250)
btn3=Button(text="Edit",command=edit)
btn3.place(x=300,y=250)
btn4=Button(text="Show",command=show)
btn4.place(x=350,y=250)
root.mainloop()from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql
root= Tk()
root.geometry("500x500")
root.title("Application")
def save():
    regno=txt1.get()
    name=txt2.get()
    address=txt3.get()
    phone=txt4.get()
    if regno=='' or name=='' or address=='' or phone=='':
        messagebox.showinfo("Insert Data","Please fill all feilds.")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='mkd123')
        cursor=conn.cursor()
        cursor.execute("insert into student values('%s','%s','%s','%s')"%(regno,name,address,phone))
        conn.commit()
        messagebox.showinfo("Insert Status","Inserted Successfully")
        txt1.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        txt4.delete(0,END)
        cursor.close()
        conn.close()
def delete():
    regno=txt1.get()
    if regno =='':
        messagebox.showinfo("Insert Data","Please enter your register number.")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='mkd123')
        cursor=conn.cursor()
        cursor.execute("delete from student where regno='%s'"%regno)
        conn.commit()
        messagebox.showinfo("Delete Status","Deleted Successfully")
        txt1.delete(0,END)
        cursor.close()
        conn.close()
def edit():
    regno=txt1.get()
    name=txt2.get()
    address=txt3.get()
    phone=txt4.get()
    if regno=='' or name=='' or address=='' or phone=='':
        messagebox.showinfo("Insert Data","Please fill all feilds.")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='mkd123')
        cursor=conn.cursor()
        cursor.execute("update student set name='%s', address='%s', phone='%s' where regno='%s'"%(name,address,phone,regno))
        conn.commit()
        messagebox.showinfo("Update Status","Updated Successfully")
        txt1.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        txt4.delete(0,END)
        cursor.close()
        conn.close()
def show():
    regno=txt1.get()
    if regno =='':
        messagebox.showinfo("Insert Data","Please enter your register number.")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='mkd123')
        cursor=conn.cursor()
        cursor.execute("select *from student where regno='%s'"%regno)
        rows=cursor.fetchall()
        for result in rows:
            txt2.insert(0,result[1])
            txt3.insert(0,result[2])
            txt4.insert(0,result[3])

lbl=Label(text="Register No:")
lbl.place(x=50,y=50)
lbl2=Label(text="Name :")
lbl2.place(x=50,y=100)
lbl3=Label(text="Address:")
lbl3.place(x=50,y=150)
lbl4=Label(text="Phone No:")
lbl4.place(x=50,y=200)
txt1=Entry()
txt1.place(x=200,y=50)
txt2=Entry()
txt2.place(x=200,y=100)
txt3=Entry()
txt3.place(x=200,y=150)
txt4=Entry()
txt4.place(x=200,y=200)
btn1=Button(text="Save", command=save)
btn1.place(x=200,y=250)
btn2=Button(text="Delete",command=delete)
btn2.place(x=250,y=250)
btn3=Button(text="Edit",command=edit)
btn3.place(x=300,y=250)
btn4=Button(text="Show",command=show)
btn4.place(x=350,y=250)
root.mainloop()