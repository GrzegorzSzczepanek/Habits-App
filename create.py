import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from visual_effects import *

# I need to extract data from OptionMenu and validate other data there.
def print_input(*args):
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
        if isinstance(entry, OptionMenu):
            print(clicked.get())

        elif entry.get() in basic_values:
            messagebox.showerror('Incorrect values', 'You need to create your own objectives')
            break

        elif i == 1:
            if entry.get()[-1] != "?":
                entry = entry + "?"

        elif i == 2:
            if len(entry.get()) != 5 and entry.get() != "None":
                messagebox.showerror("Incorrect values", "Time shold be in XX:XX format or set as None if you don't want a remainder")
                break

        correct_values.append(entry.get())
        i += 1

    print(correct_values)


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


# Mostly done
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
    Button(select_type_window, text="Add", command=print_input
           ).grid(row=len(entries), column=1)


# Mostly done - waits for validation
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
        Label(select_type_window, text="Unin f.e kilometers"),
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
    Button(select_type_window, text="Add", command=print_input).grid(row=len(entries), column=1)



# Waiting till valitadion for entries
def use_objective_input(selected):
    print(selected)

def create_obejctive(objective_type):
    pass

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


def change_theme(current_theme):
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
def create_saves_folder():
    if os.path.isdir("C:\\HbtsApp"):
        return 
    else:
        check_path = os.path.join("C:\\", "HbtsApp")
        os.makedirs(check_path)
        path = os.path.join(check_path, "Saves")
        os.makedirs(path)
    return path