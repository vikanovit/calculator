import tkinter as tk
from typing import List

history: List[str] = []


def insert_number(number: str) -> None:
    """Добавляет цифру или символ в поле ввода.

    Возвращает: None
    """
    current = calc_entry.get()
    calc_entry.delete(0, tk.END)
    calc_entry.insert(0, str(current) + str(number))


def clear_entry() -> None:
    """Очищает поле ввода калькулятора.

    Возвращает: None
    """
    calc_entry.delete(0, tk.END)


def calculate_result() -> None:
    """Вычисляет результат выражения и сохраняет его в историю.

    Возвращает: None
    """
    global history
    try:
        expression = calc_entry.get()
        result = eval(expression)

        history.append(f"{expression} = {result}")

        if len(history) > 10:
            history.pop(0)

        calc_entry.delete(0, tk.END)
        calc_entry.insert(0, result)

    except Exception as ex:
        calc_entry.delete(0, tk.END)
        calc_entry.insert(0, ex)


def show_history_window() -> None:
    """Открывает окно с историей операций.

    Возвращает: None
    """
    history_window = tk.Toplevel(root)
    history_window.title("История операций")
    history_window.configure(bg="#FFC0CB")

    listbox = tk.Listbox(history_window, width=35, height=10)
    listbox.pack(padx=10, pady=10)

    for item in history:
        listbox.insert(tk.END, item)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Калькулятор")
    root.configure(bg="#FFC0CB")

    calc_entry = tk.Entry(root, width=45, bg="white")
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
            btn = tk.Button(
                root,
                text=button,
                width=6,
                height=2,
                bg="#FFC0CB",
                font=font_size,
                command=clear_entry
            )
        else:
            btn = tk.Button(
                root,
                text=button,
                width=6,
                height=2,
                bg="#FFC0CB",
                font=font_size,
                command=lambda x=button: insert_number(x)
            )

        btn.grid(row=row, column=col)

        col += 1
        if col > 3:
            col = 0
            row += 1

    btn_equal = tk.Button(
        root,
        text="=",
        width=6,
        height=2,
        bg="#FFC0CB",
        font=("Arial", 16),
        command=calculate_result
    )
    btn_equal.grid(row=6, column=3)

    btn_history = tk.Button(
        root,
        text="🕒",
        height=2,
        bg="#FFC0CB",
        command=show_history_window
    )
    btn_history.grid(row=6, column=0, columnspan=3, sticky="we")

    root.mainloop()