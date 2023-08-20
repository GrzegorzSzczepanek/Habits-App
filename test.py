import tkinter as tk

def calculate():
    selected_value = radio_var.get()
    num = spinbox.get()
    
    if selected_value == "Double":
        result = num * 2
    elif selected_value == "Triple":
        result = num * 3
    else:
        result = num
    
    result_label.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Spinbox and Radio Buttons")

# Create a variable to hold the selected value
radio_var = tk.StringVar()

# Create radio buttons
radio_double = tk.Radiobutton(window, text="Double", variable=radio_var, value="Double")
radio_triple = tk.Radiobutton(window, text="Triple", variable=radio_var, value="Triple")
radio_none = tk.Radiobutton(window, text="None", variable=radio_var, value="None")

# Create a Spinbox for numeric input
spinbox = tk.Spinbox(window, from_=0, to=100)

# Create a button to perform calculations
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")

# Layout widgets
radio_double.pack()
radio_triple.pack()
radio_none.pack()
spinbox.pack()
calculate_button.pack()
result_label.pack()

# Start the main loop
window.mainloop()
