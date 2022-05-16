from tkinter import Button, Entry, Label, Tk
import pandas as pd
from script import *
# from register import *



# adding the functionality

# for login and automate to all system
def login_and_automate():
    name = entry1.get()
    password = entry2.get()
    data = {
        "user_name":[name],
        "user_password":[password]
    }
    df = pd.DataFrame(data)
    df.to_csv('database.csv',index=False)
    sleep(5)
    login = WebElementBot()
    login.login_user()
    login.edit_profile()
    login.upload_image()
    login.share_profile()
    # login.newsfeed_checker()
    # login.upload_vedio_or_content()


# register and shutdown
def register():
    pass

# designing the ui for the tiktok bot
screen = Tk()
screen.title("Ticktok bot")
screen.config(padx=50,pady=50)
print("hello")


# text and title
label0 = Label(text="Log In",fg='black')
lable1 = Label(text="Enter your phone number or eamil id :", fg='black')
lable2 = Label(text="Enter your facebook password        :", fg='black')
lable3 = Label(text="Enter your phone number or eamil id :", fg='black')
lable4 = Label(text="Enter your facebook password        :", fg='black')
lable5 = Label(text="Sign Up",fg='black')


# input box
entry1 = Entry(width=40)
entry2 = Entry(width=40)
entry3 = Entry(width=40)
entry4 = Entry(width=40)


# button
login = Button(text="Log In",width=20,command=login_and_automate)
signup = Button(text="Sign Up",width=20)


label0.grid(row=0,column=1,pady=10)
lable1.grid(row=1,column=0,pady=10)
lable2.grid(row=2,column=0,pady=10)
lable5.grid(row=3,column=1,pady=10)
lable3.grid(row=4,column=0,pady=10)
lable4.grid(row=5,column=0,pady=10)
entry1.grid(row=1,column=1,pady=10)
entry2.grid(row=2,column=1,pady=10)
entry3.grid(row=4,column=1,pady=10)
entry4.grid(row=5,column=1,pady=10)
login.grid(row=6,column=0,pady=10)
signup.grid(row=6,column=1,pady=10)







# it will keep the screen
screen.mainloop()