from tkinter import *
import tkinter
import tkinter as tk
import ttkbootstrap as ttk
import customtkinter
import customtkinter as ctk
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("Dark") #can set light or dark
customtkinter.set_default_color_theme("dark-blue") #themes: blue, dark-blue or green

app=customtkinter.CTk() #creating custom tkinter window
app.geometry("470x750'")
app.title("Conversatile")

#test function not needed
def button_function():
    app.destroy()
    w=customtkinter.CTk()
    w.geometry("1280x720")
    w.title("Welcome")
    l1=customtkinter.CTkLabel(master=w, text="Home Page", font=('Cetury Gothuic', 60))
    l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    w.mainloop()

def CONVERSATILE():
    app.destroy()
    import CONVERSATILE

img1=ImageTk.PhotoImage(Image.open('LodiTechs\CONVERSATILE_BG.png'))
l1=customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account", font=("Century Gothic", 20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password", show='*')
entry2.place(x=50, y=165)

def show_password():
    if entry2.cget('show') == '*':
        entry2.configure(show='')
    else:
        entry2.configure(show='*')

Check_button=Checkbutton(master=frame, 
                         text="show password", 
                         font=("Century Gothic", 11), 
                         fg='white', 
                         bg='#21201E',
                         activeforeground='#21201E',
                         activebackground='#21201E',
                         command=show_password
                        )
Check_button.place(x=65, y=255)

#l2=customtkinter.CTkLabel(master=frame, text="Sign In", font=("Century Gothic", 12))
#l2.place(x=165, y=195)

button1=customtkinter.CTkButton(master=frame, width=220, 
                                text='Login', 
                                corner_radius=6, 
                                text_color='Black', 
                                fg_color='white', 
                                hover_color="#A4A4A4", 
                                command=CONVERSATILE
                                )
button1.place(x=50, y=240)

img2=customtkinter.CTkImage(Image.open('LodiTechs\GOOG.png').resize((20,20), Image.ANTIALIAS))
img3=customtkinter.CTkImage(Image.open('LodiTechs\Facebook_Logo_(2019).png').resize((20,20), Image.ANTIALIAS))


button2=customtkinter.CTkButton(master=frame, 
                                image=img2, text="Google", 
                                width=100, height=20, 
                                corner_radius=6, 
                                compound='left', 
                                text_color='Black', 
                                fg_color='white', 
                                hover_color="#A4A4A4"
                                )
button2.place(x=50, y=290)

button3=customtkinter.CTkButton(master=frame, 
                                image=img3, 
                                text="Facebook", 
                                width=100, 
                                height=20, 
                                corner_radius=6, 
                                compound='left', 
                                text_color='Black', 
                                fg_color='white', 
                                hover_color="#A4A4A4"
                                )
button3.place(x=170, y=290)


app.mainloop()
