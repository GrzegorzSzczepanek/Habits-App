import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from visual_effects import *
# functions for entries placeholders

def create_starting_btns():
    global measurable_objective_btn, yes_no_objective_btn
    yes_no_objective_btn = Button(select_type_window,
                                  text="YES/NO\nf.e. Did you wake up at 6AM",
                                  bg="#222",
                                  fg="#FFF",
                                  command=add_yes_no_objective
                                  ).grid(row=0)

    measurable_objective_btn = Button(select_type_window,
                                  text="Measurable Objective\nf.e. How many book pages have you read today",
                                  bg="#222",
                                  fg="#FFF",
                                  command=add_measurable_objective
                                  ).grid(row=1)

def add_objective():
    global select_type_window
    select_type_window = Toplevel()
    select_type_window.resizable(False, False)
    create_starting_btns()
# correct frequency to radio or list type input with "everday, every second day and weekly" options

def add_yes_no_objective():
    _button_list = select_type_window.winfo_children()
    _button_list[0].destroy()
    _button_list[1].destroy()

    name = Label(select_type_window,
                  text="Name of task").grid(row=0)

    question = Label(select_type_window,
                      text="Question").grid(row=1)


    frequency = Label(select_type_window,
                      text="Frequency per week").grid(row=2)

    remainder = Label(select_type_window,
                      text="Remainder").grid(row=3)

    notes = Label(select_type_window,
                      text="Notes").grid(row=4)

    name_entry = EntryWithPlaceholder(select_type_window, "f.e Wake up at 7AM").grid(row=0, column=1)    
    question_entry = EntryWithPlaceholder(select_type_window, "F.e. did you wake up early").grid(row=1, column=1)
    # frequency_frame = Frame(select_type_window).grid(row=2, column=1) 
    frequency_entry = EntryWithPlaceholder(select_type_window, "max 14 times per week").grid(row=2,column=1)
    remainder_entry = EntryWithPlaceholder(select_type_window, "18:00").grid(row=3, column=1)
    
    notes_entry = EntryWithPlaceholder(select_type_window, "Any additional information").grid(row=4, column=1)

    Button(select_type_window, text="Back",command=get_back).grid(row=5, column=0)
    Button(select_type_window, text="Add", command=create_obejctive("YN")).grid(row=5, column=1)


def add_measurable_objective():
    _button_list = select_type_window.winfo_children()
    _button_list[0].destroy()
    _button_list[1].destroy()

    name = Label(select_type_window,
                  text="Name of task").grid(row=0)

    question = Label(select_type_window,
                      text="Question").grid(row=1)


    frequency = Label(select_type_window,
                      text="Frequency per week").grid(row=2)

    remainder = Label(select_type_window,
                      text="Remainder").grid(row=3)

    notes = Label(select_type_window,
                      text="Notes").grid(row=4)
    unit = Label(select_type_window, text="Unin f.e kilometers").grid(row=5)
    name_entry = EntryWithPlaceholder(select_type_window, "f.e Read pages of the book").grid(row=0, column=1)
    question_entry = EntryWithPlaceholder(select_type_window, "How many kilometers did you run?").grid(row=1, column=1)
    # frequency_frame = Frame(select_type_window).grid(row=2, column=1) 
    frequency_entry = EntryWithPlaceholder(select_type_window, "Max 7 times per week").grid(row=2,column=1)
    remainder_entry = EntryWithPlaceholder(select_type_window, "21:37").grid(row=3, column=1)
    notes_entry = EntryWithPlaceholder(select_type_window, "Any info you find usefull").grid(row=4, column=1)
    unit_entry = EntryWithPlaceholder(select_type_window, "f.e Kilometers").grid(row=5, column=1)

    Button(select_type_window, text="Back",command=get_back).grid(row=6, column=0)
    Button(select_type_window, text="Add", command=create_obejctive("M")).grid(row=6, column=1)



def use_objective_input(selected):
    print(selected)

def create_obejctive(objective_type):
    pass


def get_back():
    _button_list = select_type_window.winfo_children()
    for i in _button_list:
        i.destroy()
    create_starting_btns()

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


# this function creates folder for saves only if user has not done it before
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
