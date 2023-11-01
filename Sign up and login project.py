from tkinter import *
from tkinter import ttk,messagebox,scrolledtext
from PIL import ImageTk, Image
import mysql.connector as mc

win = Tk()
win.title('sign up and login page')
win.geometry('1280x800')
win.config(bg='#80ffff')

# image intro
#-------------
sing_up = ImageTk.PhotoImage(Image.open("C:\Python310\sign-up.png")) 
p1 = Label(win, image = sing_up)
p1.pack(side = "left", fill = "both")

# frame intro
#-------------
frame = Frame(win, bg="white")
frame.place(x = 700,y = 50,width = 550,height = 500)

# label intro
#-------------
l1 = Label(frame,text='Sign Up', font=('times new roman',25,'bold'),bg="white")
l1.place(x = 10,y = 10)
l2 = Label(frame,text='please fill in the form to create an account', font=('kalam',14),bg="white")
l2.place(x = 10,y = 50)
l3 = Label(frame,text='First name', font=('Cambria',14),bg="white")
l3.place(x = 10,y = 100)
l4 = Label(frame,text='Last name', font=('Cambria',14),bg="white")
l4.place(x = 300,y = 100)
l5 = Label(frame,text='Email', font=('Cambria',14),bg="white")
l5.place(x = 10,y = 200)
l6 = Label(frame,text='Password', font=('Cambria',14),bg="white")
l6.place(x = 10,y = 250)
l7 = Label(frame,text='Confirm Password', font=('Cambria',14),bg="white")
l7.place(x = 10,y = 300)
#l7 = Label(frame,text='Sign Up', font=('Cambria',14),bg="white")
#l7.place(x = 10,y = 450)
l7 = Label(win,text='Already have an account?', font=('kalam',14))
l7.place(x = 750,y = 600)
#l7 = Label(win,text='Login here', font=('times new roman',18,'bold'))
#l7.place(x = 1000,y = 600)

# entry intro
#-------------
e1 = Entry(frame,width = 20,font=('Cambria',14))
e1.place(x = 10,y = 150)
e2 = Entry(frame,width = 20,font=('Cambria',14))
e2.place(x = 300,y = 150)
e3 = Entry(frame,width = 20,font=('Cambria',14))
e3.place(x = 250,y = 200)
e4 = Entry(frame,width = 20,font=('Cambria',14))
e4.place(x = 250,y = 250)
e5 = Entry(frame,width = 20,font=('Cambria',14))
e5.place(x = 250,y = 300)

# check box intro
#----------------
check =StringVar()
cb1 = Checkbutton(win, text ='I accept the terms of use & privacy policy',font=('kalam',14),bg="white")
cb1.place(x = 700,y = 450)

# Button intro
#--------------

def sign_up():
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="":
        messagebox.showerror("Error!","Sorry!, All fields are required",parent = win)
    elif check.get() == 0:
        messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent = win)
    else:
        f_name = e1.get()
        l_name = e2.get()
        email = e3.get()
        password = e4.get()
        c_password = e5.get()
        conn = mc.connect(host = "localhost", user = "root" , password = "" , database = "kumar")
        cursor = conn.cursor()
        cursor.execute("insert into information (f_name,l_name,email,password,c_password) values('"+f_name+"', '"+l_name+"', '"+email+"', '"+password+"', '"+c_password+"')")
        conn.close()
        messagebox.showinfo("Congratulations!","Register Successful",parent=win)


b1 = Button(frame,text='Sign Up', font=('times new roman',14,'bold'),bg="#00ff80",command = sign_up)
b1.place(x = 10,y = 450)
        
        
    
def login_here():
    
    newwin = Toplevel(win)
    newwin.title('Login page')
    newwin.geometry('600x550')
    newwin.configure(bg = 'cyan')
    

    # frame intro
    #-------------
    frame = Frame(newwin, bg="white")
    frame.place(x = 50,y = 50,width = 450,height = 400)

    # label intro
    #-------------
    l1 = Label(frame,text='LOGIN', font=('times new roman',20,'bold'),bg="white")
    l1.place(x = 150,y = 10)
    l2 = Label(frame,text = 'Email ID',font=('Cambria',14,'bold'),bg='white')
    l2.place(x = 10 , y =100)
    l3 = Label(frame,text = 'Password',font=('Cambria',14,'bold'),bg='white')
    l3.place(x = 10 , y =200)
    #l4 = Label(frame,text = 'forgot password ?',font=('Cambria',12,'bold'),bg='#00ff00',fg='white')
    #l4.place(x = 300 , y =300)

    # entry intro
    #-------------
    e1 = Entry(frame,width = 20,font =('Cambria',14))
    e1.place(x = 10,y = 150)
    e2 = Entry(frame,width = 20,font =('Cambria',14))
    e2.place(x = 10,y = 250)

    #check box intro
    #----------------
    check = StringVar()
    cb1 = Checkbutton(newwin, text ='Remember me',font=('kalam',14,'bold'),bg="white")
    cb1.place(x = 50,y = 350)

    # button intro
    #--------------
    
    def login():
        if e1.get()=="" or e2.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=newwin)
        else:
            try:
                connection=mc.connect(host="localhost", user="root", password="", database="kumar")
                cur = connection.cursor()
                cur.execute("select * from information where email=%s and password=%s",(e1.get(),e2.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid USERNAME & PASSWORD",parent=newwin)
                else:
                    messagebox.showinfo("Success","Login successfully",parent=newwin)
                    connection.close()

                    root = Toplevel(win)
                    root.title('registration form')
                    root.geometry('600x900')
                    root.configure(bg = 'cyan')

                    l1 = Label(root,text='REGISTRATION FORM',font=('times new roman',20,'bold'),fg='black')
                    l1.place(x = 200,y = 10)
                    l2 = Label(root,text='Name',font=('Cambria',14,'bold'),fg='black')
                    l2.place(x = 10,y = 100)
                    l3 = Label(root,text='Father Name',font=('Cambria',14,'bold'),fg='black')
                    l3.place(x = 10,y = 150)
                    l4 = Label(root,text='DOB',font=('Cambria',14,'bold'),fg='black')
                    l4.place(x = 10,y = 200)
                    l5 = Label(root,text='Age',font=('Cambria',14,'bold'),fg='black')
                    l5.place(x = 10,y = 250)
                    l6 = Label(root,text='Gender',font=('Cambria',14,'bold'),fg='black')
                    l6.place(x = 10,y = 300)
                    l7 = Label(root,text='phone number',font=('Cambria',14,'bold'),fg='black')
                    l7.place(x = 10,y = 350)
                    l8 = Label(root,text='Describe Yourself:',font=('Cambria',14,'bold'),fg='black')
                    l8.place(x = 10,y = 400)
                    r1= Entry(root,width = 20,font =('Cambria',14))
                    r1.place(x = 200,y = 100)
                    r2= Entry(root,width = 20,font =('Cambria',14))
                    r2.place(x = 200,y = 150)
                    r3= Entry(root,width = 20,font =('Cambria',14))
                    r3.place(x = 200,y = 200)
                    r4= Entry(root,width = 20,font =('Cambria',14))
                    r4.place(x = 200,y = 250)
                    r5= Entry(root,width = 20,font =('Cambria',14))
                    r5.place(x = 200,y = 300)
                    r6= Entry(root,width = 20,font =('Cambria',14))
                    r6.place(x = 200,y = 350)
                    
                    # Scrolled intro
                    #----------------
                    st = scrolledtext.ScrolledText(root,width = 50,height = 5,font =('Cambria',14))
                    st.insert(INSERT,'')
                    st.place(x = 10,y = 450)

                    #button intro
                    #-------------
                    bu1=Button(root,text='Register',font=('times new roman',18,'bold'),bg='#00ff00',fg='white')
                    bu1.place(x =200,y =600)
                    
                    
                    
            
                    
                    
            except :
                messagebox.showerror("Error!","Already Login exist ",parent=newwin)




    b1 = Button(frame,text = 'forgot password ?',font=('Cambria',12,'bold'),bg='#00ff00',fg='white',command=f_password)
    b1.place(x = 300 , y =300)
    b2 = Button(newwin,text='LOGIN',width = 20, font=('times new roman',14,'bold'),bg ='#4D0039',fg='white',command=login)
    b2.place(x = 150,y = 450)

b3 = Button(win,text='Login here', font=('times new roman',14,'bold'),bg="#80ff00",command = login_here)
b3.place(x = 1000,y = 600)
    



def f_password():
    window = Toplevel(win)
    window.title('Forgot Password ?')
    window.geometry('500x500')
    window.configure(bg = 'white')

    # label intro
    #-------------
    l1 = Label(window,text='Welcome Back',font=('times new roman',18,'bold'),fg='black')
    l1.place(x = 150,y = 10)
    l2 = Label(window,text='Email ID',font=('Cambria',14,'bold'),fg='black')
    l2.place(x = 10,y = 100)
    l3 = Label(window,text='New Password',font=('Cambria',14,'bold'),fg='black')
    l3.place(x = 10,y = 200)
    l4 = Label(window,text='Confrom New Password',font=('Cambria',14,'bold'),fg='black')
    l4.place(x = 10,y = 300)

    # entry intro
    #-------------
    en1 = Entry(window,font=('Cambria',14),width = 20)
    en1.place(x = 10,y = 150)
    en2 = Entry(window,font=('Cambria',14),width = 20)
    en2.place(x = 10,y = 250)
    en3 = Entry(window,font=('Cambria',14),width = 20)
    en3.place(x = 10,y = 350)

    # button intro
    #--------------

    def c_password():
        
        if en1.get()=="":
            messagebox.showerror("Error!", "Please enter your Email Id",parent=window)
        else:
            connection = mc.connect(host="localhost", user="root", password="", database="kumar")
            cur = connection.cursor()
            cur.execute("update information set password =%s  where email = %s",(en2.get(),en1.get()))
            cur.execute("update information set c_password =%s where email = %s",(en3.get(),en1.get()))
            messagebox.showinfo("Successful", "Password has changed successfully",parent=window)
            connection.close()
                            
                            
    b1 = Button(window,text='Submit',font=('times new roman',20,'bold'),bg='#ff8000',fg='white',command=c_password)
    b1.place(x = 200, y = 400)

        
    
win.mainloop()
     
            
                    


            




        
