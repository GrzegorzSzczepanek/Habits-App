import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def add_objective():
    global select_type_window
    select_type_window = Toplevel()
    select_type_window.resizable(False, False)

    yes_no_objective_btn = Button(select_type_window,
                                  text="YES/NO\nf.e. Did you wake up at 6AM",
                                  bg="#222",
                                  fg="#FFF",
                                  font=("Arial", 21),
                                  command=add_yes_no_objective
                                  ).grid(row=0)

    measurable_objective_btn = Button(select_type_window,
                                  text="Measurable Objective\nf.e. How many book pages have you read today",
                                  bg="#222",
                                  fg="#FFF",
                                  font=("Arial", 21),
                                  command=add_measurable_objective
                                  ).grid(row=1)


def add_yes_no_objective():
    _button_list = select_type_window.winfo_children()
    _button_list[0].destroy()
    _button_list[1].destroy()

    name = Label(select_type_window,
                  text="Name of task").grid(row=0)

    question = Label(select_type_window,
                      text="Question").grid(row=1)


    period_variable1 = StringVar()
    period_variable2 = StringVar()
    period_variable3 = StringVar()

    frequency = Label(select_type_window,
                      text="Frequency").grid(row=2)

    remainder = Label(select_type_window,
                      text="Remainder").grid(row=3)

    notes = Label(select_type_window,
                      text="Notes").grid(row=4)

    name_entry = Entry(select_type_window).grid(row=0, column=1)
    question_entry = Entry(select_type_window).grid(row=1, column=1)
    # frequency_frame = Frame(select_type_window).grid(row=2, column=1)
    Radiobutton(select_type_window, text="Everyday", value="everyday", variable=period_variable1).grid(row=2) 
    Radiobutton(select_type_window, text="Every other day", value="every other day", variable=period_variable2).grid(row=2) 
    Radiobutton(select_type_window, text="Weekly", value="weekly", variable=period_variable3).grid(row=2) 
    
    remainder_entry = Entry(select_type_window).grid(row=3, column=1)
    
    notes_entry = Entry(select_type_window).grid(row=4, column=1)

    Button(select_type_window, text="Back",command=get_back).grid(row=5, column=0)
    Button(select_type_window, text="Add", command=create_obejctive("YN")).grid(row=5, column=1)


def add_measurable_objective():
    _button_list = select_type_window.winfo_children()
    _button_list[0].destroy()
    _button_list[1].destroy()


def create_obejctive(objective_type):
    pass


def get_back():
    pass

def open_settings():
    dark_theme = True

    settings_window = Toplevel()
    settings_window.title("Settings")
    settings_window.geometry("250x500")
    settings_label = Label(settings_window,
                           text="Test Label").pack()

    night_mode_btn = Button(settings_window,
                            text="Night mode",
                            command=change_theme(dark_theme)).pack()

    language_btn = Button(settings_window,
                          text="Change language").pack()


def change_theme(current_theme):
    pass


def create_saves_folder():
    if os.path.isdir("C:\\HbtsApp"):
        return
    else:
        check_path = os.path.join("C:\\", "HbtsApp")
        os.makedirs(check_path)
        source_directory = filedialog.askdirectory(title="Selected Directory will be used to save your data and settings")
        path = os.path.join(source_directory, "Saves")
        os.makedirs(path)
    return path
