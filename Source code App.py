from tkinter import *
import pymongo
from pymongo import collection
import tkinter as tk
import matplotlib.pyplot as plt
from datetime import datetime
root=Tk()
root.minsize(700,400)
root.maxsize(700,400)
root.title("Rain Recorder Program")
root.config(bg="White")


province_namev=StringVar()
province_codev=StringVar()
AvgRainv=StringVar()



client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["DADS5001"]
collection=db["Mini_App_Latthawan"]
def sub():
    dic={
        'province_name':province_namev.get(),
        'province_code':province_codev.get(),
        'AvgRain':AvgRainv.get()
    }
    collection.insert_one(dic)
    
def dele():
    dic1={

        'province_code':province_codev.get(),
    }
    collection.delete_one(dic1)


head=Label(text="โปรแกรมบันทึกข้อมูลปริมาณน้ำฝนเฉลี่ยในประเทศไทย เดือนสิงหาคม ปี 2022",font=("Roboto Mono",12),bg="white")
head.place(x=100,y=25)

#province
province_code=Label(text="รหัสจังหวัด",font=("Roboto Mono",12),bg="white",fg="black")
province_code.place(x=20,y=80)
e2=Entry(font=("Roboto Mono",12),text="province_namev",borderwidth=0.5,width=70)
e2.place(x=25,y=105)

province_name=Label(text="ชื่อจังหวัด",font=("Roboto Mono",12),bg="white",fg="black")
province_name.place(x=20,y=150)
e3=Entry(font=("Roboto Mono",12),text=province_namev,borderwidth=0.5,width=70)
e3.place(x=25,y=190)

#AvgRain
AvgRain=Label(text="ปริมาณน้ำฝนเฉลี่ย",font=("Roboto Mono",12),bg="white",fg="black")
AvgRain.place(x=20,y=220)
e4=Entry(font=("Roboto Mono",12),text=AvgRainv,borderwidth=0.5,width=70)
e4.place(x=25,y=260)



but=Button(text="บันทึกข้อมูล",font=("Roboto Mono",12),command=sub)
but.place(x=80,y=340)
but=Button(text="ลบข้อมูล",font=("Roboto Mono",12),command=dele)
but.place(x=200,y=340)
but=Button(text="Dashboard",font=("Roboto Mono",12))
but.place(x=300,y=340)
but=Button(text="ล้างข้อมูล",font=("Roboto Mono",12),command=dele)
but.place(x=420,y=340)
but=Button(text="ออก",font=("Roboto Mono",12),command=root.destroy)
but.place(x=530,y=340)


root.mainloop()