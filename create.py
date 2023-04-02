import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from visual_effects import *
from visualise_data import *


# saves_path = '/home/grzes/Documents/saves'
saves_path = '/home/grzes/Documents/saves'
# I need to extract data from OptionMenu and validate other data there.
def validate_input(*args):
    # this string is used in validation as a regex
    n = "0123456789"  

    basic_values = [
        'f.e Wake up at 7AM',
        'F.e. did you wake up early',
        '18:00/None',
        'Any additional information',
    ]
    correct_values = [

    ]
    i = 0
    for entry in entries:
        # print(entry)
        if isinstance(entry, OptionMenu):
            correct_values.append(clicked.get())
        elif isinstance(entry, Entry) and entry.get() in basic_values:
            messagebox.showerror('Incorrect values', 'You need to create your own objectives')
            break

# validation for time input
        elif i == 2:
            if entry.get().lower() == "none":
                correct_values.append(entry.get().lower())
            elif len(entry.get()) != 5:
                messagebox.showerror("Incorrect values", "Time shold be in XX:XX format or set as None if you don't want a remainder")
                break
            elif entry.get()[2] != ":":
                messagebox.showerror("Incorrect values", "Time shold be in XX:XX format or set as None if you don't want a remainder")
                break
            elif not (entry.get()[0] in n and entry.get()[1] in n and entry.get()[3] in n and entry.get()[4] in n):
                messagebox.showerror("Incorrect values", "Time shold be in XX:XX format or set as None if you don't want a remainder")
                break
            elif not(0 < int(entry.get().split(":")[0]) < 24 and 0 <= int(entry.get().split(":")[0]) < 60):
                messagebox.showerror("Incorrect values", "Time shold be in XX:XX format or set as None if you don't want a remainder")
                break
            else:
                entries.append(entry.get())

        elif isinstance(entry, Entry):
            correct_values.append(entry.get())
        else:
            correct_values.append(entry)
        i += 1

    if correct_values[1][-1] != "?":
        correct_values[1] = correct_values[1] + "?"

    select_type_window.destroy()
    # print(correct_values)
    return correct_values


# Done - It is meant just to create two buttons
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



# Done - this function is supposed just to make a window
def add_objective():
    global select_type_window
    select_type_window = Toplevel()
    select_type_window.resizable(False, False)
    create_starting_btns()


# Done but there is space for improvement like making length limit for name cell
def add_yes_no_objective():
    global entries
    _button_list = select_type_window.winfo_children()
    _button_list[0].destroy()
    _button_list[1].destroy()

    labels = [
        Label(select_type_window,text="Name of task"),
        Label(select_type_window,text="Question"),
        Label(select_type_window,text="Remainder"),
        Label(select_type_window,text="Notes"),
        Label(select_type_window,text="Frequency per week")
    ]
    for i in range (0, len(labels)):
        labels[i].grid(row=i, column=0)

    options = [
        "everyday",
        "every other day",
        "weekly"
    ]
    global clicked
    clicked = StringVar()

    clicked.set( "everyday" )

    entries = [
        EntryWithPlaceholder(select_type_window, "f.e Wake up at 7AM"),
        EntryWithPlaceholder(select_type_window, "F.e. did you wake up early?"),
        EntryWithPlaceholder(select_type_window, "18:00/None"),
        EntryWithPlaceholder(select_type_window, "Any additional information"),
        OptionMenu(select_type_window, clicked, *options)
    ]
    for i in range(0, len(entries)):
        entries[i].grid(row=i, column=1)

    Button(select_type_window, text="Back",command=get_back).grid(row=len(entries), column=0)
    Button(select_type_window, text="Add", command=use_input).grid(row=len(entries), column=1)


# Done but there is space for improvement
def add_measurable_objective():
    _button_list = select_type_window.winfo_children()
    _button_list[0].destroy()
    _button_list[1].destroy()
    global entries

    labels = [
        Label(select_type_window, text="Name of task"),
        Label(select_type_window, text="Question"),
        Label(select_type_window,text="Remainder"),
        Label(select_type_window,text="Notes"),
        Label(select_type_window, text="Unit f.e kilometers"),
        Label(select_type_window,text="Frequency per week")
    ]
    for i in range (0, len(labels)):
        labels[i].grid(row=i, column=0)

    options = [
        "everyday",
        "every other day",
        "weekly"
    ]
    global clicked
    clicked = StringVar()
    clicked.set("everyday")
    entries = [
        EntryWithPlaceholder(select_type_window, "f.e Read pages of the book"),
        EntryWithPlaceholder(select_type_window, "How many kilometers did you run?"),
        EntryWithPlaceholder(select_type_window, "21:37/None"),
        EntryWithPlaceholder(select_type_window, "Any info you find usefull"),
        EntryWithPlaceholder(select_type_window, "f.e Kilometers"),
        OptionMenu(select_type_window, clicked, *options)
    ]
    for i in range(0, len(entries)):
        entries[i].grid(row=i,column=1)
    
    Button(select_type_window, text="Back",command=get_back).grid(row=len(entries), column=0)
    Button(select_type_window, text="Add", command=use_input).grid(row=len(entries), column=1)


# it has to check wheather it deals with measurable or yes/no objective
def use_input():
    valid_input = validate_input()
    obj_df = pd.DataFrame(
        [valid_input],
        columns=['name', 'question', 'notes', 'frequency', 'remainder']
     )
    # print(obj_df) 
    # print(obj_df['question'][0])
    create_save_file(obj_df, saves_path)


# Done
def get_back():
    _button_list = select_type_window.winfo_children()
    for i in _button_list:
        i.destroy()
    create_starting_btns()


# Partly done
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


# this function creates folder for saves only if user has not done it before
# create_saves_folder()

# create_saves_folder()
