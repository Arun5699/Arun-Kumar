from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector as mc

win=Tk()
win.title('Library Management System')
win.geometry('1000x500')

# image intro
#-------------
library = ImageTk.PhotoImage(Image.open("C:\Python310\library images\pexels-karol-d-333304.jpg")) 
p1 = Label(win, image = library)
p1.pack(side = "left", fill = "both")

# frame intro
#--------------
frame = Frame(win,bg="#FFBB00")
frame.place(x = 250,y = 50,width = 500,height = 100)

# label intro
#-------------
l1=Label(win,text='  Welcom to \n Arun Library',bg='black', fg='white', font=('Courier',15))
l1.place(x=275,y=60,width=450,height=80)


# add book
#-----------

def add_book():

    win=Tk()
    win.title('Add book')
    win.geometry('800x600')
    win.config(bg="#ff6e40")

    # frame intro
    #--------------
    frame = Frame(win,bg="#FFBB00")
    frame.place(x = 150,y = 50,width = 500,height = 100)

    f1=Frame(win,bg='black')
    f1.place(x=50,y=200,width=700,height=280)

    # label intro
    #-------------
    l1=Label(win,text='Add Books',bg='black', fg='white', font=('Courier',15))
    l1.place(x=175,y=60,width=450,height=80)
    l2=Label(f1,text='Book ID',bg='black', fg='white', font=('Cambria',14))
    l2.place(x=100,y=50)
    l3=Label(f1,text='Book Name',bg='black', fg='white', font=('Cambria',14))
    l3.place(x=100,y=100)
    l4=Label(f1,text='Author',bg='black', fg='white', font=('Cambria',14))
    l4.place(x=100,y=150)
    l5=Label(f1,text='Price',bg='black', fg='white', font=('Cambria',14))
    l5.place(x=100,y=200)

    # entry intro
    #-------------
    e1=Entry(f1,width=30,font=('Courier',14))
    e1.place(x=300,y=50)
    e2=Entry(f1,width=30,font=('Courier',14))
    e2.place(x=300,y=100)
    e3=Entry(f1,width=30,font=('Courier',14))
    e3.place(x=300,y=150)
    e4=Entry(f1,width=30,font=('Courier',14))
    e4.place(x=300,y=200)

    #book register
    #--------------
    def submit():
        if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent = win)
        else:
            book_id = e1.get()
            book_name = e2.get()
            author = e3.get()
            price = e4.get()
            conn = mc.connect(host = "localhost", user = "root" , password = "" , database = "lms")
            cursor = conn.cursor()
            cursor.execute("insert into library (Book_id,Book_name,Author,Price) values('"+book_id+"', '"+book_name+"', '"+author+"', '"+price+"')")
            conn.close()
            messagebox.showinfo("Congratulations!","Book Added Successful",parent= win)

    b1=Button(win,text='SUBMIT',bg='#d1ccc0', fg='black', font=('Courier',15),command=submit)
    b1.place(x=200,y=500)
    b2=Button(win,text='QUIT',bg='#d1ccc0', fg='black', font=('Courier',15))
    b2.place(x=500,y=500,width=90)


b1=Button(win,text='Add Books Details',font=('times new roman',14,'bold'),bg="#00ff80",command=add_book)
b1.place(x=350,y=200,width=300,height=50)


# view books
#------------

def v_book():

    connect = mc.connect(host = "localhost", user = "root", password="", database = "lms")
    cursor = connect.cursor()
    cursor.execute("select * from library;")
    connect.close()
    view = cursor.fetchone()
    print('....................  VIEW BOOKS ....................')
    print(view)
    messagebox.showinfo("Congratulations!","Successful Published Your Book List",parent=win)


b2=Button(win,text='View Book List',font=('times new roman',14,'bold'),bg="#00ff80",command = v_book)
b2.place(x=350,y=250,width=300,height=50)

# issue book
#------------

def issue():
    win=Tk()
    win.title('issue book')
    win.geometry('800x600')
    win.config(bg='cyan')

    # frame intro
    #--------------
    frame = Frame(win,bg='white')
    frame.place(x = 150,y = 50,width = 500,height = 100)

    f1=Frame(win,bg='black')
    f1.place(x=50,y=200,width=700,height=250)

    # label intro
    #-------------
    l1=Label(win,text='Issue Book',bg='black', fg='white', font=('Courier',15))
    l1.place(x=175,y=60,width=450,height=80)
    l2=Label(f1,text='Book ID',bg='black', fg='white', font=('Cambria',14))
    l2.place(x=100,y=50)
    l3=Label(f1,text='Student Name',bg='black', fg='white', font=('Cambria',14))
    l3.place(x=100,y=100)
    l4=Label(f1,text='Department',bg='black', fg='white', font=('Cambria',14))
    l4.place(x=100,y=150)

    # entry intro
    #-------------
    e1=Entry(f1,width=30,font=('Courier',14))
    e1.place(x=300,y=50)
    e2=Entry(f1,width=30,font=('Courier',14))
    e2.place(x=300,y=100)
    e3=Entry(f1,width=30,font=('Courier',14))
    e3.place(x=300,y=150)
    

    def issue_book():
        if e1.get()=="":
            messagebox.showerror("Error!","Please Enter Your Book ID",parent=win)
        elif e1.get()==None:
            messagebox.showerror("Error!","Can't fetch Book IDs",parent=win)
        else:
            connection = mc.connect(host="localhost", user="root", password="", database="lms")
            cur = connection.cursor()
            cur.execute("select * from library where Book_id ='"+e1.get()+"'")
            connection.close()
            book_id = cur.fetchone()
            messagebox.showinfo("Success","Book Issued successfully",parent=win)
            
             
    b1=Button(win,text='ISSUE',bg='#80ff00', fg='black', font=('Courier',15),command=issue_book)
    b1.place(x=200,y=500)
    b2=Button(win,text='QUIT',bg='#80ff00', fg='black', font=('Courier',15))
    b2.place(x=500,y=500,width=90)
        
        
    
b3=Button(win,text='Issuse Book to Student',font=('times new roman',14,'bold'),bg="#00ff80",command=issue)
b3.place(x=350,y=300,width=300,height=50)

# return book
#-------------
def re_turn():
    
    win=Tk()
    win.title('return book')
    win.geometry('800x600')
    win.config(bg='cyan')

    # frame intro
    #--------------
    frame = Frame(win,bg='white')
    frame.place(x = 150,y = 50,width = 500,height = 100)

    f1=Frame(win,bg='black')
    f1.place(x=50,y=200,width=700,height=250)

    # label intro
    #-------------
    l1=Label(win,text='Return Book',bg='black', fg='white', font=('Courier',15))
    l1.place(x=175,y=60,width=450,height=80)
    l2=Label(f1,text='Book ID',bg='black', fg='white', font=('Cambria',14))
    l2.place(x=100,y=50)
    l3=Label(f1,text='Student Name',bg='black', fg='white', font=('Cambria',14))
    l3.place(x=100,y=100)
    l4=Label(f1,text='Department',bg='black', fg='white', font=('Cambria',14))
    l4.place(x=100,y=150)

    # entry intro
    #-------------
    e1=Entry(f1,width=30,font=('Courier',14))
    e1.place(x=300,y=50)
    e2=Entry(f1,width=30,font=('Courier',14))
    e2.place(x=300,y=100)
    e3=Entry(f1,width=30,font=('Courier',14))
    e3.place(x=300,y=150)
    
    def return_book():
        if e1.get()=="":
            messagebox.showerror("Error!","Please Enter Your Book ID",parent=win)
        else:
            connection = mc.connect(host="localhost", user="root", password="", database="lms")
            cur = connection.cursor()
            cur.execute("select * from library where Book_id ='"+e1.get()+"'")
            connection.close()
            book_id = cur.fetchone()
            messagebox.showinfo("Success","Successful Returned Your Book",parent=win)
            

    b1=Button(win,text='RETURN',bg='#80ff00', fg='black', font=('Courier',15),command=return_book)
    b1.place(x=200,y=500)
    b2=Button(win,text='QUIT',bg='#80ff00', fg='black', font=('Courier',15))
    b2.place(x=500,y=500,width=90)
        
    
b4=Button(win,text='Return Book',font=('times new roman',14,'bold'),bg="#00ff80",command=re_turn)
b4.place(x=350,y=350,width=300,height=50)    


# delete book
#-------------

def delete():

    win=Tk()
    win.title('return book')
    win.geometry('800x500')
    win.config(bg='cyan')

    # frame intro
    #--------------
    frame = Frame(win,bg='white')
    frame.place(x = 150,y = 50,width = 500,height = 100)

    f1=Frame(win,bg='black')
    f1.place(x=50,y=200,width=700,height=150)

    # label intro
    #-------------
    l1=Label(win,text='Delete Book',bg='black', fg='white', font=('Courier',15))
    l1.place(x=175,y=60,width=450,height=80)
    l2=Label(f1,text='Book ID',bg='black', fg='white', font=('Cambria',14))
    l2.place(x=100,y=50)

    # entry intro
    #-------------
    e1=Entry(f1,width=30,font=('Courier',14))
    e1.place(x=300,y=50)

    def delete_book():
        if e1.get()=="":
            messagebox.showerror("Error!","Please Enter Your Book ID",parent=win)
        elif e1.get()==None:
            messagebox.showerror("Error!","Can't fetch Book IDs",parent=win)
        else:
            connection = mc.connect(host="localhost", user="root", password="", database="lms")
            cur = connection.cursor()
            cur.execute("delete from library where Book_id ='"+e1.get()+"'")
            connection.close()
            book_id = cur.fetchone()
            messagebox.showinfo("Success","Book Deleted successfully",parent=win)

    b1=Button(win,text='SUBMIT',bg='#80ff00', fg='black', font=('Courier',15),command=delete_book)
    b1.place(x=200,y=400)
    b2=Button(win,text='QUIT',bg='#80ff00', fg='black', font=('Courier',15))
    b2.place(x=500,y=400,width=90)


b5=Button(win,text='Delete Book',font=('times new roman',14,'bold'),bg="#00ff80",command=delete)
b5.place(x=350,y=400,width=300,height=50)


win.mainloop()
