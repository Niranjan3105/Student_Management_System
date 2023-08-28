from tkinter import *

class student:
    name = ""
    roll = 00
    m_marks = 0
    e_marks = 0
    p_marks = 0
    c_marks = 0
    b_marks = 0
    p = 0
    g = ""

    def perc():
        p = (m_marks + e_marks + p_marks +c_marks + b_marks)/5

    def grade():
        if (p>0.9):
            g = "A+"
            
        elif (p>0.8):
            g = "A"
            
        elif (p>0.7):
            g = "B+"
            
        elif (p>0.6):
            g = "B"
            
        elif (p>0.5):
            g = "C+"
            
        elif (p>0.4):
            g = "C"
            
        elif (p>0.3):
            g = "D"
            
        else:
            g = "E"
a=0
def Add_button():
    #if(a==0):
        #Window.destroy()
    def Back():
        Window1.destroy()
        Back1()
        print("go")
    Window1 = Tk()
    Window1.title("Student Data Base Management System")
    l2 = Label(Window1,text="Add Student Record",font=('Times New Roman',40))
    b4 = Button(Window1,text="Back",font=('Times New Roman',25),command=Back)
    b4.place(x=30,y=30)
    Window1.state('zoomed')
    l2.place(x=100,y=100)
    Window1.mainloop()
    
def Delete_button():
    
    def Back():
        Window1.destroy()
        Back1()
        print("go")
    Window1 = Tk()
    #Window.destroy()
    Window1.title("Student Data Base Management System")
    l2 = Label(Window1,text="Delete Student Record",font=('Times New Roman',40))
    b4 = Button(Window1,text="Back",font=('Times New Roman',25),command=Back)
    b4.place(x=30,y=30)
    Window1.state('zoomed')
    l2.place(x=100,y=100)
    Window1.mainloop()
    
def View_button():
    #if(a==0):
       # Window.destroy()
    def Back():
        Window1.destroy()
        Back1()
        print("go")
    Window1 = Tk()
    #Window.destroy()
    Window1.title("Student Data Base Management System")
    l2 = Label(Window1,text="View Student Record",font=('Times New Roman',40))
    b4 = Button(Window1,text="Back",font=('Times New Roman',25),command=Back)
    b4.place(x=30,y=30)
    Window1.state('zoomed')
    l2.place(x=100,y=100)
    Window1.mainloop()

    
def Back1():
    def Add():
        Window2.destroy()
        Add_button()
    def Delete():
        Window2.destroy()
        Delete_button()
    def View():
        Window2.destroy()
        View_button()
    Window2 = Tk()
    print("go1")
    global a
    a=1
    #Window1.destroy()
    Window2.state('zoomed')
    Window2.title("Student Data Base Management System")
    l1 = Label(Window2,text="Student Data Base Management system",font=('Times New Roman',40))
    l1.place(x=100,y=100)
    b1 = Button(Window2,text="Add Student Record",font=('Times New Roman',25),command=Add)
    b1.place(x=100,y=200)
    b2 = Button(Window2,text="Delete Student Record",font=('Times New Roman',25),command=Delete)
    b2.place(x=100,y=300)
    b3 = Button(Window2,text="View Student Record",font=('Times New Roman',25),command=View)
    b3.place(x=100,y=400)
    Window2.mainloop()
    

def Add1():
    Window.destroy()
    Add_button()
def Delete1():
    Window.destroy()
    Delete_button()
def View1():
    Window.destroy()
    View_button()
    



Window = Tk()
Window.state('zoomed')
Window.title("Student Data Base Management System")
l1 = Label(Window,text="Student Data Base Management system",font=('Times New Roman',40))
l1.place(x=100,y=100)
b1 = Button(Window,text="Add Student Record",font=('Times New Roman',25),command=Add1)
b1.place(x=100,y=200)
b2 = Button(Window,text="Delete Student Record",font=('Times New Roman',25),command=Delete1)
b2.place(x=100,y=300)
b3 = Button(Window,text="View Student Record",font=('Times New Roman',25),command=View1)
b3.place(x=100,y=400)
Window.mainloop()




    




    
    
