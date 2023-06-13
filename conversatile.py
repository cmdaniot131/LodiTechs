import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("theme/conversatile.json")

# Window Changes
window=ctk.CTk() #creating custom tkinter window
window.geometry("470x750'")
window.title("Conversatile")

#Database
db = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='02blz002', 
    database='conversatile_db'
    )

conversatile = db.cursor()


#Switch pages

def to_credit():
    creditPage_frame.pack(fill='both', expand=True)
    mainMenu_frame.pack_forget()

def to_Main():
    mainMenu_frame.pack(fill='both', expand=True)
    LoginPage_Frame.pack_forget()
    creditPage_frame.pack_forget()
    lbd_frame.pack_forget()
    playMenu_frame.pack_forget()
    

def to_Play():
    playMenu_frame.pack(fill='both', expand=True)
    mainMenu_frame.pack_forget()
 



# Frame Declaration
LoginPage_Frame = ctk.CTkFrame(window)
RegisterPage_Frame = ctk.CTkFrame(window)
mainMenu_frame = ctk.CTkFrame(window)
creditPage_frame = ctk.CTkFrame(window)
lbd_frame = ctk.CTkFrame(window)
playMenu_frame = ctk.CTkFrame(window)
SchoolScenario1_frame = ctk.CTkFrame(window)

#--------------------------------------------------------------------------------------------------

# Login Page

# ------------- Header ------------- #

Ltitleframe = ctk.CTkFrame(LoginPage_Frame)

Lheader_label = ctk.CTkLabel(Ltitleframe, text='Login Page', font=("",30))

# Header layout
Lheader_label.pack()

Ltitleframe.pack(fill='both', pady='100')

# ------------- End Header ------------- #

Lmainframe = ctk.CTkFrame(LoginPage_Frame)

# ------------- Login Page ------------- #

# Login Page Functions

def go_to_rg():
    RegisterPage_Frame.pack(fill='both', expand=True)
    LoginPage_Frame.pack_forget()


# create a function to make the user login
def login():
    global user_id
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    select_query = "SELECT * FROM usercredentials_tbl WHERE username = %s AND password = %s"
    conversatile.execute(select_query, (username, password))
    user = conversatile.fetchone()
    if user is not None:
        user_id = user[0]
        to_Main()  # Call the mainmenu function from within the code

    else:
        messagebox.showwarning('Error','Wrong username or password')



# Login widgets

login_frame = ctk.CTkFrame(LoginPage_Frame)

username_entry = ctk.CTkEntry(login_frame, placeholder_text="Username")
password_entry = ctk.CTkEntry(login_frame, placeholder_text="Password", show='*')

def show_password():
    if password_entry.cget('show') == '*':
        password_entry.configure(show='')
    else:
        password_entry.configure(show='*')

Check_button= ctk.CTkSwitch(login_frame, 
                         text="SHOW PASSWORD", 
                         command=show_password)

# login and register button
login_button = ctk.CTkButton(login_frame, 
                         text='Login',
                         font=("", 20),
                         command= login)

register_button = ctk.CTkButton(login_frame, 
                         text='Register',
                         font=("", 20),
                         command= go_to_rg)

# Login Page layout
username_entry.pack(fill='x', padx='150', pady='15')

password_entry.pack(fill='x', padx='150', pady='15')

Check_button.pack(fill='x', padx='150', pady='15')

login_button.pack(pady='10')
register_button.pack(pady='10')

login_frame.pack(fill='both', expand=True)
Lmainframe.pack(fill='both', expand=True)

LoginPage_Frame.pack(fill='both', expand=True)

#--------------------------------------------------------------------------------------------------

# Register Page
# ------------- Header ------------- #

Rheaderframe = ctk.CTkFrame(RegisterPage_Frame)
Rheader_label = ctk.CTkLabel(Rheaderframe, text='Register Page', font=("",30))

# Header layout
Rheader_label.pack()

Rheaderframe.pack(fill='both', pady='100')


# ------------- End Header ------------- #

Rmainframe = ctk.CTkFrame(RegisterPage_Frame)

# ------------- Register Page ------------- #

register_frame = ctk.CTkFrame(Rmainframe)

username_entry_rg = ctk.CTkEntry(register_frame, placeholder_text="Username")
password_entry_rg = ctk.CTkEntry(register_frame, placeholder_text="Password")
confirmpass_entry_rg = ctk.CTkEntry(register_frame, placeholder_text="Confirm Password")

# Register Functions
def returnlg():
    LoginPage_Frame.pack(fill='both', expand=True)
    RegisterPage_Frame.pack_forget()

# create a function to check if the username already exists
def check_username(username):
    username = username_entry_rg.get().strip()
    select_query = "SELECT * FROM usercredentials_tbl WHERE username = %s"
    conversatile.execute(select_query, (username,))
    user = conversatile.fetchone()
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
                insert_query = "INSERT INTO usercredentials_tbl (username, password) VALUES (%s,%s)"
                conversatile.execute(insert_query, (username, password))
                db.commit()
                messagebox.showinfo('Register','your account has been created successfully')
            else: 
                messagebox.showwarning('Password','incorrect password confirmation')
        else: messagebox.showwarning('Duplicate Username','Username Already Exsits, try another one')
    else:
        messagebox.showwarning('Register','something went wrong')

register_button = ctk.CTkButton(register_frame, 
                         text='Register', command= register)

relogin_button = ctk.CTkButton(register_frame, 
                         text='Return to Login Page', 
                         command= returnlg)

Rmainframe.pack(fill='both', expand=1)
register_frame.pack(fill='both', expand=1)

username_entry_rg.pack(fill='x', padx='150', pady='15')
password_entry_rg.pack(fill='x', padx='150', pady='15')
confirmpass_entry_rg.pack(fill='x', padx='150', pady='15')

register_button.pack(pady='10')
relogin_button.pack(pady='10')

#--------------------------------------------------------------------------------------------------



# CREDIT PAGE

credit_frame = ctk.CTkFrame(creditPage_frame)

logoCC = ctk.CTkImage(dark_image=Image.open('img/Conversatile_Logo.png'),
                      size=(300,300))
labelCC = ctk.CTkLabel(credit_frame, image=logoCC, text="")
title = ctk.CTkLabel(credit_frame, text='Meet the Team behind', font=("", 20))


highlight_frame = ctk.CTkFrame(creditPage_frame)

ld_techlogo = ctk.CTkImage(dark_image=Image.open('img/LodiTechs_Logo.png'),
                      size=(50,50))
ldtech_img = ctk.CTkLabel(highlight_frame, image=ld_techlogo, text="")

team_label = ctk.CTkLabel(highlight_frame, text='   Loditech Members', font=("", 16))



name_frame = ctk.CTkFrame(creditPage_frame)
name1 = ctk.CTkLabel(name_frame, text='Jwaine Bravo', font=("", 16))
name2 = ctk.CTkLabel(name_frame, text='Chrysler Daniot', font=("", 16))
name3 = ctk.CTkLabel(name_frame, text='Joaquin Rizal', font=("", 16))

button1 = ctk.CTkButton(creditPage_frame, text='Back', width=20, command= to_Main)

# Credit Layout

title.pack(pady=5)
labelCC.pack()
credit_frame.pack(pady=10)

ldtech_img.pack(side='left')
team_label.pack(pady=10)
highlight_frame.pack(pady=10)


name1.pack(side='left', padx=15)
name2.pack(side='left', padx=15)
name3.pack(side='left', padx=15)
name_frame.pack(pady=10)

button1.pack(ipadx='20', pady=50)

#--------------------------------------------------------------------------------

# Leaderbords
def to_leaderboard():
    lbd_frame.pack(fill='both', expand=True)
    mainMenu_frame.pack_forget() 

    # Leaderboard label
    lbd_label = ctk.CTkLabel(lbd_frame, text="LEADERBOARD", font=("", 30))

    # Leaderboard access database
    conversatile.execute("SELECT usercredentials_tbl.username, scenario1_tbl.total_score "
                        "FROM usercredentials_tbl "
                        "JOIN scenario1_tbl ON usercredentials_tbl.user_id = scenario1_tbl.user_id "
                        "ORDER BY scenario1_tbl.total_score DESC "
                        "LIMIT 10")

    leaderboard_entries = conversatile.fetchall()

    # Leaderboard variables
    top10_entries = []
    for entry in leaderboard_entries:
        username = entry[0]
        score = entry[1]
        top10_entries.append(f"{username} | {score}")

    # Leaderboard entry labels
    lbd_entry_labels = []
    for i in range(10):
        if i < len(top10_entries):
            lbd_entry_labels.append(ctk.CTkLabel(lbd_frame, anchor="w", text=f"{i + 1}. {top10_entries[i]}", fg_color="#FFFFFF",
                                                corner_radius=15, font=("", 20)))
        else:
            lbd_entry_labels.append(ctk.CTkLabel(lbd_frame, text=f"{i + 1}.", fg_color="#FFFFFF", corner_radius=15,
                                                font=("", 20)))
    #back to main menu
    b2mm_button = ctk.CTkButton(lbd_frame, text="Back", font=("", 20), command= to_Main)

    #Leaderboard layout
    lbd_label.pack(pady='30')

    for label in lbd_entry_labels:
        label.pack(fill='x', padx='190', pady='15')

    b2mm_button.pack(fill='x', padx='100', pady='25')

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


button1.pack(fill='x', padx='150', pady='15')
button3.pack(fill='x', padx='150', pady='15')
button4.pack(fill='x', padx='150', pady='15')


#--------------------------------------------------------------------------------

# PLAY MENU

def to_schoolscenario1():
    SchoolScenario1_frame.pack(fill='both', expand=True)
    playMenu_frame.pack_forget()

setting_frame = ctk.CTkFrame(playMenu_frame)
title1 = ctk.CTkLabel(setting_frame, text='Choose Setting', font=("",30))
school_btn = ctk.CTkButton(setting_frame, text='School', width=24, command=to_schoolscenario1)
office_btn = ctk.CTkButton(setting_frame, text='Office', width=24, command=lambda: print('Office Button') )
family_btn = ctk.CTkButton(setting_frame, text='Family', width=24, command=lambda: print('Family Button') )

button1 = ctk.CTkButton(setting_frame, text='Back', width=24, command= to_Main)


# Layout
title1.pack(pady='15')
school_btn.pack(fill='x', expand=True, pady='5', ipady='15', ipadx='20')
office_btn.pack(fill='x', expand=True, pady='5', ipady='15', ipadx='20')
family_btn.pack(fill='x', expand=True, pady='5', ipady='15', ipadx='20')
button1.pack(fill='x', expand=True, pady=20)
setting_frame.pack()



#--------------------------------------------------------------------------------

#School Scenario 1
zeroframe = ctk.CTkFrame(SchoolScenario1_frame)
firstframe = ctk.CTkFrame(SchoolScenario1_frame)
secondframe = ctk.CTkFrame(SchoolScenario1_frame)
thirdframe = ctk.CTkFrame(SchoolScenario1_frame)
fourthframe = ctk.CTkFrame(SchoolScenario1_frame)
fifthframe = ctk.CTkFrame(SchoolScenario1_frame)
sixthframe = ctk.CTkFrame(SchoolScenario1_frame)
seventhframe = ctk.CTkFrame(SchoolScenario1_frame)
eightframe = ctk.CTkFrame(SchoolScenario1_frame)
ninthframe = ctk.CTkFrame(SchoolScenario1_frame)
tenthframe = ctk.CTkFrame(SchoolScenario1_frame)

passedframe = ctk.CTkFrame(SchoolScenario1_frame)
failedframe = ctk.CTkFrame(SchoolScenario1_frame)

def back_to_scenario_menu():
    playMenu_frame.pack(fill='both', expand=True)
    SchoolScenario1_frame.pack_forget()

#zeroframe-----------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame0 = ctk.CTkFrame(zeroframe)

    #Image visual
visual0 = ctk.CTkImage(dark_image=Image.open('img/Situation 1.jpg'),
                      size=(450,300))
visual_label0 = ctk.CTkLabel(visual_frame0, image= visual0, text="")

#Problem window frame
problem_frame0 = ctk.CTkFrame(zeroframe)

    #Problem window
problem_label0 = ctk.CTkLabel(problem_frame0, anchor= "e", font= ('Arial',16), justify= "left",
                          text= "It's the first day of school and you want to make friends, \nbut you must act quick. People tend to establish their \nfriendship circles in 3 days making it tougher to join \nthem the longer you hesitate." 
                          )

#Options buttons frame
optionbutton_frame0 = ctk.CTkFrame(zeroframe)

#next function

def change_to_firstframe():
    firstframe.pack(fill="both", expand= True)
    zeroframe.pack_forget()

#next button

next_button = ctk.CTkButton(optionbutton_frame0, text="NEXT", command= change_to_firstframe)

#Layout for zeroframe

    #Image visual layout
visual_label0.pack()
visual_frame0.pack(pady= '30')

    #Problem window layout
problem_label0.pack(padx='10')
problem_frame0.pack(pady='10')

    #Next Button layout
next_button.pack(padx='70', pady='100', fill='x',expand= True)
optionbutton_frame0.pack(fill='both', expand= True)

#first frame
zeroframe.pack(fill="both", expand= True)

#firstframe-----------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame = ctk.CTkFrame(firstframe)

    #Image visual
visual = ctk.CTkImage(dark_image=Image.open('img/S1_Act1.jpg'),
                      size=(450,300))
visual_label = ctk.CTkLabel(visual_frame, image= visual, text="")

#Problem window frame
problem_frame = ctk.CTkFrame(firstframe,)

    #Problem window
problem_label = ctk.CTkLabel(problem_frame, anchor= "e", font= ('Arial',16), justify= "left",
                          text= "You found someone interesting and mustered up your courage, \nbut you can't just approach someone without having \nanything to say."
                          )

#Options buttons frame
optionbutton_frame = ctk.CTkFrame(firstframe)

    #Options buttons label
what_label = ctk.CTkLabel(optionbutton_frame, text="What should you do?", font= ('Arial',15))


#option functions


finalscore = 0

def act1_bestoption():
    global finalscore
    finalscore += 5
    secondframe.pack(fill='both', expand= True)
    firstframe.pack_forget()

    

def act1_betteroption():
    global finalscore
    finalscore += 4
    secondframe.pack(fill='both', expand= True)
    firstframe.pack_forget()    

def act1_goodoption():
    global finalscore
    finalscore += 3
    secondframe.pack(fill='both', expand= True)
    firstframe.pack_forget()

def act1_badoption():
    global finalscore
    finalscore += 1
    secondframe.pack(fill='both', expand= True)
    firstframe.pack_forget()



    #Option buttons 
Option1_button = ctk.CTkButton(optionbutton_frame, text="Approach them but don't say anything until they do.", width= 45, command= act1_goodoption)
Option2_button = ctk.CTkButton(optionbutton_frame, text="Join in a random conversation and take over.", width= 45, command= act1_badoption)
Option3_button = ctk.CTkButton(optionbutton_frame, text="Observe, Approach, and Introduce yourself.", width= 45, command= act1_bestoption)
Option4_button = ctk.CTkButton(optionbutton_frame, text="Gamble your odds and let them come to you first.", width= 45, command= act1_betteroption)


#Layout for firstframe

    #Image visual layout
visual_label.pack()
visual_frame.pack(pady= '30')

    #Problem window layout
problem_label.pack(padx='10')
problem_frame.pack(pady='10')

    #Options label layout
what_label.pack(pady='10')
    #Option Button layout
Option1_button.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame.pack(fill= 'x', expand= True)



#secondframe----------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame2 = ctk.CTkFrame(secondframe)

    #Image visual
visual2 = ctk.CTkImage(dark_image=Image.open('img/S1_Act2.jpg'),
                      size=(450,300))
visual_label2 = ctk.CTkLabel(visual_frame2, image= visual2, text="")

#Problem window frame
problem_frame2 = ctk.CTkFrame(secondframe)

    #Problem window
problem_label2 = ctk.CTkLabel(problem_frame2, anchor= "e", font= ('Arial',18),
                          text= "Looks like they're friendly enough to talk to…"
                          )

#Options buttons frame
optionbutton_frame2 = ctk.CTkFrame(secondframe)

    #Options buttons label
what_label2 = ctk.CTkLabel(optionbutton_frame2, text="How should you talk to them?", font= ('Arial',20))


#option button functions

def act2_bestoption():
    global finalscore
    finalscore += 5
    thirdframe.pack(fill='both', expand= True)
    secondframe.pack_forget()

def act2_betteroption():
    global finalscore
    finalscore += 4
    thirdframe.pack(fill='both', expand= True)
    secondframe.pack_forget()    

def act2_goodoption():
    global finalscore
    finalscore += 3
    thirdframe.pack(fill='both', expand= True)
    secondframe.pack_forget()
def act2_badoption():
    global finalscore
    finalscore += 1
    thirdframe.pack(fill='both', expand= True)
    secondframe.pack_forget()

    #Option buttons 
Option1_button2 = ctk.CTkButton(optionbutton_frame2, text="Hi! I see that you like (Thing observed), I also like \n(Common Interest). I'm (username) by the way, \nnice to meet you!", width= 45, command= act2_betteroption)
Option2_button2 = ctk.CTkButton(optionbutton_frame2, text="I remember when I had (recall experience \nabout common interest), it was cool. \nOh, I'm (username), how about you?", width= 45, command= act2_goodoption)
Option3_button2 = ctk.CTkButton(optionbutton_frame2, text="Oh I really like (common interest), I see you have great taste. \nI'm (username). How did you get started with \n(common interest)?", width= 45, command= act2_bestoption)
Option4_button2 = ctk.CTkButton(optionbutton_frame2, text="I don't really like it because of... Why do you even like it? \nI'm (username) by the way.", width= 45, command= act2_badoption)


#Layout for secondframe

    #Image visual layout
visual_label2.pack()
visual_frame2.pack(pady= '50')

#Problem window layout
problem_label2.pack(padx='10')
problem_frame2.pack(pady='10')

    #Options label layout
what_label2.pack(pady='10')
    #Option Button layout
Option1_button2.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button2.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button2.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button2.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame2.pack(fill= 'x', expand= True)


#thirdframe------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame3 = ctk.CTkFrame(thirdframe)

    #Image visual
visual3 = ctk.CTkImage(dark_image=Image.open('img/S1_Act3.jpg'),
                      size=(450,300))
visual_label3 = ctk.CTkLabel(visual_frame3, image= visual3, text="")

#Problem window frame
problem_frame3 = ctk.CTkFrame(thirdframe)

    #Problem window
problem_label3 = ctk.CTkLabel(problem_frame3, font= ('Arial',18),
                          text= "Looks like they are uncomfortable or straight up ignored you…"
                          )

#Options buttons frame
optionbutton_frame3 = ctk.CTkFrame(thirdframe)

    #Options buttons label
what_label3 = ctk.CTkLabel(optionbutton_frame3, text="What should you do?", font= ('Arial',20))

#option button functions

def act3_bestoption():
    global finalscore
    finalscore += 5
    fourthframe.pack(fill='both', expand= True)
    thirdframe.pack_forget()

def act3_betteroption():
    global finalscore
    finalscore += 4
    fourthframe.pack(fill='both', expand= True)
    thirdframe.pack_forget()   

def act3_goodoption():
    global finalscore
    finalscore += 3
    fourthframe.pack(fill='both', expand= True)
    thirdframe.pack_forget()

def act3_badoption():
    global finalscore
    finalscore += 1
    fourthframe.pack(fill='both', expand= True)
    thirdframe.pack_forget()

    #Option buttons 
Option1_button3 = ctk.CTkButton(optionbutton_frame3, text="Sorry for bothering you, I will go now.", width= 45, command= act3_bestoption)
Option2_button3 = ctk.CTkButton(optionbutton_frame3, text="Keep talking and they'll eventually warm up to you.", width= 45, command= act3_betteroption)
Option3_button3 = ctk.CTkButton(optionbutton_frame3, text="Cuss them out for not being interested in you.", width= 45, command= act3_badoption)
Option4_button3 = ctk.CTkButton(optionbutton_frame3, text="Stay silent and just wait for them to excuse themselves.", width= 45, command= act3_goodoption)


#Layout for thirdframe

    #Image visual layout
visual_label3.pack()
visual_frame3.pack(pady= '50')

#Problem window layout
problem_label3.pack(padx='10')
problem_frame3.pack(pady='10')

    #Options label layout
what_label3.pack(pady='10')
    #Option Button layout
Option1_button3.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button3.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button3.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button3.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame3.pack(fill= 'x', expand= True)



#fourthframe------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame4 = ctk.CTkFrame(fourthframe)

    #Image visual
visual4 = ctk.CTkImage(dark_image=Image.open('img/S1_Act4.jpg'),
                      size=(450,300))
visual_label4 = ctk.CTkLabel(visual_frame4, image= visual4, text="")

#Problem window frame
problem_frame4 = ctk.CTkFrame(fourthframe)

    #Problem window
problem_label4 = ctk.CTkLabel(problem_frame4, anchor= "e", font= ('Arial',18),
                          text= "It turns out, you didn't like them…"
                          )

#Options buttons frame
optionbutton_frame4 = ctk.CTkFrame(fourthframe)

    #Options buttons label
what_label4 = ctk.CTkLabel(optionbutton_frame4, text="What should you do?", font= ('Arial',20))

option3_var = (" 'Hey, don't mean to offend you \nbut I just don't like you, maybe we should stop talking.'")

#option buttons function

def act4_bestoption():
    global finalscore
    finalscore += 5
    fifthframe.pack(fill='both', expand= True)
    fourthframe.pack_forget()

def act4_betteroption():
    global finalscore
    finalscore += 4
    fifthframe.pack(fill='both', expand= True)
    fourthframe.pack_forget()   

def act4_goodoption():
    global finalscore
    finalscore += 3
    fifthframe.pack(fill='both', expand= True)
    fourthframe.pack_forget()

def act4_badoption():
    global finalscore
    finalscore += 1
    fifthframe.pack(fill='both', expand= True)
    fourthframe.pack_forget()
    

    #Option buttons 
Option1_button4 = ctk.CTkButton(optionbutton_frame4, text="Look at your phone then say \n'Sorry, something came up I have to go now.'", width= 45, command= act4_bestoption)
Option2_button4 = ctk.CTkButton(optionbutton_frame4, text="Fake it till you make it.", width= 45, command= act4_betteroption)
Option3_button4 = ctk.CTkButton(optionbutton_frame4, text="Be straightforward and say" + f"{option3_var}", width= 45, command= act4_goodoption)
Option4_button4 = ctk.CTkButton(optionbutton_frame4, text="Just leave.", width= 45, command= act4_badoption)


#Layout for fourthframe

    #Image visual layout
visual_label4.pack()
visual_frame4.pack(pady= '50')

#Problem window layout
problem_label4.pack(padx='10')
problem_frame4.pack(pady='10')

    #Options label layout
what_label4.pack(pady='10')
    #Option Button layout
Option1_button4.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button4.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button4.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button4.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame4.pack(fill= 'x', expand= True)



#fifthframe-----------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame5 = ctk.CTkFrame(fifthframe)

    #Image visual
visual5 = ctk.CTkImage(dark_image=Image.open('img/S1_Act5.jpg'),
                      size=(450,300))
visual_label5 = ctk.CTkLabel(visual_frame5, image= visual5, text="")

#Problem window frame
problem_frame5 = ctk.CTkFrame(fifthframe)

    #Problem window
problem_label5 = ctk.CTkLabel(problem_frame5, anchor= "e", font= ('Arial',16),
                          text= "They turned out to be friendly! Your next goal is to get their name \nand how to contact them, easy right?"
                          )

#Options buttons frame
optionbutton_frame5 = ctk.CTkFrame(fifthframe)

    #Options buttons label
what_label5 = ctk.CTkLabel(optionbutton_frame5, text="What should you say?", font= ('Arial',20))

#option buttons function


def act5_bestoption():
    global finalscore
    finalscore += 5
    sixthframe.pack(fill="both", expand= True)
    fifthframe.pack_forget()

def act5_betteroption():
    global finalscore
    finalscore += 4
    sixthframe.pack(fill="both", expand= True)
    fifthframe.pack_forget()

def act5_goodoption():
    global finalscore
    finalscore += 3
    sixthframe.pack(fill="both", expand= True)
    fifthframe.pack_forget()
    

def act5_badoption():
    global finalscore
    finalscore += 1
    sixthframe.pack(fill="both", expand= True)
    fifthframe.pack_forget()

    #Option buttons 
Option1_button5 = ctk.CTkButton(optionbutton_frame5, text="Oh hey, I didn't catch your name, also would you mind \nif we add each other on social media?", width= 45, command= act5_bestoption)
Option2_button5 = ctk.CTkButton(optionbutton_frame5, text="Wait for them to offer adding you to socials\n and know their name on there.", width= 45, command= act5_badoption)
Option3_button5 = ctk.CTkButton(optionbutton_frame5, text="Hey want to add each other on social media?", width= 45, command= act5_betteroption)
Option4_button5 = ctk.CTkButton(optionbutton_frame5, text="Oh wait, let me guess what your name is!", width= 45, command= act5_goodoption)


#Layout for fifthframe

    #Image visual layout
visual_label5.pack()
visual_frame5.pack(pady= '50')

#Problem window layout
problem_label5.pack(padx='10')
problem_frame5.pack(pady='10')

    #Options label layout
what_label5.pack(pady='10')
    #Option Button layout
Option1_button5.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button5.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button5.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button5.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame5.pack(fill= 'x', expand= True)

#sixthframe--------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame6 = ctk.CTkFrame(sixthframe)

    #Image visual
visual6 = ctk.CTkImage(dark_image=Image.open('img/S1_Act6.jpg'),
                      size=(450,300))
visual_label6 = ctk.CTkLabel(visual_frame6, image= visual6, text="")

#Problem window frame
problem_frame6 = ctk.CTkFrame(sixthframe)

    #Problem window
problem_label6 = ctk.CTkLabel(problem_frame6, anchor= "e", font= ('Arial',16),
                          text= "You and your new friend made quite \na connection about a common interest! "
                          )

#Options buttons frame
optionbutton_frame6 = ctk.CTkFrame(sixthframe)

    #Options buttons label
what_label6 = ctk.CTkLabel(optionbutton_frame6, text="What should you do?", font= ('Arial',20))

#option buttons function


def act6_bestoption():
    global finalscore
    finalscore += 5
    seventhframe.pack(fill="both", expand= True)
    sixthframe.pack_forget()

def act6_betteroption():
    global finalscore
    finalscore += 4
    seventhframe.pack(fill="both", expand= True)
    sixthframe.pack_forget()

def act6_goodoption():
    global finalscore
    finalscore += 3
    seventhframe.pack(fill="both", expand= True)
    sixthframe.pack_forget()
    

def act6_badoption():
    global finalscore
    finalscore += 1
    seventhframe.pack(fill="both", expand= True)
    sixthframe.pack_forget()

    #Option buttons 
Option1_button6 = ctk.CTkButton(optionbutton_frame6, text="Stay with the same topic and just expand on it.", width= 45, command= act6_goodoption)
Option2_button6 = ctk.CTkButton(optionbutton_frame6, text="End the conversation.", width= 45, command= act6_badoption)
Option3_button6 = ctk.CTkButton(optionbutton_frame6, text="Think about another interest that you and \nthey could potentially talk about.", width= 45, command= act6_bestoption)
Option4_button6 = ctk.CTkButton(optionbutton_frame6, text="Talk about the weather.", width= 45, command= act6_betteroption)


#Layout for sixthframe

    #Image visual layout
visual_label6.pack()
visual_frame6.pack(pady= '50')

#Problem window layout
problem_label6.pack(padx='10')
problem_frame6.pack(pady='10')

    #Options label layout
what_label6.pack(pady='10')
    #Option Button layout
Option1_button6.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button6.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button6.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button6.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame6.pack(fill= 'x', expand= True)

#seventhframe--------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame7 = ctk.CTkFrame(seventhframe)

    #Image visual
visual7 = ctk.CTkImage(dark_image=Image.open('img/S1_Act7.jpg'),
                      size=(450,300))
visual_label7 = ctk.CTkLabel(visual_frame7, image= visual7, text="")

#Problem window frame
problem_frame7 = ctk.CTkFrame(seventhframe)

    #Problem window
problem_label7 = ctk.CTkLabel(problem_frame7, anchor= "e", justify= "left", font= ('Arial',16),
                          text= "Someone overheard your conversation, and a stranger \nsuddenly joins in the conversation and introduces \nthemselves. (They look friendly as well)"
                          )

#Options buttons frame
optionbutton_frame7 = ctk.CTkFrame(seventhframe)

    #Options buttons label
what_label7 = ctk.CTkLabel(optionbutton_frame7, text="What should you say?", font= ('Arial',20))

#option buttons function


def act7_bestoption():
    global finalscore
    finalscore += 5
    eightframe.pack(fill="both", expand= True)
    seventhframe.pack_forget()

def act7_betteroption():
    global finalscore
    finalscore += 4
    eightframe.pack(fill="both", expand= True)
    seventhframe.pack_forget()

def act7_goodoption():
    global finalscore
    finalscore += 3
    eightframe.pack(fill="both", expand= True)
    seventhframe.pack_forget()
    

def act7_badoption():
    global finalscore
    finalscore += 1
    eightframe.pack(fill="both", expand= True)
    seventhframe.pack_forget()

    #Option buttons 
Option1_button7 = ctk.CTkButton(optionbutton_frame7, text="I'm (username), Nice to meet you! We're just talking \nabout our interests, do you like …?", width= 45, command= act7_bestoption)
Option2_button7 = ctk.CTkButton(optionbutton_frame7, text="…", width= 45, command= act7_badoption)
Option3_button7 = ctk.CTkButton(optionbutton_frame7, text="Uhm, excuse us please.", width= 45, command= act7_goodoption)
Option4_button7 = ctk.CTkButton(optionbutton_frame7, text="Oh hey, have you heard about…", width= 45, command= act7_betteroption)


#Layout for seventhframe

    #Image visual layout
visual_label7.pack()
visual_frame7.pack(pady= '50')

#Problem window layout
problem_label7.pack(padx='10')
problem_frame7.pack(pady='10')

    #Options label layout
what_label7.pack(pady='10')
    #Option Button layout
Option1_button7.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button7.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button7.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button7.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame7.pack(fill= 'x', expand= True)

#eighthframe--------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame8 = ctk.CTkFrame(eightframe)

    #Image visual
visual8 = ctk.CTkImage(dark_image=Image.open('img/S1_Act8.jpg'),
                      size=(450,300))
visual_label8 = ctk.CTkLabel(visual_frame8, image= visual8, text="")

#Problem window frame
problem_frame8 = ctk.CTkFrame(eightframe)

    #Problem window
problem_label8 = ctk.CTkLabel(problem_frame8, anchor= "e", font= ('Arial',16),
                          text= " A person approaches you and makes a creepy joke."
                          )

#Options buttons frame
optionbutton_frame8 = ctk.CTkFrame(eightframe)

    #Options buttons label
what_label8 = ctk.CTkLabel(optionbutton_frame8, text="What should you do?", font= ('Arial',20))

#option buttons function


def act8_bestoption():
    global finalscore
    finalscore += 5
    ninthframe.pack(fill="both", expand= True)
    eightframe.pack_forget()

def act8_betteroption():
    global finalscore
    finalscore += 4
    ninthframe.pack(fill="both", expand= True)
    eightframe.pack_forget()

def act8_goodoption():
    global finalscore
    finalscore += 3
    ninthframe.pack(fill="both", expand= True)
    eightframe.pack_forget()
    

def act8_badoption():
    global finalscore
    finalscore += 1
    ninthframe.pack(fill="both", expand= True)
    eightframe.pack_forget()

    #Option buttons 
Option1_button8 = ctk.CTkButton(optionbutton_frame8, text="Scream!", width= 45, command= act8_badoption)
Option2_button8 = ctk.CTkButton(optionbutton_frame8, text="Immediately turn around and go the other direction.", width= 45, command= act8_betteroption)
Option3_button8 = ctk.CTkButton(optionbutton_frame8, text="Ignore and hope that they go away.", width= 45, command= act8_goodoption)
Option4_button8 = ctk.CTkButton(optionbutton_frame8, text="I don't find that joke funny. Please leave me alone.", width= 45, command= act8_bestoption)


#Layout for eightframe

    #Image visual layout
visual_label8.pack()
visual_frame8.pack(pady= '50')

#Problem window layout
problem_label8.pack(padx='10')
problem_frame8.pack(pady='10')

    #Options label layout
what_label8.pack(pady='10')
    #Option Button layout
Option1_button8.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button8.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button8.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button8.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame8.pack(fill= 'x', expand= True)

#ninthframe--------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame9 = ctk.CTkFrame(ninthframe)

    #Image visual
visual9 = ctk.CTkImage(dark_image=Image.open('img/S1_Act9.jpg'),
                      size=(450,300))
visual_label9 = ctk.CTkLabel(visual_frame9, image= visual9, text="")

#Problem window frame
problem_frame9 = ctk.CTkFrame(ninthframe)

    #Problem window
problem_label9 = ctk.CTkLabel(problem_frame9, anchor= "e", font= ('Arial',16),
                          text= "As you were walking in the library, you saw a person \nstruggling to reach a book."
                          )

#Options buttons frame
optionbutton_frame9 = ctk.CTkFrame(ninthframe)

    #Options buttons label
what_label9 = ctk.CTkLabel(optionbutton_frame9, text="What should you do?", font= ('Arial',20))

#option buttons function


def act9_bestoption():
    global finalscore
    finalscore += 5
    tenthframe.pack(fill="both", expand= True)
    ninthframe.pack_forget()

def act9_betteroption():
    global finalscore
    finalscore += 4
    tenthframe.pack(fill="both", expand= True)
    ninthframe.pack_forget()

def act9_goodoption():
    global finalscore
    finalscore += 3
    tenthframe.pack(fill="both", expand= True)
    ninthframe.pack_forget()
    

def act9_badoption():
    global finalscore
    finalscore += 1
    tenthframe.pack(fill="both", expand= True)
    ninthframe.pack_forget()

    #Option buttons 
Option1_button9 = ctk.CTkButton(optionbutton_frame9, text="Approach and offer them help.", width= 45, command= act9_bestoption)
Option2_button9 = ctk.CTkButton(optionbutton_frame9, text="Ignore", width= 45, command= act9_betteroption)
Option3_button9 = ctk.CTkButton(optionbutton_frame9, text="Approach without saying anything and help. Then leave.", width= 45, command= act9_goodoption)
Option4_button9 = ctk.CTkButton(optionbutton_frame9, text="Go over and just look at the situation.", width= 45, command= act9_badoption)


#Layout for fifthframe

    #Image visual layout
visual_label9.pack()
visual_frame9.pack(pady= '50')

#Problem window layout
problem_label9.pack(padx='10')
problem_frame9.pack(pady='10')

    #Options label layout
what_label9.pack(pady='10')
    #Option Button layout
Option1_button9.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button9.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button9.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button9.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame9.pack(fill= 'x', expand= True)

#tenthframe--------------------------------------------------------------------------------------------------------------------

#Image visual frame
visual_frame10 = ctk.CTkFrame(tenthframe)

    #Image visual
visual10 = ctk.CTkImage(dark_image=Image.open('img/S1_Act10.jpg'),
                      size=(450,300))
visual_label10 = ctk.CTkLabel(visual_frame10, image= visual10, text="")

#Problem window frame
problem_frame10 = ctk.CTkFrame(tenthframe)

    #Problem window
problem_label10 = ctk.CTkLabel(problem_frame10, anchor= "e", font= ('Arial',16),
                          text= "You asked if you could join a group, but they declined."
                          )

#Options buttons frame
optionbutton_frame10 = ctk.CTkFrame(tenthframe)

    #Options buttons label
what_label10 = ctk.CTkLabel(optionbutton_frame10, text="What should you say?", font= ('Arial',20))

#option buttons function



def act10_bestoption():
    global finalscore
    finalscore += 5
    global finalscore_param
    finalscore_param = int(finalscore)
    global user_id
    user_id_param = int(user_id)
    conversatile.execute("INSERT INTO scenario1_tbl (user_id, total_score) VALUES (%s, %s)", (user_id_param, finalscore_param))
    db.commit()
    if finalscore >= 35 :
        passedframe.pack(fill="both", expand= True)
        tenthframe.pack_forget()
    
    if finalscore <= 34 :
        failedframe.pack(fill="both", expand= True)
        tenthframe.pack_forget()

    #passed frame

    #Image visual frame
    visual_framep = ctk.CTkFrame(passedframe)

    #Image visual
    visualp = ctk.CTkImage(dark_image=Image.open('img/You Passed!.jpg'),
                      size=(450,300))
    visual_labelp = ctk.CTkLabel(visual_framep, image= visualp, text="")

    pass_label = ctk.CTkLabel(passedframe, font= ('Arial',16),                      
                        text="YOU PASSED! \n YOUR SCORE IS " + f"{finalscore}")

    #back to scenario menu
    b2s_button = ctk.CTkButton(passedframe, text="Back To Scenario Menu", width= 45, command= back_to_scenario_menu)

    #layout for passed frame
    visual_labelp.pack()
    visual_framep.pack(pady= '50')

    pass_label.pack(fill="both", expand= True)

    b2s_button.pack(padx='70',pady='35', fill='x',expand= True)

    #failed frame

    #Image visual frame
    visual_framef = ctk.CTkFrame(failedframe)

    #Image visual
    visualf = ctk.CTkImage(dark_image=Image.open('img/You Failed!.jpg'),
                      size=(450,300))
    visual_labelf = ctk.CTkLabel(visual_framef, image= visualf, text="")

    fail_label = ctk.CTkLabel(failedframe, font= ('Arial',16),                      
                        text="YOU FAILED! \n YOUR SCORE IS " + f"{finalscore}")

    #back to scenario menu
    b2s_button2 = ctk.CTkButton(failedframe, text="Back To Scenario Menu", width= 45, command= back_to_scenario_menu)

    #layout for fail frame
    visual_labelf.pack()
    visual_framef.pack(pady='50')

    fail_label.pack(fill="both", expand= True)

    b2s_button2.pack(padx='70',pady='35', fill='x',expand= True)

def act10_betteroption():
    global finalscore
    finalscore += 4
    global finalscore_param
    finalscore_param = int(finalscore)
    global user_id
    user_id_param = int(user_id)
    conversatile.execute("INSERT INTO scenario1_tbl (user_id, total_score) VALUES (%s, %s)", (user_id_param, finalscore_param))
    db.commit()
    if finalscore >= 35 :
        passedframe.pack(fill="both", expand= True)
        tenthframe.pack_forget()
    
    if finalscore <= 34 :
        failedframe.pack(fill="both", expand= True)
        tenthframe.pack_forget()

    #passed frame

    #Image visual frame
    visual_framep = ctk.CTkFrame(passedframe)

    #Image visual
    visualp = ctk.CTkImage(dark_image=Image.open('img/You Passed!.jpg'),
                      size=(450,300))
    visual_labelp = ctk.CTkLabel(visual_framep, image= visualp, text="")

    pass_label = ctk.CTkLabel(passedframe, font= ('Arial',16),                      
                        text="YOU PASSED! \n YOUR SCORE IS " + f"{finalscore}")

    #back to scenario menu
    b2s_button = ctk.CTkButton(passedframe, text="Back To Scenario Menu", width= 45, command= back_to_scenario_menu)

    #layout for passed frame
    visual_labelp.pack()
    visual_framep.pack(pady= '50')

    pass_label.pack(fill="both", expand= True)

    b2s_button.pack(padx='70',pady='35', fill='x',expand= True)

    #failed frame

    #Image visual frame
    visual_framef = ctk.CTkFrame(failedframe)

    #Image visual
    visualf = ctk.CTkImage(dark_image=Image.open('img/You Failed!.jpg'),
                      size=(450,300))
    visual_labelf = ctk.CTkLabel(visual_framef, image= visualf, text="")

    fail_label = ctk.CTkLabel(failedframe, font= ('Arial',16),                      
                        text="YOU FAILED! \n YOUR SCORE IS " + f"{finalscore}")

    #back to scenario menu
    b2s_button2 = ctk.CTkButton(failedframe, text="Back To Scenario Menu", width= 45, command= back_to_scenario_menu)

    #layout for fail frame
    visual_labelf.pack()
    visual_framef.pack(pady='50')

    fail_label.pack(fill="both", expand= True)

    b2s_button2.pack(padx='70',pady='35', fill='x',expand= True)

def act10_goodoption():
    global finalscore
    finalscore += 3
    global finalscore_param
    finalscore_param = int(finalscore) 
    global user_id
    user_id_param = int(user_id)  
    conversatile.execute("INSERT INTO scenario1_tbl (user_id, total_score) VALUES (%s, %s)", (user_id_param, finalscore_param))
    db.commit()
    if finalscore >= 35 :
        passedframe.pack(fill="both", expand= True)
        tenthframe.pack_forget()
    
    if finalscore <= 34 :
        failedframe.pack(fill="both", expand= True)
        tenthframe.pack_forget()

    #passed frame

    #Image visual frame
    visual_framep = ctk.CTkFrame(passedframe)

    #Image visual
    visualp = ctk.CTkImage(dark_image=Image.open('img/You Passed!.jpg'),
                      size=(450,300))
    visual_labelp = ctk.CTkLabel(visual_framep, image= visualp, text="")

    pass_label = ctk.CTkLabel(passedframe, font= ('Arial',16),                      
                        text="YOU PASSED! \n YOUR SCORE IS " + f"{finalscore}")

    #back to scenario menu
    b2s_button = ctk.CTkButton(passedframe, text="Back To Scenario Menu", width= 45, command= back_to_scenario_menu)

    #layout for passed frame
    visual_labelp.pack()
    visual_framep.pack(pady= '50')

    pass_label.pack(fill="both", expand= True)

    b2s_button.pack(padx='70',pady='35', fill='x',expand= True)

    #failed frame

    #Image visual frame
    visual_framef = ctk.CTkFrame(failedframe)

    #Image visual
    visualf = ctk.CTkImage(dark_image=Image.open('img/You Failed!.jpg'),
                      size=(450,300))
    visual_labelf = ctk.CTkLabel(visual_framef, image= visualf, text="")

    fail_label = ctk.CTkLabel(failedframe, font= ('Arial',16),                      
                        text="YOU FAILED! \n YOUR SCORE IS " + f"{finalscore}")

    #back to scenario menu
    b2s_button2 = ctk.CTkButton(failedframe, text="Back To Scenario Menu", width= 45, command= back_to_scenario_menu)

    #layout for fail frame
    visual_labelf.pack()
    visual_framef.pack(pady='50')

    fail_label.pack(fill="both", expand= True)

    b2s_button2.pack(padx='70',pady='35', fill='x',expand= True)

def act10_badoption():
    global finalscore
    finalscore += 1
    global finalscore_param
    finalscore_param = int(finalscore)
    global user_id
    user_id_param = int(user_id)    
    conversatile.execute("INSERT INTO scenario1_tbl (user_id, total_score) VALUES (%s, %s)", (user_id_param, finalscore_param))
    db.commit()
    if finalscore >= 35 :
        passedframe.pack(fill="both", expand= True)
        tenthframe.pack_forget()
    
    if finalscore <= 34 :
        failedframe.pack(fill="both", expand= True)
        tenthframe.pack_forget()

    #passed frame

    #Image visual frame
    visual_framep = ctk.CTkFrame(passedframe)

    #Image visual
    visualp = ctk.CTkImage(dark_image=Image.open('img/You Passed!.jpg'),
                      size=(450,300))
    visual_labelp = ctk.CTkLabel(visual_framep, image= visualp, text="")

    pass_label = ctk.CTkLabel(passedframe, font= ('Arial',16),                      
                        text="YOU PASSED! \n YOUR SCORE IS " + f"{finalscore}")

    #back to scenario menu
    b2s_button = ctk.CTkButton(passedframe, text="Back To Scenario Menu", width= 45, command= back_to_scenario_menu)

    #layout for passed frame
    visual_labelp.pack()
    visual_framep.pack(pady= '50')

    pass_label.pack(fill="both", expand= True)

    b2s_button.pack(padx='70',pady='35', fill='x',expand= True)

    #failed frame

    #Image visual frame
    visual_framef = ctk.CTkFrame(failedframe)

    #Image visual
    visualf = ctk.CTkImage(dark_image=Image.open('img/You Failed!.jpg'),
                      size=(450,300))
    visual_labelf = ctk.CTkLabel(visual_framef, image= visualf, text="")

    fail_label = ctk.CTkLabel(failedframe, font= ('Arial',16),                      
                        text="YOU FAILED! \n YOUR SCORE IS " + f"{finalscore}")

    #back to scenario menu
    b2s_button2 = ctk.CTkButton(failedframe, text="Back To Scenario Menu", width= 45, command= back_to_scenario_menu)

    #layout for fail frame
    visual_labelf.pack()
    visual_framef.pack(pady='50')

    fail_label.pack(fill="both", expand= True)

    b2s_button2.pack(padx='70',pady='35', fill='x',expand= True)

    #Option buttons 
Option1_button10 = ctk.CTkButton(optionbutton_frame10, text="Okay, sorry for disturbing you.", width= 45, command= act10_bestoption)
Option2_button10 = ctk.CTkButton(optionbutton_frame10, text="What do you mean no? I just wanted to share about…", width= 45, command= act10_goodoption)
Option3_button10 = ctk.CTkButton(optionbutton_frame10, text="You know what?” then proceed to make fun of them.", width= 45, command= act10_badoption)
Option4_button10 = ctk.CTkButton(optionbutton_frame10, text="Before I go, is there anything I did wrong?", width= 45, command= act10_betteroption)


#Layout for fifthframe

    #Image visual layout
visual_label10.pack()
visual_frame10.pack(pady= '50')

#Problem window layout
problem_label10.pack(padx='10')
problem_frame10.pack(pady='10')

    #Options label layout
what_label10.pack(pady='10')
    #Option Button layout
Option1_button10.pack(padx='70',pady='15', fill='x',expand= True)
Option2_button10.pack(padx='70',pady='15', fill='x',expand= True)
Option3_button10.pack(padx='70',pady='15', fill='x',expand= True)
Option4_button10.pack(padx='70',pady='15', fill='x',expand= True)
optionbutton_frame10.pack(fill= 'x', expand= True)

#--------------------------------------------------------------------------------

# Run
window.mainloop()
