from tkinter import *
from tkinter import ttk #import Theme of tk
from tkinter import messagebox
#############################################3
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data
#####################################################3


GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')#ชื่อของโปรแกรม
GUI.geometry('500x800')#ขนาดของโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึก',font=('Kanit',20),fg='green')
L1.place(x=30,y=30)

###########################
def Button2():
       text = 'Uncle Engineer'
       messagebox.showinfo('Teacher',text)

FB1 = LabelFrame(GUI,text='Teacher',font=('Kanit',10),fg='blue') # คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='ใครเป็นผู้สอน',command=Button2)
B2.pack(ipadx=20,ipady=20)
############################

def Button3():
       text = 'Python 101 Ep.2'
       messagebox.showinfo('Study',text)

FB1 = LabelFrame(GUI,text='Study',font=('Kanit',10),fg='blue') # คล้ายกระดาน
FB1.place(x=100,y=280)
B2 = ttk.Button(FB1,text='สัปดาห์นี้เรียนอะไร',command=Button3)
B2.pack(ipadx=20,ipady=20)

def Button4():
       text = 'Modul,GUI,Botton'
       messagebox.showinfo('Python Unit',text)

FB1 = LabelFrame(GUI,text='Python Unit',font=('Kanit',10),fg='blue') # คล้ายกระดาน
FB1.place(x=100,y=480)
B2 = ttk.Button(FB1,text='เรียนเรื่องอะไรไปบ้าง',command=Button4)
B2.pack(ipadx=20,ipady=20)

def Button5():
       text = 'Creat GUI and Botton'
       messagebox.showinfo('Homework',text)

FB1 = LabelFrame(GUI,text='Homework',font=('Kanit',10),fg='blue') # คล้ายกระดาน
FB1.place(x=100,y=680)
B2 = ttk.Button(FB1,text='มีการบ้านอะไรบ้าง',command=Button5)
B2.pack(ipadx=20,ipady=20)

######################SECTION RIGTH################################
LF1 = ttk.LabelFrame(GUI)
LF1.place(x=400,y=50)

v_data= StringVar()
E1 = ttk.Entry(LF1,textvarible=v_data,font=('Kanit',25))



GUI.mainloop()
