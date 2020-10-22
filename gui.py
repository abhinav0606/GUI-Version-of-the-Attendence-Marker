from tkinter import *
import cv2
import pandas as pd
import xlsxwriter
import numpy as np
import os
import datetime
def login_student():
    Name=name_login.get()
    Id=id_login.get()
    folder = Name.lower() + Id.lower()
    list_files = os.listdir("/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder)
    list_files.sort()
    print(list_files)
    l = []
    t = []
    for i in range(len(list_files)):
        image_path = "/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder + "/" + \
                     lfrom tkinter import *
import cv2
import pandas as pd
import xlsxwriter
import numpy as np
import os
import datetime

def login_student():
    Name=name_login.get()
    Id=id_login.get()
    folder = Name.lower() + Id.lower()
    list_files = os.listdir("/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder)
    list_files.sort()
    print(list_files)
    l = []
    t = []
    for i in range(len(list_files)):
        image_path = "/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder + "/" + \
                     list_files[i]
        print(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        t.append(np.asarray(image, dtype=np.uint8))
        l.append(i)
    l = np.asarray(l, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(t), np.asarray(l))
    faces = cv2.CascadeClassifier("frontal_face.xml")
    capture = cv2.VideoCapture(0)
    result = 0
    attendence = []
    while True:
        try:
            ret, frame = capture.read()
            grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = faces.detectMultiScale(grey_frame, 1.3, 5)
            for (x, y, w, h) in face:
                cv2.imshow("Croppped", frame[y:y + h, x:x + w])
                result = model.predict(cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY))
            confidence = 0
            if result[1] < 500:
                confidence = int(100 * ((1 - result[1] / 300)))
            if confidence > 75:
                cv2.putText(frame, "unlocked " + str(confidence), (400, 450), cv2.FONT_HERSHEY_COMPLEX, 1,
                            (255, 0, 255), 2)
                # cv2.putText(frame, (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                attendence.append("Present")
            else:
                cv2.putText(frame, "locked " + str(confidence), (400, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255),
                            2)
                attendence.append("Absent")
            cv2.imshow("Frame", frame)
        except:
            pass

        if cv2.waitKey(1) == 13 or len(attendence) == 120:
            break
    print(attendence)
    if attendence.count("Present") > 77:
        listy = str(datetime.datetime.now())
        date = listy.split(" ")[0]
        excell = pd.read_excel("a.xlsx")
        columns = list(excell.columns)
        print(columns)
        print(excell)
        workbook = xlsxwriter.Workbook("a.xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.set_column(0, 40, 20)
        for i in range(len(columns)):
            worksheet.write(0, i, columns[i])
            l = list(excell[columns[i]])
            for j in range(len(l)):
                try:
                    worksheet.write(j + 1, i, l[j])
                except:
                    pass
        if date in columns:
            index_row = 0
            l = list(excell[date])
            if np.nan in l:
                index_row = l.index(np.nan)
                index = columns.index(date)
                worksheet.write(index_row + 1, index, Id)
            else:
                index = columns.index(date)
                worksheet.write(len(l) + 1, index, Id)
        else:
            worksheet.write(0, len(columns), date)
            worksheet.write(1, len(columns), Id)
        workbook.close()
        attendency.set("Present")
    else:
        attendency.set("Absent")
    capture.release()
    cv2.destroyAllWindows()
def register_student():
    Name=name_regi.get()
    id=id_regi.get()
    folder = Name.lower() + id.lower()
    try:
        os.mkdir("/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder)
    except:
        print("Folder Already exist")
        exit()
    faces = cv2.CascadeClassifier("frontal_face.xml")
    Capture = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = Capture.read()
        frame = cv2.flip(frame, 1)
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = faces.detectMultiScale(grey_frame, 1.3, 5)
        for (x, y, w, h) in face:
            cv2.imshow("Cropped", frame[y:y + h, x:x + w])
            cv2.imwrite(
                "/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder + "/" + str(
                    count) + ".JPG", cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY))
            count = count + 1
        if cv2.waitKey(1) == 13 or count == 100:
            break
    Capture.release()
    cv2.destroyAllWindows()

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
attendency=StringVar()
attendency.set("")
print(attendency)
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
Button(login,text="Take Attendence",font="arial 12 bold",command=login_student).place(x=160,y=230)
Button(login,text="Register",font="arial 12 bold",command=lambda:raise_frame(register)).place(x=180,y=270)
Entry(login,textvariable=attendency,bg="ghost white").place(x=130,y=330)
Label(register,text="Attendence Marker(IIIT-BH)",font="arial 15 bold").pack(side=TOP)
Label(register,text="Abhinav Gangrade(B118006)",font="arial 15 bold").pack(side=BOTTOM)
Label(register,text="Enter the Name:",font="arial 10 bold").place(x=70,y=120)
Label(register,text="Enter the Id:",font="arial 10 bold").place(x=70,y=170)
Entry(register,textvariable=name_regi,bg="ghost white").place(x=190,y=120)
Entry(register,textvariable=id_regi,bg="ghost white").place(x=190,y=170)
Button(register,text="Register The Student",font="arial 12 bold",command=register_student).place(x=160,y=230)
Button(register,text="Login",font="arial 12 bold",command=lambda:raise_frame(login)).place(x=200,y=270)
root.mainloop()
ist_files[i]
        print(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        t.append(np.asarray(image, dtype=np.uint8))
        l.append(i)
    l = np.asarray(l, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(t), np.asarray(l))
    faces = cv2.CascadeClassifier("frontal_face.xml")
    capture = cv2.VideoCapture(0)from tkinter import *
import cv2
import pandas as pd
import xlsxwriter
import numpy as np
import os
import datetime

def login_student():
    Name=name_login.get()
    Id=id_login.get()
    folder = Name.lower() + Id.lower()
    list_files = os.listdir("/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder)
    list_files.sort()
    print(list_files)
    l = []
    t = []
    for i in range(len(list_files)):
        image_path = "/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder + "/" + \
                     list_files[i]
        print(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        t.append(np.asarray(image, dtype=np.uint8))
        l.append(i)
    l = np.asarray(l, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(t), np.asarray(l))
    faces = cv2.CascadeClassifier("frontal_face.xml")
    capture = cv2.VideoCapture(0)
    result = 0
    attendence = []
    while True:
        try:
            ret, frame = capture.read()
            grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = faces.detectMultiScale(grey_frame, 1.3, 5)
            for (x, y, w, h) in face:
                cv2.imshow("Croppped", frame[y:y + h, x:x + w])
                result = model.predict(cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY))
            confidence = 0
            if result[1] < 500:
                confidence = int(100 * ((1 - result[1] / 300)))
            if confidence > 75:
                cv2.putText(frame, "unlocked " + str(confidence), (400, 450), cv2.FONT_HERSHEY_COMPLEX, 1,
                            (255, 0, 255), 2)
                # cv2.putText(frame, (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                attendence.append("Present")
            else:
                cv2.putText(frame, "locked " + str(confidence), (400, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255),
                            2)
                attendence.append("Absent")
            cv2.imshow("Frame", frame)
        except:
            pass

        if cv2.waitKey(1) == 13 or len(attendence) == 120:
            break
    print(attendence)
    if attendence.count("Present") > 77:
        listy = str(datetime.datetime.now())
        date = listy.split(" ")[0]
        excell = pd.read_excel("a.xlsx")
        columns = list(excell.columns)
        print(columns)
        print(excell)
        workbook = xlsxwriter.Workbook("a.xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.set_column(0, 40, 20)
        for i in range(len(columns)):
            worksheet.write(0, i, columns[i])
            l = list(excell[columns[i]])
            for j in range(len(l)):
                try:
                    worksheet.write(j + 1, i, l[j])
                except:
                    pass
        if date in columns:
            index_row = 0
            l = list(excell[date])
            if np.nan in l:
                index_row = l.index(np.nan)
                index = columns.index(date)
                worksheet.write(index_row + 1, index, Id)
            else:
                index = columns.index(date)
                worksheet.write(len(l) + 1, index, Id)
        else:
            worksheet.write(0, len(columns), date)
            worksheet.write(1, len(columns), Id)
        workbook.close()
        attendency.set("Present")
    else:
        attendency.set("Absent")
    capture.release()
    cv2.destroyAllWindows()
def register_student():
    Name=name_regi.get()
    id=id_regi.get()
    folder = Name.lower() + id.lower()
    try:
        os.mkdir("/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder)
    except:
        print("Folder Already exist")
        exit()
    faces = cv2.CascadeClassifier("frontal_face.xml")
    Capture = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = Capture.read()
        frame = cv2.flip(frame, 1)
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = faces.detectMultiScale(grey_frame, 1.3, 5)
        for (x, y, w, h) in face:
            cv2.imshow("Cropped", frame[y:y + h, x:x + w])
            cv2.imwrite(
                "/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder + "/" + str(
                    count) + ".JPG", cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY))
            count = count + 1
        if cv2.waitKey(1) == 13 or count == 100:
            break
    Capture.release()
    cv2.destroyAllWindows()

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
attendency=StringVar()
attendency.set("")
print(attendency)
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
Button(login,text="Take Attendence",font="arial 12 bold",command=login_student).place(x=160,y=230)
Button(login,text="Register",font="arial 12 bold",command=lambda:raise_frame(register)).place(x=180,y=270)
Entry(login,textvariable=attendency,bg="ghost white").place(x=130,y=330)
Label(register,text="Attendence Marker(IIIT-BH)",font="arial 15 bold").pack(side=TOP)
Label(register,text="Abhinav Gangrade(B118006)",font="arial 15 bold").pack(side=BOTTOM)
Label(register,text="Enter the Name:",font="arial 10 bold").place(x=70,y=120)
Label(register,text="Enter the Id:",font="arial 10 bold").place(x=70,y=170)
Entry(register,textvariable=name_regi,bg="ghost white").place(x=190,y=120)
Entry(register,textvariable=id_regi,bg="ghost white").place(x=190,y=170)
Button(register,text="Register The Student",font="arial 12 bold",command=register_student).place(x=160,y=230)
Button(register,text="Login",font="arial 12 bold",command=lambda:raise_frame(login)).place(x=200,y=270)
root.mainloop()

    result = 0
    attendence = []
    while True:
        try:
            ret, frame = capture.read()
            grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = faces.detectMultiScale(grey_frame, 1.3, 5)
            for (x, y, w, h) in face:
                cv2.imshow("Croppped", frame[y:y + h, x:x + w])
                result = model.predict(cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY))
            confidence = 0
            if result[1] < 500:
                confidence = int(100 * ((1 - result[1] / 300)))
            if confidence > 75:
                cv2.putText(frame, "unlocked " + str(confidence), (400, 450), cv2.FONT_HERSHEY_COMPLEX, 1,
                            (255, 0, 255), 2)
                # cv2.putText(frame, (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                attendence.append("Present")
            else:
                cv2.putText(frame, "locked " + str(confidence), (400, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255),
                            2)
                attendence.append("Absent")
            cv2.imshow("Frame", frame)
        except:
            pass

        if cv2.waitKey(1) == 13 or len(attendence) == 120:
            break
    print(attendence)
    if attendence.count("Present") > 77:
        listy = str(datetime.datetime.now())
        date = listy.split(" ")[0]
        excell = pd.read_excel("a.xlsx")
        columns = list(excell.columns)
        print(columns)
        print(excell)
        workbook = xlsxwriter.Workbook("a.xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.set_column(0, 40, 20)
        for i in range(len(columns)):
            worksheet.write(0, i, columns[i])
            l = list(excell[columns[i]])
            for j in range(len(l)):
                try:
                    worksheet.write(j + 1, i, l[j])
                except:
                    pass
        if date in columns:
            index_row = 0
            l = list(excell[date])
            if np.nan in l:
                index_row = l.index(np.nan)
                index = columns.index(date)
                worksheet.write(index_row + 1, index, Id)
            else:
                index = columns.index(date)
                worksheet.write(len(l) + 1, index, Id)
        else:
            worksheet.write(0, len(columns), date)
            worksheet.write(1, len(columns), Id)
        workbook.close()
    capture.release()
    cv2.destroyAllWindows()
def register_student():
    Name=name_regi.get()
    id=id_regi.get()
    folder = Name.lower() + id.lower()
    try:
        os.mkdir("/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder)
    except:
        print("Folder Already exist")
        exit()
    faces = cv2.CascadeClassifier("frontal_face.xml")
    Capture = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = Capture.read()
        frame = cv2.flip(frame, 1)
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = faces.detectMultiScale(grey_frame, 1.3, 5)
        for (x, y, w, h) in face:
            cv2.imshow("Cropped", frame[y:y + h, x:x + w])
            cv2.imwrite(
                "/home/abhinav/PycharmProjects/Attendance System with the help of opencv]/" + folder + "/" + str(
                    count) + ".JPG", cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY))
            count = count + 1
        if cv2.waitKey(1) == 13 or count == 100:
            break
    Capture.release()
    cv2.destroyAllWindows()

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
Button(login,text="Take Attendence",font="arial 12 bold",command=login_student).place(x=160,y=230)
Button(login,text="Register",font="arial 12 bold",command=lambda:raise_frame(register)).place(x=180,y=270)
Label(register,text="Attendence Marker(IIIT-BH)",font="arial 15 bold").pack(side=TOP)
Label(register,text="Abhinav Gangrade(B118006)",font="arial 15 bold").pack(side=BOTTOM)
Label(register,text="Enter the Name:",font="arial 10 bold").place(x=70,y=120)
Label(register,text="Enter the Id:",font="arial 10 bold").place(x=70,y=170)
Entry(register,textvariable=name_regi,bg="ghost white").place(x=190,y=120)
Entry(register,textvariable=id_regi,bg="ghost white").place(x=190,y=170)
Button(register,text="Register The Student",font="arial 12 bold",command=register_student).place(x=160,y=230)
Button(register,text="Login",font="arial 12 bold",command=lambda:raise_frame(login)).place(x=200,y=270)
root.mainloop()
