import tkinter as tk
from tkinter import ttk

def on_entry_click(event):
    """Function that gets called whenever entry is clicked"""
    # if this is a 'default' message
    if event.widget.get() == event.widget.default_text:
        event.widget.delete(0, "end") # delete all the text in the entry
        event.widget['fg'] = 'black'

def on_focusout(event):
    """Function that gets called when focus is lost from entry widget"""
    if event.widget.get() == '':
        event.widget.insert(0, event.widget.default_text)
        event.widget['fg'] = 'grey'

def on_sign_up_click(entries):
    """Function that gets called when 'Sign Up' button is clicked"""
    for entry in entries:
        entry.delete(0, "end")
        entry.insert(0, entry.default_text)
        entry['fg'] = 'grey'

def create_form():
    window = tk.Tk()
    window.title("Contact Us")
    window.configure(bg='grey')

    # Center the window
    window_width = 300
    window_height = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create 'Contact Us' label at the top
    contact_us_label = tk.Label(window, text="Contact Us", bg='grey', font=("Arial", 20))
    contact_us_label.pack(pady=10)

    # Create form fields with placeholders
    fields = [('First Name', 'John'), ('Last Name', 'Smith'), ('Email', 'example@email.com'),
              ('Website', 'https://www.example.com'), ('Password', '8-10 characters'),
              ('Password Confirmation', 'Type your password again')]
    entries = []
    for field, placeholder in fields:
        row = tk.Frame(window, bg='grey')
        label = tk.Label(row, text=field, bg='grey', width=20)
        entry = tk.Entry(row)
        entry.insert(0, placeholder)
        entry.default_text = placeholder
        entry.bind('<FocusIn>', on_entry_click)
        entry.bind('<FocusOut>', on_focusout)
        entry.config(fg = 'grey')
        entries.append(entry)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        label.pack(side=tk.TOP)
        entry.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)

    # Create Sign Up button
    sign_up_button = ttk.Button(window, text="Sign Up", command=lambda: on_sign_up_click(entries))
    sign_up_button.pack(pady=10)

    window.mainloop()

create_form()
