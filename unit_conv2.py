import tkinter as tk

# Step 1: Create the main window
window = tk.Tk()
window.title("Smart Unit Converter")
window.geometry("500x300")

# Step 2: Conversion formulas
conversion_factors = {
    "Metre to Centimetre": 100,
    "Kilogram to Gram": 1000,
    "Kilometre to Metre": 1000,
    "Millimetre to Centimetre": 0.1,
    "Centimetre to Millimetre": 10,
    "Metre to Kilometre": 0.001,
    "Kilometre to Metre": 1000
}

# Step 3: Function to perform conversion
def convert():
    try:
        input_value = float(entry.get())
        conversion_type = selected_conversion.get()
        factor = conversion_factors[conversion_type]
        result = input_value * factor
        result_label.config(text=f"{input_value} {conversion_type.split(' to ')[0]} = {result} {conversion_type.split(' to ')[1]}")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Step 4: Dropdown menu to select conversion
selected_conversion = tk.StringVar(window)
selected_conversion.set("Metre to Centimetre")  # default value

dropdown = tk.OptionMenu(window, selected_conversion, *conversion_factors.keys())
dropdown.pack(pady=10)

# Step 5: Entry to type value
entry_label = tk.Label(window, text="Enter value:")
entry_label.pack()

entry = tk.Entry(window)
entry.pack(pady=5)

# Step 6: Convert button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack(pady=10)

# Step 7: Result display
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Step 8: Run the application
window.mainloop()
