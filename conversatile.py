import tkinter as tk
# type the following in PowerShell = "pip install ttkbootstrap" , "pip install customtkinter", "pip install pillow"
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import ImageTk, Image

def credits():
    window.destroy()
    import credits

# Window Changes
window = ttk.Window(themename="vapor")
window.title('Conversatile')
window.geometry('650x950')

# Logo Frame
logo =  Image.open('LodiTechs\Conversatile_Logo.png')
logo_tk = ImageTk.PhotoImage(logo)
label = ttk.Label(window, text = 'logo', image = logo_tk)

# Main Menu Frame
menu_frame = ttk.Frame(window)
button1 = ttk.Button(menu_frame, text = 'PLAY!', width=25)
button2 = ttk.Button(menu_frame, text = 'PROFILE')
button3 = ttk.Button(menu_frame, text = 'CREDITS', command = credits)

#Small buttons
mnMenu_frame = ttk.Frame(window)
mnbutton2 = ttk.Button(mnMenu_frame, text = 'Settings')
mnbutton3 = ttk.Button(mnMenu_frame, text = 'Achievements')

# layout
label.pack()

button1.pack(side = 'top', fill = "both", expand = 'true', pady = '5')
button2.pack(side = 'top', fill = "both", expand = 'true', pady = '5')
button3.pack(side = 'top', fill = "both", expand = 'true', pady = '5')
menu_frame.pack(pady = '50')

mnbutton2.pack(side = 'left', expand = 'true', padx = '25' )
mnbutton3.pack(side = 'left', expand = 'true', padx = '25' )
mnMenu_frame.pack()

# Run
window.mainloop()
