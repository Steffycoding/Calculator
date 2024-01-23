import tkinter as tk
from tkinter import ttk
import sympy as sp

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("300x400")

        # Entry for input
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(self.master, textvariable=self.input_var, font=("Arial", 14), justify="right")
        self.input_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        # Calculator buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('Back', 5, 1)
        ]

        # Create buttons without colors (dark theme)
        for (text, row, col) in buttons:
            style_name = f"{text}.TButton"
            self.master.style = ttk.Style()
            self.master.style.configure(style_name, font=("Arial", 12), padding=5, background='#001F3F', foreground='black')
            button = ttk.Button(self.master, text=text, command=lambda t=text: self.on_button_click(t), style=style_name)
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Configure row and column weights
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = self.safe_eval(self.input_var.get())
                self.input_var.set(result)
            except ValueError:
                self.input_var.set("Error")
        elif value == 'C':
            self.input_var.set("")
        elif value == 'Back':
            current_input = self.input_var.get()
            self.input_var.set(current_input[:-1])
        else:
            current_input = self.input_var.get()
            self.input_var.set(current_input + value)

    def safe_eval(self, expression):
        try:
            # Use sympy to evaluate the expression safely
            result = sp.sympify(expression)
            return float(result.evalf())
        except (sp.SympifyError, ValueError):
            # Handle errors during evaluation
            raise ValueError("Invalid expression")

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    calculator.run()
