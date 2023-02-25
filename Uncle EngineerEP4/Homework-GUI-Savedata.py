from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        s_data = list(fr)
    return s_data

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('300x500')

L1 = Label(GUI,text='โปรแกรมบันทึกข้อมูล',font=('Kanit',20),fg='blue')
L1.place(x=30,y=30)

LF1 = ttk.LabelFrame(GUI,text='[กรอกข้อมูลที่ต้องการบันทึก]')
LF1.place(x=80,y=100)

v_data = StringVar()
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Kanit',10))
E1.pack(padx=15,pady=20)


def Savedata():
    t = datetime.now().strftime('%Y%M%d %H%M%S')
    data = v_data.get()
    text =  [t,data]
    writecsv(text)
    v_data.set('')

B1 = ttk.Button(LF1,text='บันทึก',command=Savedata)
B1.pack(ipadx=10,ipady=15)


def Button2():
    text = readcsv
    print(text)
    messagebox.showinfo('ข้อคววามที่บักทีกอยู่')

B2 = ttk.Button(LF1,text='อ่านค่าที่บันทึกทั้งหมด',command=Button2)
B2.pack(ipadx=10,ipady=15)

GUI.mainloop
