import tkinter
from tkinter import *

root=Tk()
root.geometry("350x440")
root.title(" CALCULATOR ")

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())

            scvalue.set(value)
            screen.update()
    elif text == "CLR":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


#icon        
Image_icon=PhotoImage(file="C:/Users/Lenovo/Downloads/cal icon.png")
root.iconphoto(False,Image_icon)
    

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="arial 28 bold")
screen.pack(fill=X,ipadx=6,pady=8,padx=8)

frame1=Frame(root,bg="grey").pack()

button=Button(frame1,text="CLR",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#3697f5")
button.place(x=8,y=80)
button.bind('<Button-1>',click)
button=Button(frame1,text="%",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=92,y=80)
button.bind('<Button-1>',click)
button=Button(frame1,text="/",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=175,y=80)
button.bind('<Button-1>',click)
button=Button(frame1,text="*",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=260,y=80)
button.bind('<Button-1>',click)

button=Button(frame1,text="7",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=8,y=150)
button.bind('<Button-1>',click)
button=Button(frame1,text="8",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=92,y=150)
button.bind('<Button-1>',click)
button=Button(frame1,text="9",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=175,y=150)
button.bind('<Button-1>',click)
button=Button(frame1,text="+",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=260,y=150)
button.bind('<Button-1>',click)

button=Button(frame1,text="4",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=8,y=220)
button.bind('<Button-1>',click)
button=Button(frame1,text="5",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=92,y=220)
button.bind('<Button-1>',click)
button=Button(frame1,text="6",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=175,y=220)
button.bind('<Button-1>',click)
button=Button(frame1,text="-",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=260,y=220)
button.bind('<Button-1>',click)

button=Button(frame1,text="1",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=8,y=290)
button.bind('<Button-1>',click)
button=Button(frame1,text="2",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=92,y=290)
button.bind('<Button-1>',click)
button=Button(frame1,text="3",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=175,y=290)
button.bind('<Button-1>',click)
button=Button(frame1,text="=",font="arial 20 bold",width=4,height=3,fg="#fff",bg="#fe9037")
button.place(x=260,y=290)
button.bind('<Button-1>',click)

button=Button(frame1,text="0",font="arial 20 bold",width=9,height=1,fg="#fff",bg="#2a2d36")
button.place(x=8,y=360)
button.bind('<Button-1>',click)
button=Button(frame1,text=".",font="arial 20 bold",width=4,height=1,fg="#fff",bg="#2a2d36")
button.place(x=175,y=360)
button.bind('<Button-1>',click)



root.mainloop()
