from create import generate_main_window_content
from tkinter import *

window = Tk()

width = 700
height = 500
window.geometry(str(width) + "x" + str(height))
# center_frame.grid(row=0, column=1)
# create_saves_folder()
# saves_path = "C:\\HbtsApp\\Saves"

if __name__ == "__main__":
    generate_main_window_content(window, height, width)

window.mainloop()
