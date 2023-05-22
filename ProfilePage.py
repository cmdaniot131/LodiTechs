import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import ImageTk, Image


# Window 
window = ttk.Window(themename= 'superhero')
window.title('Conversatile')
window.geometry('750x1334')

#Profile photo frame
pfp_frame = ttk.Frame(window)

    # Profile photo
pfp = Image.open('img/soy.jpeg')
pfp_resize = pfp.resize((250, 250))
pfp_tk = ImageTk.PhotoImage(pfp_resize)
profile = ttk.Label(pfp_frame, text= 'pfp', image= pfp_tk)

#Profile Info Frame
profinfo_frame = ttk.Frame(window)

    # Username
userlabel_frame = ttk.Labelframe(profinfo_frame, text= 'Username')
user_label = ttk.Label(userlabel_frame, text= 'ANGAS LODS')

    # Email
uemail_frame = ttk.Labelframe(profinfo_frame, text= 'Email')
uemail_label = ttk.Label(uemail_frame, text= 'ANGAS LODS')

    # Phone number
upnum_frame = ttk.Labelframe(profinfo_frame, text= 'Phone Number')
upnum_label = ttk.Label(upnum_frame, text= 'ANGAS LODS')

# Button menu Frame
buttonmenu_frame = ttk.Frame(window)

    # Change password button
password_button = ttk.Button(buttonmenu_frame, text= 'Change Password', width= 15)

    # Edit Profile button
editprofile_button = ttk.Button(buttonmenu_frame, text= 'Edit Profile', width= 15)

    # Back button
back_button = ttk.Button(buttonmenu_frame, text= 'Back', width= 15)

#Layout

    #Profile photo layout
profile.pack(side= 'left', padx= '15', pady= '15')
pfp_frame.pack(fill='both')

    #Info layout
userlabel_frame.pack(fill= 'x', padx= '30', pady='5')
user_label.pack(side= 'left', pady='1')

uemail_frame.pack(fill= 'x', padx= '30', pady='5')
uemail_label.pack(side= 'left', pady='1')

upnum_frame.pack(fill= 'x', padx= '30', pady='5')
upnum_label.pack(side= 'left', pady='1')

profinfo_frame.pack(fill= 'x', pady='5')

    #button menu layout
password_button.pack(pady='5')
editprofile_button.pack(pady='5')
back_button.pack(pady='5')


buttonmenu_frame.pack(expand='true')














#Run
window.mainloop()