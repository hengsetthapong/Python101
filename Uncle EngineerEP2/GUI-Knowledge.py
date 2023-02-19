from tkinter import *
from tkinter import ttk #import Theme of tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')#ชื่อของโปรแกรม
GUI.geometry('500x600')#ขนาดของโปรแกรม

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
FB1.place(x=100,y=180)
B2 = ttk.Button(FB1,text='สัปดาห์นี้เรียนอะไร',command=Button3)
B2.pack(ipadx=20,ipady=20)

def Button4():
       text = 'Modul,GUI,Botton'
       messagebox.showinfo('Python Unit',text)

FB1 = LabelFrame(GUI,text='Python Unit',font=('Kanit',10),fg='blue') # คล้ายกระดาน
FB1.place(x=100,y=280)
B2 = ttk.Button(FB1,text='เรียนเรื่องอะไรไปบ้าง',command=Button4)
B2.pack(ipadx=20,ipady=20)

def Button5():
       text = 'Creat GUI and Botton'
       messagebox.showinfo('Homework',text)

FB1 = LabelFrame(GUI,text='Homework',font=('Kanit',10),fg='blue') # คล้ายกระดาน
FB1.place(x=100,y=380)
B2 = ttk.Button(FB1,text='มีการบ้านอะไรบ้าง',command=Button5)
B2.pack(ipadx=20,ipady=20)



GUI.mainloop()
