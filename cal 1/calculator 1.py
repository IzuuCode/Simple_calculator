import tkinter as tk


def press(num):
    expression_field.insert(tk.END, num)


def equalpress():
    try:
        result = str(eval(expression_field.get()))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, result)
    except:
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, "Error")

def clear():
    expression_field.delete(0, tk.END)


window = tk.Tk()
window.title("Calculator Project")
window.geometry("350x450")
window.configure(bg="grey")

expression_field = tk.Entry(window, font=('Arial', 20), borderwidth=10, relief=tk.FLAT, bg="#252525", fg="#FFFFFF")
expression_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)


buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


button_font = ('impact', 14)
button_bg = "#ADD8E6"
button_fg = "black"
button_active_bg = "#45A049"
button_active_fg = "black"


for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, height=2, width=6, command=equalpress, bg=button_bg, fg=button_fg, 
                  font=button_font, activebackground=button_active_bg, activeforeground=button_active_fg).grid(row=row, column=col, pady=5, padx=5)
    else:
        tk.Button(window, text=text, height=2, width=6, command=lambda t=text: press(t), bg=button_bg, fg=button_fg, 
                  font=button_font, activebackground=button_active_bg, activeforeground=button_active_fg).grid(row=row, column=col, pady=5, padx=5)


tk.Button(window, text='Clear', height=2, width=5, command=clear, bg="#f44336", fg=button_fg, font=button_font, 
          activebackground="#d32f2f", activeforeground=button_active_fg).grid(row=5, column=0, columnspan=4, pady=5, padx=5)


window.mainloop()
