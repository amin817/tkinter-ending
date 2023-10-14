from tkinter import *

master = Tk()#class#
master.geometry("800x400")#screen size#
master.title("this is a title!")#title#
master.resizable(width=False,height=False)#screen resizible#

def signUp() :
    username = username_entry.get()
    password = password_entry.get()
    age = ageVar.get()
    nameVar.set(username)
    nameVar2.set(password)
    nameVar3.set(age)
  

username_label = Label(master , text = "username")
username_label.pack(pady = 10)

username_entry = Entry(master)
username_entry.pack()

password_label = Label(master , text = "password")
password_label.pack(pady = 10)

password_entry = Entry(master , show = "*")
password_entry.pack()

age_label = Label(master ,text = "age")
age_label.pack(pady = 10)

ageVar = IntVar()
age_scale = Scale(master , variable = ageVar , from_= 18 , to = 70 , orient= HORIZONTAL).pack()

Register_button = Button(master , text = "signup" , command= signUp).pack(pady = 30)

nameVar = StringVar()
nameVar2 = StringVar()
nameVar3 = StringVar()
label_name = Label(master , textvariable= nameVar)
label_name.place(x = 100 , y =300)
label_name2 = Label(master , textvariable= nameVar2)
label_name2.place(x = 120 , y =300)
label_name3 = Label(master , textvariable= nameVar3)
label_name3.place(x = 140 , y =300)


if __name__ == "__main__":

    master.update_idletasks()#screen update#
    master.mainloop()#app loop#

