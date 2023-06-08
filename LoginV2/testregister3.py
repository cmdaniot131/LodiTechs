import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector


root = Tk()
connection = mysql.connector.connect(
    host='localhost', 
    user='root', 
    port='3306', 
    password='', 
    database='conversatile_lg&rg_py'
    ) 
c = connection.cursor()
root.title('CONVERSATILE')
# width and height
w = 450
h = 525
# background color
bgcolor = "#57C5B6"

# ------------- CENTER FORM ------------- #
root.overrideredirect(0)
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# ------------- Header ------------- #

headerframe = tk.Frame(root, 
                       highlightbackground='#0000FF',
                       highlightcolor='#0000FF',
                       highlightthickness=2,
                       bg='#7EC8E3',
                       width=w,
                       height=70
                       )
titleframe = tk.Frame(headerframe, bg='blue', padx=1, pady=1)
title_label = tk.Label(titleframe, text='Register Page', 
                       padx=20, 
                       pady=5, 
                       bg='green', 
                       fg='#fff', 
                       font=('Century Gothic', 16),
                       width = 12
                       )

headerframe.pack()
titleframe.pack()
title_label.pack()


titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)


# ------------- End Header ------------- #

mainframe = tk.Frame(root)

# ------------- Register Page ------------- #

registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(registerframe, 
                       highlightbackground='#0000FF',
                       highlightcolor='#0000FF',
                       highlightthickness=2,
                       padx=15,
                       pady=15, 
                       bg=bgcolor
                       )

username_label_rg = tk.Label(register_contentframe, 
                          text='Username:', 
                          font=('Century Gothic', 14),
                          fg='white',
                          bg=bgcolor
                          )
password_label_rg = tk.Label(register_contentframe, 
                          text='Password:', 
                          font=('Century Gothic', 14),
                          fg='white',
                          bg=bgcolor
                          )
confirmpass_label_rg = tk.Label(register_contentframe, 
                          text='Re-Password:', 
                          font=('Century Gothic', 14),
                          fg='white',
                          bg=bgcolor
                          )

username_entry_rg = tk.Entry(register_contentframe, font=('Century Gothic', 14), width=22)
password_entry_rg = tk.Entry(register_contentframe, font=('Century Gothic', 14), width=22)
confirmpass_entry_rg = tk.Entry(register_contentframe, font=('Century Gothic', 14), width=22)

register_button = tk.Button(register_contentframe, 
                         text='Register', 
                         font=('Century Gothic', 16), 
                         bg='#2980b9',
                         fg='#fff',
                         padx=30,
                         pady=1,
                         width=29
                         )

relogin_button = tk.Button(register_contentframe, 
                         text='Return to Login Page', 
                         font=('Century Gothic', 16), 
                         bg='#2980b9',
                         fg='#fff',
                         padx=30,
                         pady=1,
                         width=29
                         )

mainframe.pack(fill='both', expand=1)
registerframe.pack(fill='both', expand=1)
register_contentframe.pack(fill='both', expand=1)

username_label_rg.grid(row=1, column=0, pady=5, sticky='e')
username_entry_rg.grid(row=1, column=1)

password_label_rg.grid(row=2, column=0, pady=5, sticky='e')
password_entry_rg.grid(row=2, column=1)

confirmpass_label_rg.grid(row=3, column=0, pady=5, sticky='e')
confirmpass_entry_rg.grid(row=3, column=1)

register_button.grid(row=4, column=0, columnspan=2, pady=15)
relogin_button.grid(row=5, column=0, columnspan=2, pady=15)

# -------------  ------------- #

# -------------  ------------- #

def returnlg():
    root.destroy()
    import testregister2
relogin_button['command'] = returnlg

# create a function to check if the username already exists
def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM `conversatile` WHERE `username` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False

# create a function to register a new user
def register():

    username = username_entry_rg.get().strip()
    password = password_entry_rg.get().strip()
    confirm_password = confirmpass_entry_rg.get().strip()
    if len(username) > 0 :
        if check_username(username)  == False:
            if password == confirm_password:
                vals = (username, password)
                insert_query = "INSERT INTO `conversatile`(`username`, `password`) VALUES (%s,%s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo('Register','your account has been created successfully')
            else: 
                messagebox.showwarning('Password','incorrect password confirmation')
        else: messagebox.showwarning('Duplicate Username','Username Already Exsits, try another one')
    else:
        messagebox.showwarning('Register','something went wrong')

register_button['command'] = register 

# -------------  ------------- #

root.mainloop()