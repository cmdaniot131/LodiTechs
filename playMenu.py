import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def mainMenu():
    window.destroy()
    import conversatile

window = tk.Tk()
window.title('Conversatile')
window.geometry('750x1334')

button1 = ttk.Button(window, text='Back', width=20, command=mainMenu)

setting_frame = ttk.Frame(window)
title1 = ttk.Label(setting_frame, text='Choose Setting', font='Feather 15 bold')
school_btn = ttk.Button(setting_frame, text='School', width=20, command=lambda: print('School Button') )
office_btn = ttk.Button(setting_frame, text='Office', width=20, command=lambda: print('Office Button') )
family_btn = ttk.Button(setting_frame, text='Family', width=20, command=lambda: print('Family Button') )


# Layout
title1.pack()
school_btn.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')
office_btn.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')
family_btn.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')
setting_frame.pack()

button1.pack(pady=20)

# run
window.mainloop()