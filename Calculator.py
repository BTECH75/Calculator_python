import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error")

# Function to update the expression in the entry widget
def append_to_expression(value):
    current_text = entry.get()
    new_text = current_text + value
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

# Function to clear the entry widget
def clear_expression():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the entry widget
entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, command=evaluate_expression)
    else:
        btn = tk.Button(root, text=button, command=lambda b=button: append_to_expression(b))
    btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add clear button
clear_button = tk.Button(root, text='C', command=clear_expression)
clear_button.grid(row=row, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

# Add result label
result_label = tk.Label(root, text="Result:", font=('Arial', 14))
result_label.grid(row=row + 1, column=0, columnspan=4)

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
