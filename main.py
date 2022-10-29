from tkinter import*
from tkinter import ttk

global correct
correct=0
global incorrect
incorrect=0
global ans
ans=[]
flag=False


def quiz():
    
    page1=Tk()
    page1.geometry("1000x1000")
    Label(page1, text='Total keywords in python',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(page1, text='33',font=('Arial',25,'bold'),bg='yellow',command=window_correct).grid(row=3,column=1)
    Button(page1, text='31',font=('Arial',25,'bold'),bg='grey',command=window_incorrect).grid(row=3,column=2)
    Button(page1, text='30',font=('Arial',25,'bold'),bg='pink',command=window_incorrect).grid(row=3,column=3)
    Button(page1, text="Next",font=('Arial',25,'bold'),bg='pink',command=page1.destroy).grid(row=4,column=2)
    page1.mainloop()
        
    page2=Tk()
    page2.geometry("1000x1000")

    Label(page2, text='helloooooooooooooooooooooo',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(page2, text='hello',font=('Arial',25,'bold'),bg='yellow',command=window2_incorrect).grid(row=3,column=1)
    Button(page2, text='heyy',font=('Arial',25,'bold'),bg='grey',command=window2_correct).grid(row=3,column=2)
    Button(page2, text='hiii',font=('Arial',25,'bold'),bg='pink',command=window2_incorrect).grid(row=3,column=3)
    Button(page2, text="Next",font=('Arial',25,'bold'),bg='pink',command=page2.destroy).grid(row=4,column=2)
    page2.mainloop()

    page3=Tk()


    Label(frame3, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='yellow',command=window3_correct).grid(row=3,column=1)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='grey',command=window3_incorrect).grid(row=3,column=2)
    Button(frame3, text='',font=('Arial',25,'bold'),bg='pink',command=window3_correct).grid(row=3,column=3)

    window.add(frame4, text='Question4')

    Label(frame4, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='yellow',command=window4_incorrect).grid(row=3,column=1)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='grey',command=window4_correct).grid(row=3,column=2)
    Button(frame4, text='',font=('Arial',25,'bold'),bg='pink',command=window4_incorrect).grid(row=3,column=3)

    window.add(frame5, text='Question5')

    Label(frame5, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='yellow',command=window5_correct).grid(row=3,column=1)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='grey',command=window5_incorrect).grid(row=3,column=2)
    Button(frame5, text='',font=('Arial',25,'bold'),bg='pink',command=window5_correct).grid(row=3,column=3)

    window.add(frame6, text='Question6')

    Label(frame6, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='yellow',command=window6_incorrect).grid(row=3,column=1)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='grey',command=window6_correct).grid(row=3,column=2)
    Button(frame6, text='',font=('Arial',25,'bold'),bg='pink',command=window6_incorrect).grid(row=3,column=3)

    window.add(frame7, text='Question7')

    Label(frame7, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='yellow',command=window7_correct).grid(row=3,column=1)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='grey',command=window7_incorrect).grid(row=3,column=2)
    Button(frame7, text='',font=('Arial',25,'bold'),bg='pink',command=window7_correct).grid(row=3,column=3)

    window.add(frame8, text='Question8')

    Label(frame8, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='yellow',command=window8_incorrect).grid(row=3,column=1)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='grey',command=window8_correct).grid(row=3,column=2)
    Button(frame8, text='',font=('Arial',25,'bold'),bg='pink',command=window8_incorrect).grid(row=3,column=3)

    window.add(frame9, text='Question9')

    Label(frame9, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='yellow',command=window9_correct).grid(row=3,column=1)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='grey',command=window9_incorrect).grid(row=3,column=2)
    Button(frame9, text='',font=('Arial',25,'bold'),bg='pink',command=window9_correct).grid(row=3,column=3)

    window.add(frame10, text='Question10')


    Label(frame10, text='',font=('Arial',50,'bold')).grid(row=2,column=2)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='yellow',command=window10_incorrect).grid(row=3,column=1)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='grey',command=window10_correct).grid(row=3,column=2)
    Button(frame10, text='',font=('Arial',25,'bold'),bg='pink',command=window10_incorrect).grid(row=3,column=3)
    Button(frame10, text='Submit',font=('Arial',25,'bold'),bg='pink',command=disp_result).grid(row=4,column=4)



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

def next1():
    #page1.destroy()
    flag=True
    print(flag)

def window2_correct():
    global correct
    correct+=1
    global ans
    ans.append("2:correct")
    flag=True

def window2_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("2:incorrect")
    flag=True

def window3_correct():
    global correct
    correct+=1
    global ans
    ans.append("3:correct")
    flag=True

def window3_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("3:incorrect")
    flag=True

def window4_correct():
    global correct
    correct+=1
    global ans
    ans.append("4:correct")
    flag=True

def window4_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("4:incorrect")
    flag=True

def window5_correct():
    global correct
    correct+=1
    global ans
    ans.append("5:correct")
    flag=True

def window5_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("5:incorrect")
    flag=True

def window6_correct():
    global correct
    correct+=1
    global ans
    ans.append("6:correct")
    flag=True

def window6_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("6:incorrect")
    flag=True

def window7_correct():
    global correct
    correct+=1
    global ans
    ans.append("7:correct")
    flag=True

def window7_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("7:incorrect")
    flag=True

def window8_correct():
    global correct
    correct+=1
    global ans
    ans.append("8:correct")
    flag=True

def window8_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("8:incorrect")
    flag=True

def window9_correct():
    global correct
    correct+=1
    global ans
    ans.append("9:correct")
    flag=True

def window9_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("9:incorrect")
    flag=True

def window10_correct():
    global correct
    correct+=1
    global ans
    ans.append("10:correct")
    flag=True

def window10_incorrect():
    global incorrect
    incorrect+=1
    global ans
    ans.append("10:incorrect")
    flag=True
    
    
    
def disp_result():
    hello=Tk()
    global incorrect
    global correct  
    global ans   
    Label(hello,text=correct).pack()
    Label(hello,text=incorrect).pack()
    Label(hello,text=ans).pack()
    hello.mainloop()
    
    
    

    




    
quiz()

window.pack()



window.mainloop()

print(correct,incorrect)
for i in ans:
    print(i)

    
