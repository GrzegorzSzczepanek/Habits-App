from create import generate_main_window_content
import tkinter as tk

window = tk.Tk()

# center_frame.grid(row=0, column=1)
# create_saves_folder()
# saves_path = "C:\\HbtsApp\\Saves"

if __name__ == "__main__":
    width = 700
    height = 500
    window.geometry(str(width) + "x" + str(height))
    generate_main_window_content(window, height, width)

window.mainloop()
