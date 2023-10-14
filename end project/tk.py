from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


# Windows [welcome]

class MainFrame(tk.Frame):
    
    def __init__(self , container):
        super().__init__(container)

        self.WELCOME_label = ttk.Label(self , text = "Hello")
        self.WELCOME_label.place(x = 400 ,y = 200)
        self.Button_next = ttk.Button(self , text = "next page" , command = self.next_page ) 



    def next_page(self):

        showinfo(title="Information" , message= "wlecome")

    # def reset(self):
    #     self.WELCOME_label.place(x=250 , y=1000)
    #     self.Button_next.place(x= 250 , y= 1000)



    # def menu1(self):
    #     self.reset()
    #     self.WELCOME_label.place(x = 250 , y= 100)
    #     self.Button_next.place(x= 250 , y = 100)




class Page(tk.Tk):
    
    def __init__(self):
        super().__init__()
    
        self.geometry("800x400")#screen size#
        self.title("SIGN UP PAGE")#title#
        self.resizable(width=False,height=False)#screen resizible#

        
        #LABELS  [USERNAME]
        self.username_label = ttk.Label(self , text = "username")
        self.username_label.pack(pady = 10)


        #ENTRY [NAME]
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        #LABEL [PASSWORD]
        self.password_label = ttk.Label(self , text = "password")
        self.password_label.pack(pady = 10)


        # ENTRY [PASSWORD]
        self.password_entry = ttk.Entry(self , show = "-")
        self.password_entry.pack()

        # LABEL [AGE]
        self.age_label = ttk.Label(self ,text = "age")
        self.age_label.pack(pady = 10)
        
        #Regestr button
        self.Register_button = ttk.Button(self , text = "signup" , command= self.signUp).pack(pady = 30)

        #LABEL [NAME]
        self.nameVar = tk.StringVar()
        self.nameVar2 = tk.StringVar()
        self.nameVar3 = tk.StringVar()
        self.label_name = ttk.Label(self , textvariable= self.nameVar)
        self.label_name.place(x = 100 , y =300)
        self.label_name2 = ttk.Label(self , textvariable= self.nameVar2)
        self.label_name2.place(x = 120 , y =300)
        self.label_name3 = ttk.Label(self , textvariable= self.nameVar3)
        self.label_name3.place(x = 140 , y =300)
        
        self.ageVar = tk.IntVar()
        self.age_scale = tk.Scale(self , variable = self.ageVar , orient=tk.HORIZONTAL, from_= 10 , to = 70 ,)
        self.age_scale.pack()

#Sign up 
    def signUp(self) :
        self.username = username_entry.get()
        self.password = password_entry.get()
        self.age = self.ageVar.get()
        self.nameVar.set(username)
        self.nameVar2.set(password)
        self.nameVar3.set(age)
    
# SCALE [AGE]

# BUTTON [REGISTER]





#OPEN WINDOW AND UPADATE WINDOW
if __name__ == "__main__":

    app =Page()#screen update#
    mf = MainFrame(app)
    app.mainloop()#app loop#

