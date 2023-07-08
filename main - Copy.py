import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        history.insert(tk.END, f"{expression} = {result}")
    except Exception as e:
        print(e)
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create a Tkinter window
window = tk.Tk()
window.title("Calculator")

# Set colors
bg_color = "#232323"
btn_bg_color = "#03dffc"
btn_fg_color = "#000"
entry_bg_color = "#000000"
entry_fg_color = "#ffffff"

# Configure window background color
window.configure(bg=bg_color)

# Create an Entry widget for displaying the input and result
entry = tk.Entry(window, width=20, font=("Arial", 14), bg=entry_bg_color, fg=entry_fg_color)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a history section
history = tk.Listbox(window, width=25, height=6, font=("Arial", 12), bg=entry_bg_color, fg=entry_fg_color)
history.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Create buttons for numbers
button_1 = tk.Button(window, text="1", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(1), relief=tk.RAISED)
button_2 = tk.Button(window, text="2", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(2), relief=tk.RAISED)
button_3 = tk.Button(window, text="3", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(3), relief=tk.RAISED)
button_4 = tk.Button(window, text="4", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(4), relief=tk.RAISED)
button_5 = tk.Button(window, text="5", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(5), relief=tk.RAISED)
button_6 = tk.Button(window, text="6", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(6), relief=tk.RAISED)
button_7 = tk.Button(window, text="7", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(7), relief=tk.RAISED)
button_8 = tk.Button(window, text="8", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(8), relief=tk.RAISED)
button_9 = tk.Button(window, text="9", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(9), relief=tk.RAISED)
button_0 = tk.Button(window, text="0", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click(0), relief=tk.RAISED)

# Create other buttons
button_add = tk.Button(window, text="+", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click("+"), relief=tk.RAISED)
button_subtract = tk.Button(window, text="-", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click("-"), relief=tk.RAISED)
button_multiply = tk.Button(window, text="x", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click("*"), relief=tk.RAISED)
button_divide = tk.Button(window, text="/", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=lambda: button_click("/"), relief=tk.RAISED)
button_clear = tk.Button(window, text="C", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=button_clear, relief=tk.RAISED)
button_equal = tk.Button(window, text="=", width=5, height=2, bg=btn_bg_color, fg=btn_fg_color, command=button_equal, relief=tk.RAISED)

# Position the buttons on the grid
button_1.grid(row=2, column=0, padx=2, pady=2)
button_2.grid(row=2, column=1, padx=2, pady=2)
button_3.grid(row=2, column=2, padx=2, pady=2)
button_4.grid(row=3, column=0, padx=2, pady=2)
button_5.grid(row=3, column=1, padx=2, pady=2)
button_6.grid(row=3, column=2, padx=2, pady=2)
button_7.grid(row=4, column=0, padx=2, pady=2)
button_8.grid(row=4, column=1, padx=2, pady=2)
button_9.grid(row=4, column=2, padx=2, pady=2)
button_0.grid(row=5, column=0, padx=2, pady=2)

button_add.grid(row=2, column=3, padx=2, pady=2)
button_subtract.grid(row=3, column=3, padx=2, pady=2)
button_multiply.grid(row=4, column=3, padx=2, pady=2)
button_divide.grid(row=5, column=3, padx=2, pady=2)
button_clear.grid(row=5, column=1, padx=2, pady=2)
button_equal.grid(row=5, column=2, padx=2, pady=2)

# Set round border for buttons
buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0,
           button_add, button_subtract, button_multiply, button_divide, button_clear, button_equal]

for button in buttons:
    button.config(borderwidth=0, relief=tk.RAISED)

# Start the Tkinter event loop
window.mainloop()
