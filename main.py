from tkinter import*
from tkinter import ttk
import time

window=ttk.Notebook(height=1000,width=1000)


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

#root=ttk.Frame(window)

global correct
correct=0
global incorrect
incorrect=0
global ans
ans=[]


def quiz(window):
    
    window.add(frame1, text='Question1')

    Label(frame1, text='Total keywords in python',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame1, text='33',font=('Arial',25,'bold'),bg='yellow',command=window_correct).grid(row=3,column=1)
    Button(frame1, text='31',font=('Arial',25,'bold'),bg='grey',command=window_incorrect).grid(row=3,column=2)
    Button(frame1, text='30',font=('Arial',25,'bold'),bg='pink',command=window_incorrect).grid(row=3,column=3)
    Button(frame1, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame1.destroy).grid(row=4,column=2)

    
    
    window.add(frame2, text='Question2')

    Label(frame2, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame2, text='a',font=('Arial',25,'bold'),bg='yellow',command=window2_incorrect).grid(row=3,column=1)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='grey',command=window2_correct).grid(row=3,column=2)
    Button(frame2, text='',font=('Arial',25,'bold'),bg='pink',command=window2_incorrect).grid(row=3,column=3)
    Button(frame2, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame2.destroy).grid(row=4,column=2)

    window.add(frame3, text='Question3')

    Label(frame3, text='bbbbbbbbbbbbbbbbbbbbbbbbb',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='yellow',command=window3_correct).grid(row=3,column=1)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='grey',command=window3_incorrect).grid(row=3,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='pink',command=window3_correct).grid(row=3,column=3)
    Button(frame3, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame3.destroy).grid(row=4,column=2)

    window.add(frame4, text='Question4')

    Label(frame4, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='yellow',command=window4_incorrect).grid(row=3,column=1)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='grey',command=window4_correct).grid(row=3,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='pink',command=window4_incorrect).grid(row=3,column=3)
    Button(frame4, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame4.destroy).grid(row=4,column=2)

    window.add(frame5, text='Question5')

    Label(frame5, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='yellow',command=window5_correct).grid(row=3,column=1)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='grey',command=window5_incorrect).grid(row=3,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='pink',command=window5_correct).grid(row=3,column=3)
    Button(frame5, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame5.destroy).grid(row=4,column=2)

    window.add(frame6, text='Question6')

    Label(frame6, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='yellow',command=window6_incorrect).grid(row=3,column=1)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='grey',command=window6_correct).grid(row=3,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='pink',command=window6_incorrect).grid(row=3,column=3)
    Button(frame6, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame6.destroy).grid(row=4,column=2)

    window.add(frame7, text='Question7')

    Label(frame7, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='yellow',command=window7_correct).grid(row=3,column=1)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='grey',command=window7_incorrect).grid(row=3,column=2)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='pink',command=window7_correct).grid(row=3,column=3)
    Button(frame7, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame7.destroy).grid(row=4,column=2)

    window.add(frame8, text='Question8')

    Label(frame8, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='yellow',command=window8_incorrect).grid(row=3,column=1)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='grey',command=window8_correct).grid(row=3,column=2)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='pink',command=window8_incorrect).grid(row=3,column=3)
    Button(frame8, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame8.destroy).grid(row=4,column=2)

    window.add(frame9, text='Question9')

    Label(frame9, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='yellow',command=window9_correct).grid(row=3,column=1)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='grey',command=window9_incorrect).grid(row=3,column=2)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='pink',command=window9_correct).grid(row=3,column=3)
    Button(frame9, text="Next",font=('Arial',25,'bold'),bg='pink',command=frame9.destroy).grid(row=4,column=2)

    window.add(frame10, text='Question10')


    Label(frame10, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='yellow',command=window10_incorrect).grid(row=3,column=1)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='grey',command=window10_correct).grid(row=3,column=2)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='pink',command=window10_incorrect).grid(row=3,column=3)
    Button(frame10, text='Submit',font=('Arial',25,'bold'),bg='pink',command=lambda:[frame10.destroy(),disp_result()]).grid(row=4,column=4)




def window_correct():
    global correct
    correct+=1
    global ans
    ans.append("1:correct")

def window_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("1:incorrect")

def window2_correct():
    global correct
    correct+=1
    global ans
    ans.append("2:correct")

def window2_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("2:incorrect")

def window3_correct():
    global correct
    correct+=1
    global ans
    ans.append("3:correct")

def window3_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("3:incorrect")

def window4_correct():
    global correct
    correct+=1
    global ans
    ans.append("4:correct")

def window4_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("4:incorrect")

def window5_correct():
    global correct
    correct+=1
    global ans
    ans.append("5:correct")

def window5_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("5:incorrect")

def window6_correct():
    global correct
    correct+=1
    global ans
    ans.append("6:correct")

def window6_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("6:incorrect")

def window7_correct():
    global correct
    correct+=1
    global ans
    ans.append("7:correct")

def window7_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("7:incorrect")

def window8_correct():
    global correct
    correct+=1
    global ans
    ans.append("8:correct")

def window8_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("8:incorrect")

def window9_correct():
    global correct
    correct+=1
    global ans
    ans.append("9:correct")

def window9_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("9:incorrect")

def window10_correct():
    global correct
    correct+=1
    global ans
    ans.append("10:correct")

def window10_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("10:incorrect")
    
    
def disp_result():
    hello=Tk()
    global incorrect
    global correct  
    global ans   
    Label(hello,text=correct).pack()
    Label(hello,text=incorrect).pack()
    Label(hello,text=ans).pack()
    hello.mainloop()
    
    
    

    




    
quiz(window)

window.pack()



window.mainloop()



    
