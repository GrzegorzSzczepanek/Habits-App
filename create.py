import glob
import pandas as pd
import platform
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import filedialog
from visual_effects import *
from visualise_data import create_save_file, open_window


def check_save_path():
    saves_path = ''
    if platform.system() == "Linux":
        home_dir = os.path.expanduser('~')
        saves_path = os.path.join(home_dir, '.local', 'share', 'habits-app', 'saves')
        if not os.path.exists(saves_path):
            os.makedirs(saves_path)
    elif platform.system() == "Windows":
        saves_path = os.path.join(os.path.expandvars('%APPDATA%'), 'habits-app', 'saves')
        if not os.path.isdir():
            os.makedirs(saves_path, exist_ok=True)

    # saves_path = "./"
    return saves_path


def generate_main_window_content(window, height=700, width=250):
    window.title("Habits app")
    global center_frame
    center_frame = tk.Frame(window)
    center_frame.pack(side="right", fill="both", expand=True)
    center_frame.grid_columnconfigure(0, weight=1)

    menu_frame = tk.Frame(window, bg="#d45", height=int(height), width=int(width))
    menu_frame.grid_columnconfigure(0, weight=1)
    menu_frame.pack(side="left", fill="y")

    font = ("Tahoma", 20)

    add_objective_btn = tk.Button(
        menu_frame, text="Add Objective", command=add_objective, font=font, pady=10
    )
    add_objective_btn.grid(row=0, sticky="ew")

    settings_btn = tk.Button(
        menu_frame, text="Settings", command=open_settings, pady=10, width=10, font=font
    )
    settings_btn.grid(row=1, sticky="ew")
    create_buttons_from_saves(center_frame, font)


def create_buttons_from_saves(center_frame, font):
    for button in center_frame.winfo_children():
        button.destroy()

    directory_path = os.path.expanduser("~/.local/share/habits-app/saves")
    # Get a list of CSV file paths
    csv_file_saves = glob.glob(os.path.join(directory_path, "*.csv"))

    for index, csv_file in enumerate(csv_file_saves):
        if "progress" not in csv_file:
            data = pd.read_csv(csv_file)
            current_filename = data["name"][0]
            btn = tk.Button(
                center_frame,
                text=data["name"][0],
                bg="#222",
                fg="#EEE",
                pady=30,
                font=font,
                command=lambda x=csv_file: open_window(
                    x, center_frame.winfo_toplevel(), [create_buttons_from_saves, center_frame, font]
                ),
            ).grid(row=index, columnspan=2, sticky="we")


def create_starting_btns():
    yes_no_objective_btn = tk.Button(
        select_type_frame,
        text="YES/NO\nf.e. Did you wake up at 6AM",
        bg="#222",
        fg="#FFF",
        command=add_yes_no_objective,
    ).grid(row=0, sticky="ew")

    measurable_objective_btn = tk.Button(
        select_type_frame,
        text="Measurable Objective\nf.e. How many book pages have you read today",
        bg="#222",
        fg="#FFF",
        command=add_measurable_objective,
    ).grid(row=1, sticky="ew")


def add_objective():
    select_type_window = tk.Toplevel()
    select_type_window.title("Add objective")
    global select_type_frame
    select_type_frame = tk.Frame(select_type_window)
    select_type_frame.pack(fill="both", expand=True)
    create_starting_btns()


def add_yes_no_objective():
    global entries
    _button_list = select_type_frame.winfo_children()
    _button_list[0].destroy()
    _button_list[1].destroy()

    labels = [
        tk.Label(select_type_frame, text="Name of task"),
        tk.Label(select_type_frame, text="Question"),
        tk.Label(select_type_frame, text="Remainder"),
        tk.Label(select_type_frame, text="Notes"),
        tk.Label(select_type_frame, text="Frequency per week"),
    ]
    for i in range(0, len(labels)):
        labels[i].grid(row=i, column=0)

    options = ["everyday", "every other day", "weekly"]
    global clicked
    clicked = tk.StringVar()

    clicked.set("everyday")

    entries = [
        EntryWithPlaceholder(select_type_frame, "f.e Wake up at 7AM"),
        EntryWithPlaceholder(select_type_frame, "F.e. did you wake up early?"),
        EntryWithPlaceholder(select_type_frame, "18:00/None"),
        EntryWithPlaceholder(select_type_frame, "Any useful info (max 100 characters)"),
        tk.OptionMenu(select_type_frame, clicked, *options),
    ]
    for i in range(0, len(entries)):
        entries[i].grid(row=i, column=1)

    tk.Button(select_type_frame, text="Back", command=get_back).grid(
        row=len(entries), column=0
    )
    tk.Button(select_type_frame, text="Add", command=use_input).grid(
        row=len(entries), column=1
    )


def add_measurable_objective():
    _button_list = select_type_frame.winfo_children()
    _button_list[0].destroy()
    _button_list[1].destroy()
    global entries

    labels = [
        tk.Label(select_type_frame, text="Name of task"),
        tk.Label(select_type_frame, text="Question"),
        tk.Label(select_type_frame, text="Remainder"),
        tk.Label(select_type_frame, text="Notes"),
        tk.Label(select_type_frame, text="Unit f.e kilometers"),
        tk.Label(select_type_frame, text="Frequency per week"),
    ]
    for i in range(0, len(labels)):
        labels[i].grid(row=i, column=0)

    options = ["everyday", "every other day", "weekly"]
    global clicked
    clicked = tk.StringVar()
    clicked.set("everyday")
    entries = [
        EntryWithPlaceholder(select_type_frame, "f.e Read pages of the book"),
        EntryWithPlaceholder(select_type_frame, "How many kilometers did you run?"),
        EntryWithPlaceholder(select_type_frame, "21:37/None"),
        EntryWithPlaceholder(select_type_frame, "Any useful info (max 100 characters)"),
        EntryWithPlaceholder(select_type_frame, "f.e Kilometers"),
        tk.OptionMenu(select_type_frame, clicked, *options),
    ]
    for i in range(0, len(entries)):
        entries[i].grid(row=i, column=1)

    tk.Button(select_type_frame, text="Back", command=get_back).grid(
        row=len(entries), column=0
    )
    tk.Button(select_type_frame, text="Add", command=use_input).grid(
        row=len(entries), column=1
    )


def use_input():
    valid_input = validate_input()
    if len(valid_input) == 6:
        obj_df = pd.DataFrame(
            [valid_input],
            columns=[
                "name",
                "question",
                "notes",
                "frequency",
                "remainder",
                "objective type",
            ],
        )
    else:
        obj_df = pd.DataFrame(
            [valid_input],
            columns=[
                "name",
                "question",
                "notes",
                "unit",
                "frequency",
                "remainder",
                "objective type",
            ],
        )

    objective_save_path = check_save_path()
    create_save_file(obj_df, objective_save_path)
    create_buttons_from_saves(center_frame, font=("Tahoma", 20))


def validate_input(*args):
    # this string is used in validation as a regex
    n = "0123456789"

    basic_values = [
        "f.e Wake up at 7AM",
        "F.e. did you wake up early",
        "18:00/None",
        "Any additional information",
        "f.e Kilometers",
    ]
    correct_values = []
    i = 0
    for entry in entries:
        if (i == 0 or i == 1) and len(entry.get().strip()) == 0:
            messagebox.showerror(
                "Incorrect values", "Objective name and question can't be empty"
            )
            break

        if isinstance(entry, tk.OptionMenu):
            correct_values.append(clicked.get())
        elif isinstance(entry, tk.Entry) and entry.get() in basic_values:
            messagebox.showerror(
                "Incorrect values", "You need to create your own objectives"
            )
            break

        # validation for time input
        elif i == 2:
            if entry.get().lower() == "none":
                correct_values.append(entry.get().lower())
            elif len(entry.get()) != 5:
                messagebox.showerror(
                    "Incorrect values",
                    "Time shold be in XX:XX format or set as None if you don't want a remainder",
                )
                break
            elif entry.get()[2] != ":":
                messagebox.showerror(
                    "Incorrect values",
                    "Time shold be in XX:XX format or set as None if you don't want a remainder",
                )
                break
            elif not (
                entry.get()[0] in n
                and entry.get()[1] in n
                and entry.get()[3] in n
                and entry.get()[4] in n
            ):
                messagebox.showerror(
                    "Incorrect values",
                    "Time shold be in XX:XX format or set as None if you don't want a remainder",
                )
                break
            elif not (
                0 < int(entry.get().split(":")[0]) < 24
                and 0 <= int(entry.get().split(":")[0]) < 60
            ):
                messagebox.showerror(
                    "Incorrect values",
                    "Time shold be in XX:XX format or set as None if you don't want a remainder",
                )
                break
            else:
                entries.append(entry.get())

        # Not working lenght of Notes validation
        # elif i == 3 and len(entry.get()) > 100:
        #     messagebox.showerror(
        #             "Incorrect values",
        #             "Notes should be shorter than 100 characters, including spaces and special characters",
        #         )
        elif isinstance(entry, tk.Entry):
            correct_values.append(entry.get())
        else:
            correct_values.append(entry)
        i += 1

    # make sure user will receive a question later
    if correct_values[1][-1] != "?":
        correct_values[1] = correct_values[1] + "?"

    if len(correct_values) == 5:
        correct_values.append("y/n")
    else:
        correct_values.append("measurable")

    select_type_frame.winfo_toplevel().destroy()

    return correct_values


def get_back():
    _button_list = select_type_frame.winfo_children()
    for i in _button_list:
        i.destroy()
    create_starting_btns()


def open_settings():
    settings_window = tk.Toplevel()
    settings_window.title("Settings")
    settings_window.grid_columnconfigure(0, weight=1)
    settings_window.geometry("250x500")
    settings_label = tk.Label(settings_window, text="Test Label")

    night_mode_btn = tk.Button(
        settings_window, text="Night mode", command=change_theme
    ).grid(row=1, sticky="ew")

    language_btn = tk.Button(settings_window, text="Change language").grid(
        row=2, sticky="ew"
    )


# def get_location():
#     filetypes = (('All files', '*.*'),)
#     location = filedialog.askopenfilename(filetypes=filetypes, initialdir="/")
#     return location


# def create_saves_folder():
#     location = get_location()
#     filename = "habts_app_save.csv"
#     filepath = location + "/" + filename
#
    # this function creates folder for saves only if user has not done it before
    # create_saves_folder()
    # create_saves_folder()
