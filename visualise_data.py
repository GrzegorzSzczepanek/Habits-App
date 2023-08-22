import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import os as os
from visual_effects import *


def create_save_file(data):
    # print(data)
    filename = data["name"][0] + ".csv"
    progress_filename = data["name"][0] + "_progress" + ".csv"

    if os.path.isfile(filename) or os.path.isfile(progress_filename):
        tk.messagebox.showerror(
            "Task with such name already exists",
            "Create task with unique name or delete previous one",
        )
        return

    data.to_csv(filename, index=False)
    obj_path = os.path.join(filename)
    data.to_csv(filename, index=False)

    df_basic_info = pd.read_csv(filename)
    df_progress_info = pd.DataFrame(
        columns=[
            "days",
            "streak",
            "missed",
            "percentage",
            "objective_type",
            "done",
            "average",
        ],
    )
    # this datafreame will be used in creating plot showing user's regularity
    df_progress_info["days"] = [1]
    df_progress_info["streak"] = [0]
    df_progress_info["missed"] = [0]
    df_progress_info["objective_type"] = "m" if data.shape[1] == 7 else "y/n"
    df_progress_info["percentage"] = (
        100 - (df_progress_info["missed"] / df_progress_info["days"]) * 100
    )
    if data.shape[1] == 7:
        # these columns are explicit to measurable objective
        df_progress_info["done"] = [0]
        df_progress_info["average"] = [
            df_progress_info["done"].sum() / sum(df_progress_info["days"])
        ]

    progress_track_file = df_progress_info.to_csv(progress_filename, index=False)


def open_window(progress_filename, window, remake_objectives_button_function):
    new_window = tk.Toplevel(window)
    new_window.title("New Window")
    new_window.geometry("1000x700")

    global validate_cmd
    validate_cmd = window.register(validate_entry_text)

    generate_content(new_window, progress_filename, remake_objectives_button_function)


def generate_plot(new_window, progress_filename):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=6, columnspan=3, rowspan=3)

    df = pd.read_csv(progress_filename + "_progress.csv")
    df["percentage"] = 100 - (df["missed"] / df["days"]) * 100
    ax.plot(df["percentage"][0:])
    ax.set_ylim(0, 105)
    ax.set_xlim(0, None)
    ax.set_title(progress_filename)
    canvas.draw()

    return df


def generate_content(new_window, progress_filename, remake_objectives_button_function):

    df = generate_plot(new_window, progress_filename)

    streak = int(df.iloc[-1]["streak"])
    streak_label = tk.Label(
        new_window,
        text=f"You are on {(streak)} day streak",
        font=("Tahoma", 20),
        fg="#000",
    ).grid(row=1, column=1, columnspan=4, padx=20, pady=20)

    notes = pd.read_csv(progress_filename + ".csv")["notes"].iloc[0]
    notes_label = tk.Label(
        new_window,
        text=f"My notes:\n{notes}",
        font=("Tahoma", 15),
        relief="sunken"
    ).grid(row=7, column=0, padx=20, pady=20)
    delete_button = tk.Button(
        new_window,
        text="Delete this Objective",
        font=("Tahoma", 15),
        fg="#800",
        command=lambda x = progress_filename, y = new_window, z = remake_objectives_button_function: delete_save_file(x, y, z)
    ).grid(row=1, column=7)

    input_frame = tk.Frame(new_window)
    input_frame.grid(row=3, rowspan=6, column=1, columnspan=3)

    filename = progress_filename.replace("_progress", "") + ".csv"
    question = pd.read_csv(progress_filename + ".csv")["question"].iloc[0]

    if pd.read_csv(progress_filename + ".csv")["objective type"].iloc[0] == "y/n":
        create_input(new_window, input_frame, question, "y/n", filename)
    else:
        create_input(new_window, input_frame, question, "m")
        # create_measurable_input(new_window, input_frame, question)


def validate_entry_text():
    pass


def create_input(new_window, input_frame, question, objective_type, filename):

    check_label = tk.Label(input_frame, text=question, font=("Tahoma", 15))
    check_label.grid(row=0, column=0, columnspan=2)

    yes_no_var = tk.StringVar()
    yes_no_var.set("No")

    yes_button = tk.Radiobutton(
        input_frame, text="Yes", variable=yes_no_var, value="Yes", font=("Tahoma", 10)
    )
    no_button = tk.Radiobutton(
        input_frame, text="No", variable=yes_no_var, value="No", font=("Tahoma", 10)
    )

    yes_button.grid(row=1, column=0)
    no_button.grid(row=1, column=1)

    submit_button = tk.Button(
        input_frame, text="submit answers", font=("Tahoma", 15)
    )
    # only one difference between measurable is that it has one spinbox more so I need to prevent submit button overlapping spinbox
    if objective_type == "y/n":
        submit_button.config(command=lambda x = filename, y = yes_no_var.get: use_input(x))
        submit_button.grid(row=3, column=0, columnspan=2)
    else:
        tk.Label(
            input_frame, text="Type how many things of your objective you've done"
        ).grid(row=3, column=0, columnspan=2)

        tk.Spinbox(input_frame, from_=0, to=2^31-1, increment=1).grid(row=4, column=0, columnspan=2)
        submit_button.config(command=lambda x = filename, y = yes_no_var.get, z = "spinbox_value.get": use_input(x, y, z))
        submit_button.grid(row=5, column=0, columnspan=2)


def delete_save_file(filename, window, remake_objectives_button_function):
    os.remove(filename + ".csv")
    os.remove(filename + "_progress.csv")
    from tkinter import messagebox
    messagebox.showinfo("Success", f"{filename} has been deleted successfully.")
    window.destroy()
    remake_objectives_button_function[0](remake_objectives_button_function[1],remake_objectives_button_function[2])


def calculate_current_streak(streak_column):
    current_streak = 0
    max_streak = 0

    for streak in streak_column:
        if streak != 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak


def use_input(filename, radio_input, spinbox_input=None):
    df = pd.read_csv(filename)
    if spinbox_input == None:
        #df['days']
        pass
    else:
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
