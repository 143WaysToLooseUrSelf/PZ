import tkinter as tk
from random import randint

symbols_list = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'g', 'x', 'l', 's', 'z', 'w']

def generate_random_symbols():
    try:
        word = len(symbols_list) - 1
        result = ""
        for _ in range(40):
            a = randint(0, word)
            res = symbols_list[a]
            result += res
        return result
    except ValueError:
        return "Error!"

def show_result():
    random_symbols = generate_random_symbols()
    result_label.config(text=random_symbols)

def main():
    root = tk.Tk()
    root.title("Random characters")
    root.geometry("400x300")

    label = tk.Label(root, text="Your 40 characters:", font=("Helvetica", 14))
    label.pack()

    global result_label
    result_label = tk.Label(root, text="", font=("Courier", 16), borderwidth=2, relief="solid")  # Добавлены границы
    result_label.pack()

    button = tk.Button(root, text="Generate new characters", command=show_result)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
