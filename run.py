from tkinter import *

history = []

def click_on_button(number):
    current = calc_entry.get()
    calc_entry.delete(0, END)
    calc_entry.insert(0, str(current) + str(number))

def click_on_button_clear():
    calc_entry.delete(0, END)

def click_on_button_equal():
    global history
    try:
        expression = calc_entry.get()
        result = eval(expression)

        history.append(f"{expression} = {result}")

        if len(history) > 10:
            history.pop(0)

        calc_entry.delete(0, END)
        calc_entry.insert(0, result)

    except Exception as ex:
        calc_entry.delete(0, END)
        calc_entry.insert(0, ex)

def show_history():
    history_window = Toplevel(root)
    history_window.title("История операций")
    history_window.configure(bg="#FFC0CB")

    listbox = Listbox(history_window, width=35, height=10)
    listbox.pack(padx=10, pady=10)

    for item in history:
        listbox.insert(END, item)

root = Tk()
root.title("Калькулятор")
root.configure(bg="#FFC0CB")

calc_entry = Entry(root, width=45, bg="white")
calc_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', ',', 'C', '+'
]

big_symbols = ['+', '-', '*', '/', '🕒']

row = 1
col = 0

for button in buttons:

    font_size = ("Arial", 12)

    if button in big_symbols:
        font_size = ("Arial", 16)

    if button == 'C':
        Button(
            root,
            text=button,
            width=6,
            height=2,
            bg="#FFC0CB",
            font=font_size,
            command=click_on_button_clear
        ).grid(row=row, column=col)

    else:
        Button(
            root,
            text=button,
            width=6,
            height=2,
            bg="#FFC0CB",
            font=font_size,
            command=lambda x=button: click_on_button(x)
        ).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Кнопка =
Button(
    root,
    text="=",
    width=6,
    height=2,
    bg="#FFC0CB",
    font=("Arial", 16),
    command=click_on_button_equal
).grid(row=6, column=3)

# Кнопка истории
Button(
    root,
    text="🕒",
    height=2,
    bg="#FFC0CB",
    command=show_history
).grid(row=6, column=0, columnspan=3, sticky="we")

root.mainloop()