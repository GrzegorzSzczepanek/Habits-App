import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import os as os
from visual_effects import *


def data_to_csv(data, file_path, progress_file_name):
    data.to_csv(file_path, index=False)
    obj_path = os.path.join(file_path)
    data.to_csv(file_path, index=False)

    df_basic_info = pd.read_csv(file_path)
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

    progress_track_file = df_progress_info.to_csv(progress_file_name, index=False)


def create_save_file(data, save_dir):
    filename = data["name"][0] + ".csv"
    file_path = os.path.join(save_dir, filename)
    progress_filename = data["name"][0] + "_progress" + ".csv"
    progress_file_path = os.path.join(save_dir, progress_filename)


    if os.path.isfile(file_path) or os.path.isfile(progress_filename):
        tk.messagebox.showerror(
            "Task with such name already exists",
            "Create task with unique name or delete previous one",
        )
        return

    data_to_csv(data, file_path, progress_file_path)


def open_window(progress_filename, window, remake_objectives_button_function):
    new_window = tk.Toplevel(window)
    new_window.title("New Window")
    new_window.geometry("1200x700")

    global validate_cmd
    validate_cmd = window.register(validate_entry_text)

    generate_content(new_window, progress_filename, remake_objectives_button_function)


def generate_plot(new_window, progress_filename):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=6, columnspan=3, rowspan=3)

    df = pd.read_csv(progress_filename + "_progress.csv")

    if df["objective_type"].iloc[0] == "y/n":
        ax.plot(df["percentage"][0:], label="Percent of days when you achieved your goal")
        ax.set_ylim(0, 105)
        ax.set_xlim(0, None)
        ax.set_title(progress_filename)
        ax.legend(loc="upper left")
        ax.set_title(progress_filename)
    else:
        ax.plot(df["done"][0:], label="Acheved things per time unit")
        ax.set_ylim(0, None)
        ax.set_xlim(0, None)
        ax.set_title(progress_filename)
        ax.legend(loc="upper left")
        ax.set_title(progress_filename)

    canvas.draw()

    return df


def generate_content(new_window, progress_filename, remake_objectives_button_function):
    progress_df = generate_plot(new_window, progress_filename)
    df = pd.read_csv(progress_filename + ".csv")
    new_window.title(df["name"].iloc[0])
    streak = int(progress_df.iloc[-1]["streak"])
    streak_label = tk.Label(
        new_window,
        text=f"You are on {(streak)} day streak",
        font=("Tahoma", 20),
        fg="#000",
    ).grid(row=1, column=1, columnspan=4, padx=20, pady=20)

    notes = df["notes"].iloc[0]
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
        command=lambda x=progress_filename, y=new_window, z=remake_objectives_button_function: delete_save_file(x, y, z)
    ).grid(row=1, column=7)

    input_frame = tk.Frame(new_window)
    input_frame.grid(row=3, rowspan=6, column=1, columnspan=3)

    filename = progress_filename.replace("_progress", "") + ".csv"
    question = pd.read_csv(progress_filename + ".csv")["question"].iloc[0]

    if pd.read_csv(progress_filename + ".csv")["objective type"].iloc[0] == "y/n":
        create_input(new_window, input_frame, question, "y/n", progress_filename)
    else:
        create_input(new_window, input_frame, question, "m", progress_filename)
        # create_measurable_input(new_window, input_frame, question)


def validate_entry_text(text):
    if text.strip().isdigit():
        return True
    else:
        return False


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
        submit_button.config(command=lambda x=filename, y=yes_no_var, z=new_window: use_input(z, x, y.get()))
        submit_button.grid(row=3, column=0, columnspan=2)
    else:
        tk.Label(
            input_frame, text="Type how many things of your objective you've done"
        ).grid(row=3, column=0, columnspan=2)

        spinbox = tk.Spinbox(input_frame, from_=0, to=(2**30), increment=1)
        spinbox.grid(row=4, column=0, columnspan=2)
        submit_button.config(command=lambda x=filename, y=yes_no_var, z=spinbox,
                             a=new_window: use_input(a, x, y.get(), z.get()))
        submit_button.grid(row=5, column=0, columnspan=2)


def delete_save_file(filename, window, remake_objectives_button_function):
    os.remove(filename + ".csv")
    os.remove(filename + "_progress.csv")
    from tkinter import messagebox
    messagebox.showinfo("Success", f"{filename} has been deleted successfully.")
    window.destroy()
    remake_objectives_button_function[0](remake_objectives_button_function[1], remake_objectives_button_function[2])


def calculate_current_streak(streak_column):
    current_streak = 0
    max_streak = 0

    for value in streak_column:
        if value == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak


def update_missed(filename, radio_input):
    df = pd.read_csv(filename)
    if radio_input == "No":
        missed_count = df['missed'].sum() + 1
    else:
        missed_count = df['missed'].sum()

    total_days = len(df)
    print(total_days + 10)
    percentage = (total_days - missed_count) / total_days * 100
    return percentage


def use_input(new_window, filename, radio_input, spinbox_input=None):
    filename = filename + "_progress.csv"
    progress_df = pd.read_csv(filename)

    current_streak = calculate_current_streak(progress_df["streak"])
    # last_day = progress_df['days'].iloc[-1]
    new_day = 1
    missed = 1 if radio_input == "No" else 0
    percentage = update_missed(filename, radio_input)
    if spinbox_input is not None:
        done = spinbox_input
        new_row = pd.DataFrame({"days": [new_day], "streak": current_streak,
                               "missed": missed, "percentage": percentage, "done": done})

    else:
        new_row = pd.DataFrame({"days": [new_day], "streak": current_streak,
                               "missed": missed, "percentage": percentage})

    progress_df = pd.concat([progress_df, new_row], ignore_index=True)
    progress_df.to_csv(filename, index=False)

    new_window.destroy()
