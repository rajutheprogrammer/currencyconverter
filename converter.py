import tkinter as tk
from tkinter import ttk

# Create a Tkinter window
window = tk.Tk()
window.title("Unit Converter")

# Function to convert units
def convert():
    value = float(entry.get())
    input_unit = input_combobox.get()
    output_unit = output_combobox.get()

    # Conversion logic here
    if input_unit == "Celsius" and output_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif input_unit == "Fahrenheit" and output_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value

    result_label.configure(text=f"Result: {result}")

# Create a label for the entry
entry_label = ttk.Label(window, text="Enter a value:")
entry_label.pack()

# Create an entry field
entry = ttk.Entry(window)
entry.pack()

# Create a label for the input unit combobox
input_label = ttk.Label(window, text="From:")
input_label.pack()

# Create a combobox for input units
input_combobox = ttk.Combobox(window, values=["Celsius", "Fahrenheit"])
input_combobox.pack()

# Create a label for the output unit combobox
output_label = ttk.Label(window, text="To:")
output_label.pack()

# Create a combobox for output units
output_combobox = ttk.Combobox(window, values=["Celsius", "Fahrenheit"])
output_combobox.pack()

# Create a button to perform the conversion
convert_button = ttk.Button(window, text="Convert", command=convert)
convert_button.pack()

# Create a label to display the result
result_label = ttk.Label(window, text="Result: ")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
