from tkinter import *
def raise_frame(frame):
    name_regi.set("")
    name_login.set("")
    id_login.set("")
    id_regi.set("")
    frame.tkraise()
root=Tk()
root.geometry("500x500")

root.resizable()
name_login=StringVar()
id_login=StringVar()
name_regi=StringVar()
id_regi=StringVar()
register=Frame(root)
register.place(x=0,y=0,width=500,height=500)
login=Frame(root)
login.place(x=0,y=0,width=500,height=500)
root.title("Attendence Marker")
Label(login,text="Attendence Marker(IIIT-BH)",font="arial 15 bold").pack(side=TOP)
Label(login,text="Abhinav Gangrade(B118006)",font="arial 15 bold").pack(side=BOTTOM)
Label(login,text="Enter the Name:",font="arial 10 bold").place(x=70,y=120)
Label(login,text="Enter the Id:",font="arial 10 bold").place(x=70,y=170)
Entry(login,textvariable=name_login,bg="ghost white").place(x=190,y=120)
Entry(login,textvariable=id_login,bg="ghost white").place(x=190,y=170)
Button(login,text="Take Attendence",font="arial 12 bold").place(x=160,y=230)
Button(login,text="Register",font="arial 12 bold",command=lambda:raise_frame(register)).place(x=180,y=270)
Label(register,text="Attendence Marker(IIIT-BH)",font="arial 15 bold").pack(side=TOP)
Label(register,text="Abhinav Gangrade(B118006)",font="arial 15 bold").pack(side=BOTTOM)
Label(register,text="Enter the Name:",font="arial 10 bold").place(x=70,y=120)
Label(register,text="Enter the Id:",font="arial 10 bold").place(x=70,y=170)
Entry(register,textvariable=name_regi,bg="ghost white").place(x=190,y=120)
Entry(register,textvariable=id_regi,bg="ghost white").place(x=190,y=170)
Button(register,text="Register The Student",font="arial 12 bold").place(x=160,y=230)
Button(register,text="Login",font="arial 12 bold",command=lambda:raise_frame(login)).place(x=200,y=270)
root.mainloop()