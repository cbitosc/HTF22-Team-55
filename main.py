from tkinter import*
from tkinter import ttk
y=0
window=ttk.Notebook()
frame1=ttk.Frame(window)
frame2=ttk.Frame(window)
frame3=ttk.Frame(window)
frame4=ttk.Frame(window)
frame5=ttk.Frame(window)
frame6=ttk.Frame(window)

root=ttk.Frame(window)

def quiz(window):
    window.add(frame1, text='Question1')
    window.add(frame2, text='Question2')
    window.add(frame3, text='Question3')
    window.add(frame4, text='Question4')
    window.add(frame5, text='Question5')
    window.add(frame6, text='Question6')

    Label(frame1, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame1, text='',font=('Arial',25,'bold'),bg='yellow').grid(row=3,column=1)
    Button(frame1, text='',font=('Arial',25,'bold'),bg='grey').grid(row=3,column=2)
    Button(frame1, text='',font=('Arial',25,'bold'),bg='pink').grid(row=3,column=3)

    Label(frame2, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='yellow').grid(row=3,column=1)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='grey').grid(row=3,column=2)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='pink').grid(row=3,column=3)

    Label(frame3, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='yellow').grid(row=3,column=1)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='grey').grid(row=3,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='pink').grid(row=3,column=3)

    Label(frame4, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='yellow').grid(row=3,column=1)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='grey').grid(row=3,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='pink').grid(row=3,column=3)

    Label(frame5, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='yellow').grid(row=3,column=1)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='grey').grid(row=3,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='pink').grid(row=3,column=3)

    Label(frame6, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='yellow').grid(row=3,column=1)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='grey').grid(row=3,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='pink').grid(row=3,column=3)


def window_correct():
    Label(frame1, text='correct',font=('Arial',35,'bold'))
    
    

    




    
quiz(window)