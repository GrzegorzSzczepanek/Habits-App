import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
# def on_frame_configure(canvas):
#     canvas.configure(scrollregion=canvas.bbox("all"))
#
root = tk.Tk()
# root.title("Scrollable Frame")
#
# # Create a Canvas
# canvas = tk.Canvas(root)
# canvas.pack(side="left", fill="both", expand=True)
#
# # Create a Scrollbar
# scrollbar = ttk.Scrollbar(root, command=canvas.yview)
# scrollbar.pack(side="right", fill="y")
#
# canvas.configure(yscrollcommand=scrollbar.set)
#
# # Create a Frame inside the Canvas
# frame = tk.Frame(canvas)
# canvas.create_window((0, 0), window=frame, anchor="nw")
#
# # Configure the scrolling behavior
# frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))
#
# # Add widgets (buttons in this example) to the Frame
# for i in range(20):
#     button = tk.Button(frame, text=f"Button {i}")
#     button.pack(pady=5, padx=10)
#


def get_location():
    filetypes = (('All files', '*.*'),)
    location = filedialog.askopenfilename(filetypes=filetypes, initialdir="/")
    return location


def create_saves_folder():
    location = get_location()
    filename = "habts_app_save.csv"
    filepath = location + "/" + filename


root.mainloop()
