import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import os as os


# Add validation to check if the file already exists
def create_save_file(data):
    filename = data['name'][0] + '.csv'
    progress_filename = data['name'][0] + '_progress' + '.csv'

    data.to_csv(filename, index=False)
    obj_path = os.path.join(filename)
    data.to_csv(filename, index=False)

    df_basic_info = pd.read_csv(filename)
    df_progress_info = pd.DataFrame(
        columns=['days','streak','missed', 'percentage'],
    )
    # this datafreame will be used in creating plot showing user's regularity
    df_progress_info['days'] = [1]
    df_progress_info['streak'] = [1]
    df_progress_info['missed'] = [0]
    df_progress_info['percentage'] = 100 - (df_progress_info['missed'] / df_progress_info['days']) * 100

    progress_track_file = df_progress_info.to_csv(progress_filename, index=False)


def open_widndow_with_plot(progress_filename, window):
    new_window = tk.Toplevel(window)
    new_window.title("New Window")
    new_window.geometry("800x500")

    # create grid for a window
    for i in range(9):
        new_window.columnconfigure(i, weight=1, minsize=80)
        new_window.rowconfigure(i, weight=1, minsize=50)

    # create plot
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=6, columnspan=4, rowspan=4)

    df = pd.read_csv(progress_filename + '_progress.csv')
    df['percentage'] = 100 - (df['missed'] / df['days']) * 100
    ax.plot(df['percentage'][0:])
    ax.set_ylim(0, 105)
    ax.set_xlim(0, None)
    ax.set_title(progress_filename)
    canvas.draw()

    streak = int(df.iloc[-1]['streak'])
    streak_label = tk.Label(new_window, text=f"You are on {(streak)} day streak", font=('Tahoma', 20),
                            fg='#000').grid(row=1, column=2, columnspan=4)

    input_frame = tk.Frame(new_window).grid(row=3, rowspan=6, column=1, columnspan=3)

    return


def delete_save_file():
    pass


# this function creates folder for saves only if user has not done it before
# def create_saves_folder():
#     if os.path.isdir("C:\\HbtsApp"):
#         return
#     else:
#         check_path = os.path.join("C:\\", "HbtsApp")
#         os.makedirs(check_path)
#         source_directory = filedialog.askdirectory(title="Selected Directory will be used to save your data and settings")
#         path = os.path.join(source_directory, "Saves")
#         os.makedirs(path)
#     return path


# this function sets the saves folder arbitraily  
# def create_saves_folder():
#     if os.path.isdir("C:\\HbtsApp"):
#         return
#     else:
#         check_path = os.path.join("C:\\", "HbtsApp")
#         os.makedirs(check_path)
#         path = os.path.join(check_path, "Saves")
#         os.makedirs(path)
#     return path
