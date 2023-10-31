from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime as dt
import mysql.connector as mc


win = Tk()
win.title('IRCTC Website')
win.geometry('1280x700')
bg_color='#4D0039'

# Top section
#--------------
title=Label(win,text='IRCTC',bg=bg_color,fg='white',font=('times new roman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)


# label intro
#-------------
#l1 = Label(win,text = 'LOGIN',bg=bg_color,fg='white',font =('Cambria',14))
#l1.grid(row = 0,column = 0)
#l1.place(x = 100, y = 80)
l2 = Label(win,text = 'REGISTER',font =('Cambria',14))
l2.place(x = 200, y = 80)
l3 = Label(win,text = 'AGENT LOGIN',font =('Cambria',14))
l3.place(x = 300, y = 80)
l4 = Label(win,text = 'CONTACT US',font =('Cambria',14))
l4.place(x = 450, y = 80)
l5 = Label(win,text = 'ASK DISHA',font =('Cambria',14))
l5.place(x = 600, y = 80)
l6 = Label(win,text ='ALERTS',bg=bg_color,fg='white',font =('Cambria',14))
l6.place(x = 750, y = 80)
l7 = Label(win,text ='IRCTC EXCLUSIVE',bg=bg_color,fg='white',font =('Cambria',14))
l7.place(x = 50, y = 150)
#l8 = Label(win,text = 'TRAINS',font =('Cambria',14))
#l8.place(x = 250, y = 150)
l9 = Label(win,text = 'BUSES',font =('Cambria',14))
l9.place(x = 350, y = 150)
l10 = Label(win,text = 'FLIGHTS',font =('Cambria',14))
l10.place(x = 450, y = 150)
l11 = Label(win,text = 'HOTELS',font =('Cambria',14))
l11.place(x = 550, y = 150)
#l12 = Label(win,text = 'HOILDAYS',font =('Cambria',14))
#l12.place(x = 650, y = 150)
#l13 = Label(win,text = 'LOYALTY',font =('Cambria',14))
#l13.place(x = 750, y = 150)
#l14 = Label(win,text = 'MEALS',font =('Cambria',14))
#l14.place(x = 850, y = 150)
#l15 = Label(win,text = 'PROMOTIONS',font =('Cambria',14))
#l15.place(x = 950, y = 150)
#l16 = Label(win,text = 'MORE',font =('Cambria',14))
#l16.place(x = 1100, y = 150)
l17 = Label(win,text ='PNR STATUS',bg=bg_color,fg='white',font =('Cambria',14))
l17.place(x = 50, y = 200)
l18 = Label(win,text ='CHARTS/VACANCY',bg=bg_color,fg='white',font =('Cambria',14))
l18.place(x = 200, y = 200)
l19 = Label(win,text = 'From',font =('Cambria',14))
l19.place(x = 100, y = 250)
l20 = Label(win,text = 'To',font =('Cambria',14))
l20.place(x = 100, y = 300)
l21 = Label(win,text = 'MM/DD/YYYY',font =('Cambria',14))
l21.place(x = 100, y = 350)
l22 = Label(win,text = 'GENERAL',font =('Cambria',14))
l22.place(x = 100, y = 400)
l23 = Label(win,text = 'All Classes',font =('Cambria',14))
l23.place(x = 100, y = 450)
#l24 = Label(win,text ='Search',bg='#ff8000',fg='white',font =('Cambria',14))
#l24.place(x = 50, y = 650)
l25 = Label(win,text ='Try booking in Ask DISHA 2.0',bg='#00ff00',fg='white',font =('Cambria',14))
l25.place(x = 250, y = 650)

# check box intro
#-----------------
check = StringVar()
check1 = StringVar()
check2 = StringVar()
check3 = StringVar()
c1 = Checkbutton(win,text = 'Person With Disability Concession',font =('Cambria',14))
c1.place(x = 50,y = 500)
c2 = Checkbutton(win,text = 'Train With Available berth',font =('Cambria',14))
c2.place(x = 50,y = 550)
c3 = Checkbutton(win,text = 'Flexible With Date',font =('Cambria',14))
c3.place(x = 500,y = 500)
c4 = Checkbutton(win,text = 'Railway Pass Concession',font =('Cambria',14))
c4.place(x = 500,y = 550)


# combo box intro
#------------------
com1 = ttk.Combobox(win)
com1['values']=('Tambaram(TBM)','Arakkonam Junction(AJJ)','Coimbatore(CBE)','Madurai Junction(MDU)','Salem Junction(SA)','Erode Junction(ED)','Aluva(AWY)','Guruvayur(GUV)','Thanjavur Junctoin(TJ)','Tiruppur(TUP)','Dindigal Junction(DG)','Tirunelveli Junction(TJ)','Nagercoil Junction(NCJ)','Tuticorin(TN)','Kovilpatti(CVP)','Housur(HSRA)','Kanniyakumari(CAPE)','Palani(PLNI)','Delhi(DCI)','Ernakulam(ERN)')
com1.place(x = 300,y = 250)
com2 = ttk.Combobox(win)
com2['values']=('Tambaram(TBM)','Arakkonam Junction(AJJ)','Coimbatore(CBE)','Madurai Junction(MDU)','Salem Junction(SA)','Erode Junction(ED)','Aluva(AWY)','Guruvayur(GUV)','Thanjavur Junctoin(TJ)','Tiruppur(TUP)','Dindigal Junction(DG)','Tirunelveli Junction(TJ)','Nagercoil Junction(NCJ)','Tuticorin(TN)','Kovilpatti(CVP)','Housur(HSRA)','Kanniyakumari(CAPE)','Palani(PLNI)','Delhi(DCI)','Ernakulam(ERN)')
com2.place(x = 300,y = 300)
com3 = ttk.Combobox(win)
com3['values']=('Anubhuti Class(EA)','AC First Class(1A)','Vistadome AC(EV)','AC 2 Tier(2A)','First Class(FC)','AC 3 Tier(3A)','AC 3 Economy(3E)','Vistadome chair car(VC)','AC Chair car(CC)','Sleeper(SC)','Vistadome Non AC(VS)','Second Class(2S)')
com3.place(x = 300,y = 450)
com4 = ttk.Combobox(win)
com4['values']=('General','Ladies','Lower Berth/SR.Citizen','Person with Disability','TATKAL','premium TATKAL')
com4.place(x = 300,y = 400)

'''com5 = ttk.Combobox(win,width = 5)
com5['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
com5.place(x =300,y = 350)

com6 = ttk.Combobox(win,width = 5)
com6['values']=('1','2','3','4','5','6','7','8','9','10','11','12')
com6.place(x =350,y = 350)

com7 = ttk.Combobox(win,width = 5)
com7['values']=('2023','2024','2025')
com7.place(x =400,y = 350)'''

# datetime intro
#-----------------
l26 = Label(win,text =dt.datetime.now().strftime('%X ,%p'),font =('Cambria',14))
l26.place(x = 850 ,y = 80)
l27 = Label(win,text =dt.datetime.now().strftime('%D'),font =('Cambria',14))
l27.place(x = 300,y = 350)


# Button intro
#---------------
def details():
    newwin = Toplevel(win) 
    newwin.geometry('500x500')
    newwin.configure(bg = '#f0f0f0')
    l1 = Label(newwin,text = 'User name',font =('Cambria',14))
    l1.place(x = 80,y =100)
    l2 = Label(newwin,text='Password',font=('Cambria',14))
    l2.place(x = 80,y =150)
    l3 = Label (newwin,text='Enter Captch',font=('Cambria',14))
    l3.place(x = 80,y =200)
    b1 = Button(newwin,text = 'Sign in',bg='#ff8000',fg='white',font =('Cambria',14))
    b1.place(x = 200,y =300)
    b2 = Button(newwin,text = 'Register',bg=bg_color,fg='white',font =('Cambria',14))
    b2.place(x = 50,y =400)
    b3 = Button(newwin,text = 'Agent Login',bg=bg_color,fg='white',font =('Cambria',14))
    b3.place(x = 300,y =400)
    c1 = Checkbutton(newwin,text = 'Login & Booking with OTP',font =('Cambria',14))
    c1.place(x = 100,y = 250)
    e1 = Entry(newwin,width = 20,font=('Cambria',14))
    e1.place(x = 200,y = 100)
    e2 = Entry(newwin,width = 20,font=('Cambria',14))
    e2.place(x = 200,y = 150)
    e3 = Entry(newwin,width = 20,font=('Cambria',14))
    e3.place(x = 200,y = 200)

b1 = Button(win,text = 'LOGIN',bg=bg_color,fg='white',font =('Cambria',14),command = details)
b1.place(x = 100, y = 80)

def trains():
    newwin = Toplevel(win)
    newwin.geometry('300x300')
    newwin.configure(bg = '#f0f0f0')
    l1 = Label(newwin,text ='Book Now',font =('Cambria',14))
    l1.grid(row = 0,column = 0)
    l2 = Label(newwin,text ='Forgin Tourist Booking',font =('Cambria',14))
    l2.grid(row = 1,column = 0)
    l3 = Label(newwin,text ='Connecting Journey Booking',font =('Cambria',14))
    l3.grid(row = 2,column = 0)
    l4 = Label(newwin,text ='IRCTC Trains',font =('Cambria',14))
    l4.grid(row = 3,column = 0)
    l5 = Label(newwin,text ='Cencel Tickets',font =('Cambria',14))
    l5.grid(row = 4,column = 0)
    l6 = Label(newwin,text ='PNR Enquiry',font =('Cambria',14))
    l6.grid(row = 5,column = 0)
    l7 = Label(newwin,text ='Train Schedules',font =('Cambria',14))
    l7.grid(row = 6,column = 0)
    l8 = Label(newwin,text ='Track Your Train',font =('Cambria',14))
    l8.grid(row = 7,column = 0)
    l9 = Label(newwin,text ='PTR Cocah Train Booking',font =('Cambria',14))
    l9.grid(row = 8,column = 0)

b2 = Button(win,text = 'TRAINS',font =('Cambria',14),command = trains)
b2.place(x = 250,y = 150)    

def hoilday():
    newwin = Toplevel(win)
    newwin.geometry('100x100')
    newwin.configure(bg = '#f0f0f0')
    l1 = Label(newwin,text ='Tourist Trains',font =('Cambria',14))
    l1.grid(row = 0,column = 0)
    l2 = Label(newwin,text ='Tour Packages',font =('Cambria',14))
    l2.grid(row = 1,column = 0)
    l3 = Label(newwin,text ='Stays',font =('Cambria',14))
    l3.grid(row = 2,column = 0)

b3 = Button(win,text = 'HOILDAYS',font =('Cambria',14),command = hoilday)
b3.place(x = 650, y = 150)     

def loyality():
    newwin = Toplevel(win)
    newwin.geometry('200x100')
    newwin.configure(bg = '#f0f0f0')
    l1 = Label(newwin,text ='IRCTC SBI Credit Card',font =('Cambria',14))
    l1.grid(row = 0,column = 0)
    l2 = Label(newwin,text ='IRCTC BOB Credit Card',font =('Cambria',14))
    l2.grid(row = 1,column = 0)
    l3 = Label(newwin,text ='IRCTC HDFC Credit Card',font =('Cambria',14))
    l3.grid(row = 2,column = 0)

b4 = Button(win,text = 'LOYALTY',font =('Cambria',14),command = loyality)
b4.place(x = 750, y = 150)
    
def meals():
    newwin = Toplevel(win)
    newwin.geometry('200x100')
    newwin.configure(bg = '#f0f0f0')
    l1 = Label(newwin,text ='Order Food E-Catering',font =('Cambria',14))
    l1.grid(row = 0,column = 0)
    l2 = Label(newwin,text ='Cooked Food Menu',font =('Cambria',14))
    l2.grid(row = 1,column = 0)

b5 = Button(win,text = 'MEALS',font =('Cambria',14),command = meals)
b5.place(x = 850, y = 150)

def promotions():
    newwin = Toplevel(win)
    newwin.geometry('200x200')
    newwin.configure(bg = '#f0f0f0')
    l1 = Label(newwin,text ='Advertise with us',font =('Cambria',14))
    l1.grid(row = 0,column = 0)
    l2 = Label(newwin,text ='IRCTC Rail Connect App',font =('Cambria',14))
    l2.grid(row = 1,column = 0)
    l3 = Label(newwin,text ='IRCTC Tourism App',font =('Cambria',14))
    l3.grid(row = 2,column = 0)
    l4 = Label(newwin,text ='IRCTC Air App',font =('Cambria',14))
    l4.grid(row = 3,column = 0)
    l5 = Label(newwin,text ='UTS Ticket App',font =('Cambria',14))
    l5.grid(row = 4,column = 0)

b6 = Button(win,text = 'PROMOTIONS',font =('Cambria',14),command = promotions)
b6.place(x = 950, y = 150)

def more():
    newwin = Toplevel(win)
    newwin.geometry('350x200')
    newwin.configure(bg = '#f0f0f0')
    l1 = Label(newwin,text ='ChatBot as a Service(CaaS)',font =('Cambria',14))
    l1.grid(row = 0,column = 0)
    l2 = Label(newwin,text ='Link Your Aadhaar',font =('Cambria',14))
    l2.grid(row = 1,column = 0)
    l3 = Label(newwin,text ='Counter Ticket Cancellation',font =('Cambria',14))
    l3.grid(row = 2,column = 0)
    l4 = Label(newwin,text ='Counter Ticket Boarding Point Change',font =('Cambria',14))
    l4.grid(row = 3,column = 0)
    l5 = Label(newwin,text ='FORGOT ACCOUNT DETAILS ?',font =('Cambria',14))
    l5.grid(row = 4,column = 0)
    l6 = Label(newwin,text ='AT STATIONS',font =('Cambria',14))
    l6.grid(row = 5,column = 0)

b7 = Button(win,text = 'MORE',font =('Cambria',14),command = more)
b7.place(x = 1100, y = 150)


# database connecting
#---------------------

def search():
    if com1.get()=="" or com2.get()=="" or com3.get()=="" or com4.get()=="":
        messagebox.showerror("Error!","Sorry!,All fields are required",parent = win)
    elif check.get()== 0 or check1.get()== 0 or check2.get()== 0 or check3.get()== 0:
        messagebox.showerror("Error!","please Agree with our Terms & Conditions",parent = win)
    else:
        conn = mc.connect(host="localhost",user="root", password="", database="arun")
        cursor = conn.cursor()
        query ='select * from railway;'
        r = cursor.execute(query)
        data = cursor.fetchone()
        print('number''    ''days''       ''from''                ''to''        ''timeing')
        print(data)
        messagebox.showinfo("Congratulations!","data transfered Successful",parent=win)
        
b8 = Button(win,text ='Search',bg='#ff8000',fg='white',font =('Cambria',14),command = search)
b8.place(x = 50, y = 650)    

    
    
        
win.mainloop()
