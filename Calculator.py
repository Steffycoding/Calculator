import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 14), bd=10, insertwidth=4,
                         width=14, justify='right', state="disabled")
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=('Arial', 14), bd=8, padx=20, pady=20,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == 'C':
            self.result_var.set('')
        elif button_text == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception:
                self.result_var.set('Error')
        else:
            self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
