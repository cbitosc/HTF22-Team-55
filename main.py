from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mb
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
#final=ttk.Frame(window)

root=ttk.Frame(window)

correct=0
incorrect=0
answers={}

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
    #window.add(final, text='Result')

    Label(frame1, text='Total keywords in python',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame1, text='33',font=('Arial',25,'bold'),bg='yellow',command=window_correct(correct)).grid(row=3,column=1)
    Button(frame1, text='31',font=('Arial',25,'bold'),bg='grey',command=window_incorrect(incorrect)).grid(row=3,column=2)
    Button(frame1, text='30',font=('Arial',25,'bold'),bg='pink',command=window_incorrect(incorrect)).grid(row=3,column=3)
    Button(frame1, text="Next",font=('Arial',25,'bold'),bg='pink').grid(row=4,column=2)

    Label(frame2, text='a',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='yellow',command=window2_incorrect(incorrect)).grid(row=3,column=1)
    Button(frame2, text='A',font=('Arial',25,'bold'),bg='grey',command=window2_correct(correct)).grid(row=3,column=2)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='pink',command=window2_incorrect(incorrect)).grid(row=3,column=3)

    Label(frame3, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame3, text='A',font=('Arial',25,'bold'),bg='yellow',command=window3_correct(correct)).grid(row=3,column=1)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='grey',command=window3_incorrect(incorrect)).grid(row=3,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='pink',command=window3_incorrect(incorrect)).grid(row=3,column=3)

    Label(frame4, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='yellow',command=window4_incorrect(incorrect)).grid(row=3,column=1)
    Button(frame4, text='A',font=('Arial',25,'bold'),bg='grey',command=window4_correct(correct)).grid(row=3,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='pink',command=window4_incorrect(incorrect)).grid(row=3,column=3)

    Label(frame5, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame5, text='A',font=('Arial',25,'bold'),bg='yellow',command=window5_correct(correct)).grid(row=3,column=1)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='grey',command=window5_incorrect(incorrect)).grid(row=3,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='pink',command=window5_incorrect(incorrect)).grid(row=3,column=3)

    Label(frame6, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='yellow',command=window6_incorrect(incorrect)).grid(row=3,column=1)
    Button(frame6, text='A',font=('Arial',25,'bold'),bg='grey',command=window6_correct(correct)).grid(row=3,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='pink',command=window6_incorrect(incorrect)).grid(row=3,column=3)

    Label(frame7, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='yellow',command=window7_incorrect(incorrect)).grid(row=3,column=1)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='grey',command=window7_incorrect(incorrect)).grid(row=3,column=2)
    Button(frame7, text='A',font=('Arial',25,'bold'),bg='pink',command=window7_correct(correct)).grid(row=3,column=3)

    Label(frame8, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='yellow',command=window8_incorrect(incorrect)).grid(row=3,column=1)
    Button(frame8, text='A',font=('Arial',25,'bold'),bg='grey',command=window8_correct(correct)).grid(row=3,column=2)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='pink',command=window8_incorrect(incorrect)).grid(row=3,column=3)

    Label(frame9, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame9, text='A',font=('Arial',25,'bold'),bg='yellow',command=window9_correct(correct)).grid(row=3,column=1)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='grey',command=window9_incorrect(incorrect)).grid(row=3,column=2)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='pink',command=window9_incorrect(incorrect)).grid(row=3,column=3)

    Label(frame10, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='yellow',command=window10_incorrect(incorrect)).grid(row=3,column=1)
    Button(frame10, text='A',font=('Arial',25,'bold'),bg='grey',command=window10_correct(correct)).grid(row=3,column=2)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='pink',command=window10_incorrect(incorrect)).grid(row=3,column=3)
    Button(frame10,text='submit',command=result_display).grid(row=5,column=5)
    


def window_correct(correct):
    correct+=1
    answers[1]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)'''

def window_incorrect(incorrect):
    incorrect+=1
    answers[1]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=1,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=1,column=3)'''


def window2_correct(correct):
    correct+=1
    answers[2]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=2,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=2,column=3)'''

def window2_incorrect(incorrect):
    incorrect+=1
    answers[2]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=2,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=2,column=3)'''


def window3_correct(correct):
    correct+=1
    answers[3]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=3,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=3,column=3)'''

def window3_incorrect(incorrect):
    incorrect+=1
    answers[3]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=3,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=3,column=3)'''


def window4_correct(correct):
    correct+=1
    answers[4]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=4,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=4,column=3)'''

def window4_incorrect(incorrect):
    incorrect+=1
    answers[4]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=4,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=4,column=3)'''


def window5_correct(correct):
    correct+=1
    answers[5]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=5,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=5,column=3)'''

def window5_incorrect(incorrect):
    incorrect+=1
    answers[5]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=5,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=5,column=3)'''
    

def window6_correct(correct):
    correct+=1
    answers[6]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=6,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=6,column=3)'''

def window6_incorrect(incorrect):
    incorrect+=1
    answers[6]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=6,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=6,column=3)'''


def window7_correct(correct):
    correct+=1
    answers[7]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=7,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=7,column=3)'''

def window7_incorrect(incorrect):
    incorrect+=1
    answers[7]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=7,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=7,column=3)'''
    

def window8_correct(correct):
    correct+=1
    answers[8]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=8,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=8,column=3)'''

def window8_incorrect(incorrect):
    incorrect+=1
    answers[8]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=8,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=8,column=3)'''


def window9_correct(correct):
    correct+=1
    answers[9]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=9,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=9,column=3)'''

def window9_incorrect(incorrect):
    incorrect+=1
    answers[9]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=9,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=9,column=3)'''


def window10_correct(correct):
    correct+=1
    answers[10]="Correct"
    '''Label(final, text='Correct',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=10,column=2)
    Label(final, text='Obtained Marks: 1',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=10,column=3)'''

def window10_incorrect(incorrect):
    incorrect+=1
    answers[10]="Incorrect"
    '''Label(final, text='Incorrect',font=('Times New Roman',35,'bold'),background='green',fg='pink').grid(row=10,column=2)
    Label(final, text='Obtained Marks: 0',font=('Times New Roman',40,'bold'),background='blue',fg='yellow').grid(row=10,column=3)'''

def result_display():
    score=correct*10
    mb.showinfo("Result", f"{score}\n{correct}\n{incorrect}\n{answers}")



    
    
    
        
    
    
    

    




    
quiz(window)
window.pack()
window.mainloop()

    
