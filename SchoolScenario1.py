import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import ImageTk, Image


# Window 
window = ttk.Window(themename= 'vapor')
window.title('Conversatile')
window.geometry('750x1334')

#Image visual frame
visual_frame = ttk.Frame(window)

    #Image visual
visual = Image.open('img/First day.jpg')
visual_resize = visual.resize((450,300))
visual_tk = ImageTk.PhotoImage(visual_resize)
visual_label = ttk.Label(visual_frame, image= visual_tk)

#Problem window frame
problem_frame = ttk.Frame(window)

    #Problem window
problem_label = ttk.Label(problem_frame, anchor= "e", font= (30),
                          text= "It's the first day of school and you want to make friends, but you must act quick. \nPeople tend to establish their friendship circles in 3 days making it tougher \nto join them the longer you hesitate." 
                          "\n\nYou muster up your courage, but you can't just \napproach someone without having anything to say."
                          )

#Options buttons frame
optionbutton_frame = ttk.Frame(window)

    #Options buttons label
what_label = ttk.Label(optionbutton_frame, text="What should you do?", font=(20))

    #Option buttons 
Option1_button = ttk.Button(optionbutton_frame, text="Approach them but don't say anything until they do.", width= 45)
Option2_button = ttk.Button(optionbutton_frame, text="Join in a random conversation and take over.", width= 45)
Option3_button = ttk.Button(optionbutton_frame, text="Observe, Approach, and Introduce yourself.", width= 45)
Option4_button = ttk.Button(optionbutton_frame, text="Gamble your odds and let them come to you first.", width= 45)


#Layout

    #Image visual layout
visual_label.pack()
visual_frame.pack(pady= '50')

    #Problem window layout
problem_label.pack(padx='10')
problem_frame.pack(pady='10')

    #Options label layout
what_label.pack(pady='10')
    #Option Button layout
Option1_button.pack(pady='15')
Option2_button.pack(pady='15')
Option3_button.pack(pady='15')
Option4_button.pack(pady='15')
optionbutton_frame.pack(expand='true')



#Run
window.mainloop()