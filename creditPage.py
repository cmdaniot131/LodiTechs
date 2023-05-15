import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import ImageTk, Image

window = ttk.Window(themename="superhero")
window.title('Conversatile')
window.geometry('750x1334')

credit_frame = ttk.Frame(window)
logo =  Image.open('Conversatile\Conversatile_Logo.png')
logo_tk = ImageTk.PhotoImage(logo)
label = ttk.Label(credit_frame, text = 'logo', image = logo_tk)

title = ttk.Label(credit_frame, text = 'Meet the Team behind', font = 'Feather 24 bold')


highlight_frame = ttk.Frame(window)
ld_tech = Image.open('Conversatile\Loditechs_logo.png')
tech_tk = ImageTk.PhotoImage(ld_tech)
ldtech_img = ttk.Label(highlight_frame, text = 'logo', image = tech_tk)

loditech = ttk.Label(highlight_frame, text = 'LodiTech Members', font = 'Feather 20 bold')
name1 = ttk.Label(highlight_frame, text = 'Jwaine Bravo', font = 'Feather 15')
name2 = ttk.Label(highlight_frame, text = 'Chrysler Daniot', font = 'Feather 15')
name3 = ttk.Label(highlight_frame, text = 'Joaquin Rizal', font = 'Feather 15')


# Lay out
title.pack()
label.pack()
credit_frame.pack()

#ldtech_img.pack()
loditech.pack(side = 'top', pady = 15)
name1.pack(side = 'left', padx = 15)
name2.pack(side = 'left', padx = 15)
name3.pack(side = 'left', padx = 15)
highlight_frame.pack()






window.mainloop()