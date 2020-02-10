from tkinter import *
root=Tk()
root.title("CGPA CALCULATOR")
root.geometry("800x800")

def tgpa1():
    N1=int(entry1.get())
    N2=int(entry2.get())
    N3=int(entry3.get())
    N4=int(entry4.get())
    N5=int(entry5.get())
    N6=int(entry6.get())
    if N1>100 or N2>100 or N3>100 or N4>100 or N5>100 or N6>100:    
        mp=Message(frame3,text="Please Enter Number Less Than 100.")
        mp.config(width=350,fg="red",font=('times', 10, 'bold'))
        mp.grid(row=2,column=0,pady=2,padx=8)
    else:
        mp=Message(frame3,text="                                                                      ")
        mp.config(width=350)
        mp.grid(row=2,column=0,pady=12,padx=5)
        add=N1+N2+N3+N4+N5+N6
        tgpaF=(add*10)/600
        label17=Label(frame,text=tgpaF,font=('arial',10),width=17,bg="white")
        label17.grid(row=8,column=1,padx=5,ipady=2,pady=10)
        Cg=tgpaF
        label18=Label(frame3,text=Cg,font=('arial',10),width=17,bg="white").grid(row=0,column=1,padx=2)
        return(tgpaF)
    

def tgpa2():
    N1=int(entry8.get())
    N2=int(entry9.get())
    N3=int(entry10.get())
    N4=int(entry12.get())
    N5=int(entry13.get())
    N6=int(entry14.get())
    if N1>100 or N2>100 or N3>100 or N4>100 or N5>100 or N6>100:    
        mp=Message(frame3,text="Please Enter Number Less Than 100.")
        mp.config(width=350,fg="red",font=('times', 10, 'bold'))
        mp.grid(row=2,column=0,pady=2,padx=8)
    else:
        mp=Message(frame3,text="                                                                      ")
        mp.config(width=350)
        mp.grid(row=2,column=0,pady=12,padx=5)
        add=N1+N2+N3+N4+N5+N6
        tgpaS=(add*10)/600
        label19=Label(frame1,text=tgpaS,font=('arial',10),width=17,bg="white")
        label19.grid(row=8,column=1,padx=5,ipady=2,pady=10)
        return(tgpaS)

def cgpa1():
    Cg=(tgpa1()+tgpa2())/2
    label18=Label(frame3,text=Cg,font=('arial',10),width=17,bg="white").grid(row=0,column=1,padx=2)

frame=Frame(root,height=600,width=600,bg="powder blue")
frame.grid(row=0,column=0,padx=10)

frame3=Frame(root,height=300,width=300)
frame3.grid(row=0,column=1,rowspan=3,pady=20,padx=20)

frame1=Frame(root,height=600,width=600,bg="powder blue")
frame1.grid(row=1,column=0,padx=10,pady=20)


label=Label(frame,text="FIRST SEMESTER",bg="powder blue")
label.grid(pady=10)

label1=Label(frame,text="PEL121",bg="powder blue")
label1.grid(row=2, column=0,pady=10,sticky="w")
entry1=Entry(frame,font=('arial',10))
entry1.grid(row=2,column=1)

label2=Label(frame,text="PHY109",bg="powder blue")
label2.grid(row=3, column=0,sticky="w")
entry2=Entry(frame,font=('arial',10))
entry2.grid(row=3,column=1,padx=5,pady=10)

label3=Label(frame,text="CSE101",bg="powder blue")                     
label3.grid(row=4, column=0,sticky="w")
entry3=Entry(frame,font=('arial',10))
entry3.grid(row=4,column=1,padx=5,pady=10)

label4=Label(frame,text="MTH165",bg="powder blue")
label4.grid(row=5, column=0,sticky="w")
entry4=Entry(frame,font=('arial',10))
entry4.grid(row=5,column=1,padx=5,pady=10)

label5=Label(frame,text="ECE121",bg="powder blue")
label5.grid(row=6, column=0,sticky="w")
entry5=Entry(frame,font=('arial',10))
entry5.grid(row=6,column=1,padx=5,pady=10)

label6=Label(frame,text="CSE104",bg="powder blue")
label6.grid(row=7, column=0,sticky="w")
entry6=Entry(frame,font=('arial',10))
entry6.grid(row=7,column=1,padx=5,pady=10)

button1=Button(frame,text="Calulate TGPA",command=tgpa1).grid(row=8,column=0,padx=5,pady=10)

button3=Button(frame3,text="Calculate CGPA",command=cgpa1).grid(row=0,column=0,pady=15,padx=5)

label18=Label(frame3,font=('arial',10),width=17,bg="white").grid(row=0,column=1,padx=2)

button4=Button(frame3,text="Clear").grid(row=1,column=0,ipadx=10)

button5=Button(frame3,text="Quit",command=quit).grid(row=1,column=1,ipadx=15,padx=20)

label7=Label(frame1,text="SECOND SEMESTER",bg="powder blue")
label7.grid(pady=10)

label8=Label(frame1,text="PES214",bg="powder blue")
label8.grid(row=2, column=0,pady=10,sticky="w")
entry8=Entry(frame1,font=('arial',10))
entry8.grid(row=2,column=1)

label9=Label(frame1,text="CSE211",bg="powder blue")
label9.grid(row=3, column=0,sticky="w")
entry9=Entry(frame1,font=('arial',10))
entry9.grid(row=3,column=1,padx=5,pady=10)

label10=Label(frame1,text="CSE205",bg="powder blue")
label10.grid(row=4, column=0,sticky="w")
entry10=Entry(frame1,font=('arial',10))
entry10.grid(row=4,column=1,padx=5,pady=10)

label11=Label(frame1,text="MTH405",bg="powder blue")
label11.grid(row=5, column=0,sticky="w")
entry12=Entry(frame1,font=('arial',10))
entry12.grid(row=5,column=1,padx=5,pady=10)

label13=Label(frame1,text="INT213",bg="powder blue")
label13.grid(row=6, column=0,sticky="w")
entry13=Entry(frame1,font=('arial',10))
entry13.grid(row=6,column=1,padx=5,pady=10)

label14=Label(frame1,text="INT306",bg="powder blue")
label14.grid(row=7, column=0,sticky="w")
entry14=Entry(frame1,font=('arial',10))
entry14.grid(row=7,column=1,padx=5,pady=10)

button2=Button(frame1,text="Calulate TGPA",command=tgpa2).grid(row=8,column=0,padx=5,pady=10)

root.mainloop()
