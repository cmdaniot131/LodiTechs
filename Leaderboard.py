import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
import mysql.connector

#Database
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "02blz002",
    database="conversatile_db"
)

conversatile = db.cursor()


#window style
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("theme/conversatile.json")

# Window Changes
window=ctk.CTk() #creating custom tkinter window
window.geometry("470x750'")
window.title("Conversatile")

#Leaderboard Frame 
lbd_frame = ctk.CTkFrame(window)

#Leaderboard label
lbd_label = ctk.CTkLabel(lbd_frame, text=" LEADERBOARD", font=("", 30))

#Leaderboard access database

conversatile.execute("SELECT total_score FROM scenario1_tbl ORDER BY total_score DESC")

top10 = []

for x in conversatile:
    score = x[0]
    if score is not None:  # Check if the score is not None
        score = int(score)
        top10.append(score)

#Leaderboard variables
top1_entry = str(top10[0]) if top10 else ""
top2_entry = str(top10[1]) if len(top10) > 1 else ""
top3_entry = str(top10[2]) if len(top10) > 2 else ""
top4_entry = str(top10[3]) if len(top10) > 3 else ""
top5_entry = str(top10[4]) if len(top10) > 4 else ""
top6_entry = str(top10[5]) if len(top10) > 5 else ""
top7_entry = str(top10[6]) if len(top10) > 6 else ""
top8_entry = str(top10[7]) if len(top10) > 7 else ""
top9_entry = str(top10[8]) if len(top10) > 8 else ""
top10_entry = str(top10[9]) if len(top10) > 9 else ""
#Leaderboard entry

lbdentry1_label = ctk.CTkLabel(lbd_frame, text="1." + "Joaquin Rizal" + "     |      " + f"{top1_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry2_label = ctk.CTkLabel(lbd_frame, text="2." + "Jwaine Bravo" + "     |      " + f"{top2_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry3_label = ctk.CTkLabel(lbd_frame, text="3." + " " + "     |      " + f"{top3_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry4_label = ctk.CTkLabel(lbd_frame, text="4." + " " + "     |      " + f"{top4_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry5_label = ctk.CTkLabel(lbd_frame, text="5." + " " + "     |      " + f"{top5_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry6_label = ctk.CTkLabel(lbd_frame, text="6." + " " + "     |      " + f"{top6_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry7_label = ctk.CTkLabel(lbd_frame, text="7." + " " + "     |      " + f"{top7_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry8_label = ctk.CTkLabel(lbd_frame, text="8." + " " + "     |      " + f"{top8_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry9_label = ctk.CTkLabel(lbd_frame, text="9." + " " + "     |      " + f"{top9_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))
lbdentry10_label = ctk.CTkLabel(lbd_frame, text="10." + " " + "     |      " + f"{top10_entry}", fg_color= "#FFFFFF", corner_radius= 15, font=("", 20))        

#bact to main menu function
def b2mm():
    window.destroy
    import conversatile

#back to main menu
b2mm_button = ctk.CTkButton(lbd_frame, text="Back", font=("", 20), command= b2mm)

#Leaderboard layout
lbd_label.pack(pady='30')

lbdentry1_label.pack(fill='x', padx='100', pady='15')
lbdentry2_label.pack(fill='x', padx='100', pady='15')
lbdentry3_label.pack(fill='x', padx='100', pady='15')
lbdentry4_label.pack(fill='x', padx='100', pady='15')
lbdentry5_label.pack(fill='x', padx='100', pady='15')
lbdentry6_label.pack(fill='x', padx='100', pady='15')
lbdentry7_label.pack(fill='x', padx='100', pady='15')
lbdentry8_label.pack(fill='x', padx='100', pady='15')
lbdentry9_label.pack(fill='x', padx='100', pady='15')
lbdentry10_label.pack(fill='x', padx='100', pady='15')

b2mm_button.pack(fill='x', padx='100', pady='25')

lbd_frame.pack(fill="both", expand= True, pady= '20')


# Run
window.mainloop()