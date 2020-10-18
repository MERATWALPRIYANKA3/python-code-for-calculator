from tkinter import *
import math
def Display(t):
    global string
    if t=="=":
        try:
            obj.set(str(eval(obj.get())))
            string=""
        except Exception as e:
            obj.set(e)
    elif t=="C":
        obj.set("")
    elif t=="CE":
        s=obj.get()
        s=s[:len(s)-1]
        obj.set(s)
    elif t=='1/x'or t=='x^2' or t=='x^3':
        pass
    elif t=='sin':
        obj.set(str(eval(obj.get())))
    else:
        string=string+t
        obj.set(string)
string=""   
root=Tk()
root.title("calculater")
root.config(bg="#22ffee")
f1=Frame(root,bg="black")

obj=StringVar()
e=Entry(f1,textvariable=obj,bg="powder blue",font="ariel 20 bold",bd=5,relief=RAISED,justify=RIGHT)
e.pack(padx=10,pady=10,expand=YES,fill=BOTH)
f1.pack(padx=10,pady=10,expand=YES,fill=BOTH)

for data in['789/','456*','123+','.0=-',["C","CE"],['sin','cos','tan'],['1/x','x^2','x^3']]:
    f=Frame(root,bg='black')
    for t in data:
        b=Button(f,text=t,bg="powder blue",font="ariel 20 bold",bd=5,relief=RAISED,justify=RIGHT,command=lambda x=t:Display(x))
        b.pack(side=LEFT,padx=10,pady=10,expand=YES,fill=BOTH)
    f.pack(padx=10,pady=10,expand=YES,fill=BOTH)
root.mainloop()
