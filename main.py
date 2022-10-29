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
frame7=ttk.Frame(window)
frame8=ttk.Frame(window)
frame9=ttk.Frame(window)
frame10=ttk.Frame(window)


root=ttk.Frame(window)

def quiz(window):
    window.add(frame1, text='Question1')
    window.add(frame2, text='Question2')
    window.add(frame3, text='Question3')
    window.add(frame4, text='Question4')
    window.add(frame5, text='Question5')
    window.add(frame6, text='Question6')
    window.add(frame7, text='Question7')
    window.add(frame8, text='Question8')
    window.add(frame9, text='Question9')
    window.add(frame10, text='Question10')

    Label(frame1, text='Total keywords in python',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame1, text='33',font=('Arial',25,'bold'),bg='yellow',command=window_correct).grid(row=3,column=1)
    Button(frame1, text='31',font=('Arial',25,'bold'),bg='grey',command=window_incorrect).grid(row=3,column=2)
    Button(frame1, text='30',font=('Arial',25,'bold'),bg='pink',command=window_incorrect).grid(row=3,column=3)
    Button(frame1, text="Next",font=('Arial',25,'bold'),bg='pink').grid(row=4,column=2)

    Label(frame2, text='a',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame2, text='a',font=('Arial',25,'bold'),bg='yellow',command=window2_incorrect).grid(row=3,column=1)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='grey',command=window2_correct).grid(row=3,column=2)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='pink',command=window2_incorrect).grid(row=3,column=3)

    Label(frame3, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='yellow',command=window3_correct).grid(row=3,column=1)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='grey',command=window3_incorrect).grid(row=3,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='pink',command=window3_correct).grid(row=3,column=3)

    Label(frame4, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='yellow',command=window4_incorrect).grid(row=3,column=1)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='grey',command=window4_correct).grid(row=3,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='pink',command=window4_incorrect).grid(row=3,column=3)

    Label(frame5, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='yellow',command=window5_correct).grid(row=3,column=1)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='grey',command=window5_incorrect).grid(row=3,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='pink',command=window5_correct).grid(row=3,column=3)

    Label(frame6, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='yellow',command=window6_incorrect).grid(row=3,column=1)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='grey',command=window6_correct).grid(row=3,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='pink',command=window6_incorrect).grid(row=3,column=3)

    Label(frame7, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='yellow',command=window7_correct).grid(row=3,column=1)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='grey',command=window7_incorrect).grid(row=3,column=2)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='pink',command=window7_correct).grid(row=3,column=3)

    Label(frame8, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='yellow',command=window8_incorrect).grid(row=3,column=1)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='grey',command=window8_correct).grid(row=3,column=2)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='pink',command=window8_incorrect).grid(row=3,column=3)

    Label(frame9, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='yellow',command=window9_correct).grid(row=3,column=1)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='grey',command=window9_incorrect).grid(row=3,column=2)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='pink',command=window9_correct).grid(row=3,column=3)

    Label(frame10, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='yellow',command=window10_incorrect).grid(row=3,column=1)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='grey',command=window10_correct).grid(row=3,column=2)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='pink',command=window10_incorrect).grid(row=3,column=3)


def window_correct():
    Label(frame1, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame1, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window_incorrect():
    Label(frame1, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame1, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)


def window2_correct():
    Label(frame2, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame2, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window2_incorrect():
    Label(frame2, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame2, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)


def window3_correct():
    Label(frame3, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame3, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window3_incorrect():
    Label(frame3, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame3, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)


def window4_correct():
    Label(frame4, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame4, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window4_incorrect():
    Label(frame4, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame4, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)


def window5_correct():
    Label(frame5, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame5, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window5_incorrect():
    Label(frame5, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame5, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)
    

def window6_correct():
    Label(frame6, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame6, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window6_incorrect():
    Label(frame6, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame6, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)


def window7_correct():
    Label(frame7, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame7, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window7_incorrect():
    Label(frame7, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame7, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)
    

def window8_correct():
    Label(frame8, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame8, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window8_incorrect():
    Label(frame8, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame8, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)


def window9_correct():
    Label(frame9, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame9, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window9_incorrect():
    Label(frame9, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame9, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)


def window10_correct():
    Label(frame10, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame10, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)

def window10_incorrect():
    Label(frame10, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(frame10, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)
    
    
    
    
        
    
    
    

    




    
quiz(window)
window.pack()
window.mainloop()