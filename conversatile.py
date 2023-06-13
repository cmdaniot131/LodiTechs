import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("theme/conversatile.json")

# Window Changes
window=ctk.CTk() #creating custom tkinter window
window.geometry("470x750'")
window.title("Conversatile")

def to_credit():
    creditPage_frame.pack(fill='both', expand=True)
    mainMenu_frame.pack_forget()

def to_Main():
    mainMenu_frame.pack(fill='both', expand=True)
    creditPage_frame.pack_forget()
    playMenu_frame.pack_forget()

def to_Play():
    playMenu_frame.pack(fill='both', expand=True)
    mainMenu_frame.pack_forget()

def to_leaderboard():
    window.destroy()
    import Leaderboard    



# Frame Declaration
mainMenu_frame = ctk.CTkFrame(window)
creditPage_frame = ctk.CTkFrame(window)
playMenu_frame = ctk.CTkFrame(window)

#--------------------------------------------------------------------------------

# Main Menu 
logoMM = ctk.CTkImage(dark_image=Image.open('img/Conversatile_Logo.png'),
                      size=(300,300))
MM_label = ctk.CTkLabel(mainMenu_frame, image= logoMM, text="")


button1 = ctk.CTkButton(mainMenu_frame, text='PLAY!', width=20, command = to_Play)
button3 = ctk.CTkButton(mainMenu_frame, text='CREDITS', width=20, command = to_credit )
button4 = ctk.CTkButton(mainMenu_frame, text='LEADERBOARD', width=20, command =  to_leaderboard)

# Layout Main Menu
MM_label.pack(pady='30')


button1.pack(fill='x', padx='150')
button3.pack(fill='x', padx='150')
button4.pack(fill='x', padx='150')

mainMenu_frame.pack(fill='both', expand=True,)

#--------------------------------------------------------------------------------

# CREDIT PAGE

credit_frame = ctk.CTkFrame(creditPage_frame)

logoCC = Image.open('img/school.png')
resized_logoCC = logoCC.resize((300, 300))
logo_tkCC = ImageTk.PhotoImage(resized_logoCC)
labelCC = ttk.Label(credit_frame, image=logo_tkCC)
title = ctk.CTkLabel(credit_frame, text='Meet the Team behind')


highlight_frame = ctk.CTkFrame(creditPage_frame)

ld_techMC = Image.open('img/school.png')
resized_techMC = ld_techMC.resize((50, 50))
tech_tk = ImageTk.PhotoImage(resized_techMC)
ldtech_img = ttk.Label(highlight_frame, image=tech_tk)

team = ctk.CTkLabel(highlight_frame, text='Loditech Members')



name_frame = ctk.CTkFrame(creditPage_frame)
name1 = ctk.CTkLabel(name_frame, text='Jwaine Bravo')
name2 = ctk.CTkLabel(name_frame, text='Chrysler Daniot')
name3 = ctk.CTkLabel(name_frame, text='Joaquin Rizal')

button1 = ctk.CTkButton(creditPage_frame, text='Back', width=20, command= to_Main)

# Credit Layout

title.pack(pady=20)
labelCC.pack()
credit_frame.pack(pady=10)

ldtech_img.pack(side='left')
team.pack(pady=10)
highlight_frame.pack(pady=10)


name1.pack(side='left', padx=15)
name2.pack(side='left', padx=15)
name3.pack(side='left', padx=15)
name_frame.pack(pady=10)

button1.pack(pady=20)




#--------------------------------------------------------------------------------

# PLAY MENU

def to_schoolscenario1():
    window.destroy()
    import SchoolScenario1

setting_frame = ctk.CTkFrame(playMenu_frame)
title1 = ctk.CTkLabel(setting_frame, text='Choose Setting')
school_btn = ctk.CTkButton(setting_frame, text='School', width=20, command=to_schoolscenario1)
office_btn = ctk.CTkButton(setting_frame, text='Office', width=20, command=lambda: print('Office Button') )
family_btn = ctk.CTkButton(setting_frame, text='Family', width=20, command=lambda: print('Family Button') )

button1 = ctk.CTkButton(playMenu_frame, text='Back', width=20, command= to_Main)


# Layout
title1.pack()
school_btn.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')
office_btn.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')
family_btn.pack(fill='both', expand=True, pady='5', ipady='15', ipadx='20')
setting_frame.pack()

button1.pack(pady=20)


# Run
window.mainloop()
