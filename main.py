from create import *
from tkinter import *

window = Tk()

width = 700
height = 250
window.geometry(str(width) + "x" + str(height))

center_frame = Frame(window)
center_frame.pack(side="right")
# center_frame.grid(row=0, column=1)

menu_frame = Frame(window,
                   bg="#d45",
                   height=height,
                   width=int(width))
menu_frame.pack(side="left", fill="y")

add_objective_btn = Button(menu_frame,
                           text="Add Objective",
                           command=add_objective,
                           padx=10,
                           pady=10,
                           )
add_objective_btn.pack(pady=20, padx=20)

settings_btn = Button(menu_frame,
                           text="Settings",
                           command=open_settings,
                           padx=10,
                           pady=10,
                           width=10
                           )
settings_btn.pack(pady=20, padx=20)


# One way to check wheather user picked saves folder once
#create_saves_folder()
saves_path = "C:\\HbtsApp\\Saves"

window.mainloop()