from create import generate_main_window_content
import tkinter as tk

window = tk.Tk()

if __name__ == "__main__":
    width = 900
    height = 500
    window.geometry(str(width) + "x" + str(height))
    generate_main_window_content(window, height, width)

window.mainloop()
