from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.config(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file='login.png')
Label(root, image= img, bg='white').place(x= 50, y= 50)

frame = Frame(root, width= 350, height= 350)
frame.place(x= 480, y= 70)

heading = Label(frame, text='Sign in', fg='#57a1f8', font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x= 120, y= 5)

# username

username_label = Label(frame, text= 'Enter your username', fg='black')
username_label.place(x= 50, y= 65)

username = Entry(frame, width= 25, bg='white', fg='black', relief=RAISED, borderwidth= 0)
username.place(x= 50, y= 100)


#password
password_label = Label(frame, text= 'Enter your password',  fg='black')
password_label.place(x= 50, y= 140)

password = Entry(frame, width= 25, bg='white', fg='black', show= '*', relief=RAISED, borderwidth= 0)
password.place(x= 50, y= 180)

Frame(frame, width= 330, height=2, bg='black').place(x= 10, y = 220)

# sign in button
def signIn():
    username.delete(0, END)
    password.delete(0, END)
    messagebox.showinfo(message='Login succesfull')

sign_in = Button(frame, text='Sign in', width= 23, command= signIn)
sign_in.place(x= 50, y= 244)

# create an account

def createAccount():
    new_root = Toplevel()
    new_root.title('Create account')
    new_root.geometry('925x500+300+200')
    new_root.config(bg='#fff')
    new_root.resizable(False, False)

    Label(new_root, image= img, bg='white').place(x= 50, y= 50)
    new_frame = Frame(new_root, width= 350, height= 400,)
    new_frame.place(x= 480, y= 40)
    new_heading = Label(new_frame, text='Create an account', fg='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold'))
    new_heading.place(x= 70, y= 5)

    # username
    username_label = Label(new_frame, text='Enter a username', fg='black')
    username_label.place(x= 50, y= 65)

    username = Entry(new_frame, width= 25, bg='white', fg='black', relief=RAISED, borderwidth= 0)
    username.place(x= 50, y= 100)

    #password
    password_label = Label(new_frame, text= 'Enter a password', fg='black')
    password_label.place(x= 50, y= 140)

    password = Entry(new_frame, width= 25, bg='white', fg='black', show= '*', relief=RAISED, borderwidth= 0)
    password.place(x= 50, y= 180)

    confirm_pass_label = Label(new_frame, text= 'Confirm your password', fg='black')
    confirm_pass_label.place(x= 50, y=220)

    confirm_pass = Entry(new_frame, width= 25, bg='white', fg='black', show= '*', relief=RAISED, borderwidth= 0)
    confirm_pass.place(x=50, y= 260)

    # button
    create_account_btn = Button(new_frame, text= 'Create my account', width= 23)
    create_account_btn.place(x= 45, y= 300)


create_account = Button(frame, text='Create account', width= 23,command= createAccount)
create_account.place(x= 50, y= 284)


root.mainloop()