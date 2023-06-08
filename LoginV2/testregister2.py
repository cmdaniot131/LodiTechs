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
titleframe = tk.Frame(headerframe, bg='yellow', padx=1, pady=1)
title_label = tk.Label(titleframe, text='Login Page', 
                       padx=20, 
                       pady=5, 
                       bg='green', 
                       fg='#fff', 
                       font=('Tahoma', 16),
                       width = 12
                       )


headerframe.pack()
titleframe.pack()
title_label.pack()


titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)



# ------------- End Header ------------- #

mainframe = tk.Frame(root)

# ------------- Login Page ------------- #
loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(loginframe, 
                       padx=30,
                       pady=100, 
                       highlightbackground='#0000FF',
                       highlightcolor='#0000FF',
                       highlightthickness=2,
                       bg=bgcolor
                       )

username_label = tk.Label(login_contentframe, 
                          text='Username:', 
                          font=('Verdana', 16),
                          bg=bgcolor
                          )
password_label = tk.Label(login_contentframe, 
                          text='Password:', 
                          font=('Verdana', 16),
                          bg=bgcolor
                          )

username_entry = tk.Entry(login_contentframe, font=('Verdana', 16))
password_entry = tk.Entry(login_contentframe, font=('Verdana', 16), show='*')

def show_password():
    if password_entry.cget('show') == '*':
        password_entry.configure(show='')
    else:
        password_entry.configure(show='*')

Check_button=tk.Checkbutton(master=root, 
                         text="SHOW PASSWORD", 
                         command=show_password,
                         font=('Verdana', 8), 
                         fg='Black', 
                         bg=bgcolor,
                         activeforeground='#fff',
                         activebackground='#fff',
                        )
Check_button.place(x=35, y=275)

login_button = tk.Button(login_contentframe, 
                         text='Login', 
                         font=('Verdana', 16), 
                         bg='#2980b9',
                         fg='#fff',
                         padx=25,
                         pady=3,
                         width=25
                         )

rgpagebtn = tk.Button(login_contentframe, 
                         text='Register', 
                         font=('Verdana', 16), 
                         bg='#2980b9',
                         fg='#fff',
                         padx=25,
                         pady=3,
                         width=25
                         )


mainframe.pack(fill='both', expand=1)
loginframe.pack(fill='both', expand=1)
login_contentframe.pack(fill='both', expand=1)

username_label.grid(row=0, column=0, pady=10)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0, pady=10)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, column=0, columnspan=2, pady=30)
rgpagebtn.grid(row=3, column=0, columnspan=2, pady=0)

def go_to_rg():
    root.destroy()
    import testregister3
rgpagebtn['command'] = go_to_rg

def main():
    root.destroy()
    import CONVERSATILE
    CONVERSATILE.main()


# create a function to make the user login
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    vals = (username, password,)
    select_query = "SELECT * FROM `conversatile` WHERE `username` = %s and `password` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        main()  # Call the mainmenu function from within the code
        root.withdraw()  # Hide the root window

    else:
        messagebox.showwarning('Error','Wrong username or password')

login_button['command'] = login

root.mainloop()