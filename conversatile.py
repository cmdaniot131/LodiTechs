import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def playMenu():
    window.destroy()
    import playMenu

def creditPage():
    window.destroy()
    import creditPage

# Window Changes
window = tk.Tk()
window.title('Conversatile')
window.geometry('750x1334')

# Logo Frame
logo = Image.open('Conversatile\Conversatile_Logo.png')
resized_logo = logo.resize((300, 300))
logo_tk = ImageTk.PhotoImage(resized_logo)
label = ttk.Label(window, text='logo', image=logo_tk)

# Main Menu Frame
menu_frame = ttk.Frame(window)
button1 = ttk.Button(menu_frame, text='PLAY!', width=20, command=playMenu)
button2 = ttk.Button(menu_frame, text='PROFILE', width=20, command=lambda: print('Profile'))
button3 = ttk.Button(menu_frame, text='CREDITS', width=20, command=creditPage)

# Small buttons
mnMenu_frame = ttk.Frame(window)
mnbutton2 = ttk.Button(mnMenu_frame, text='Settings', command=lambda: print('Settings'))
mnbutton3 = ttk.Button(mnMenu_frame, text='Achievements', command=lambda: print('Achievements'))

# Layout
label.pack(pady='30')

menu_frame.pack(pady='50')
button1.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')
button2.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')
button3.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')

mnMenu_frame.pack()
mnbutton2.pack(side='left', padx='25', ipady='15', ipadx='10')
mnbutton3.pack(side='left', padx='25', ipady='15', ipadx='10')

# Run
window.mainloop()
