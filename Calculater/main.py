import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get the numbers from the entry fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        # Perform the calculation based on the selected operation
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        # Display the result
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

#for icon 
#icon_image=tk.PhotoImage(file='icon.ico')
#root.iconphoto(True,icon_image)

# Create and place the widgets
label_num1 = tk.Label(root, text="Enter the first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter the second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

operation_var = tk.StringVar(value="Addition")  # Default operation

label_operation = tk.Label(root, text="Select an operation:")
label_operation.pack()

operations = ["Addition", "Subtraction", "Multiplication", "Division"]
for operation in operations:
    rb = tk.Radiobutton(root, text=operation, variable=operation_var, value=operation)
    rb.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Start the GUI event loop
root.mainloop()