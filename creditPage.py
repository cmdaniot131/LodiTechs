import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def mainMenu():
    window.destroy()
    import conversatile

window = tk.Tk()
window.title('Conversatile')
window.geometry('750x1334')


credit_frame = ttk.Frame(window)
logo = Image.open('Conversatile\Conversatile_Logo.png')
resized_logo = logo.resize((300, 300))
logo_tk = ImageTk.PhotoImage(resized_logo)
label = ttk.Label(credit_frame, text='logo', image=logo_tk)
title = ttk.Label(credit_frame, text='Meet the Team behind', font='Feather 24 bold')


highlight_frame = ttk.Frame(window)
ld_tech = Image.open('Conversatile\Loditechs_logo.png')
resized_tech = ld_tech.resize((50, 50))
tech_tk = ImageTk.PhotoImage(resized_tech)
ldtech_img = ttk.Label(highlight_frame, image=tech_tk)
loditech = ttk.Label(highlight_frame, text='LodiTech Members', font='Feather 20 bold')


name_frame = ttk.Frame(window)
name1 = ttk.Label(name_frame, text='Jwaine Bravo', font='Feather 15')
name2 = ttk.Label(name_frame, text='Chrysler Daniot', font='Feather 15')
name3 = ttk.Label(name_frame, text='Joaquin Rizal', font='Feather 15')

button1 = ttk.Button(window, text='Back', width=20, command=mainMenu)

# Layout
title.pack(pady=20)
label.pack()
credit_frame.pack(pady=10)

ldtech_img.pack(side='left')
loditech.pack(pady=10)
highlight_frame.pack(pady=10)


name1.pack(side='left', padx=15)
name2.pack(side='left', padx=15)
name3.pack(side='left', padx=15)
name_frame.pack(pady=10)

button1.pack(pady=20)

window.mainloop()
