import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard():
    password = password_output.get()
    pyperclip.copy(password)

def generate_password_gui():
    try:
        length = int(length_entry.get())
        if length > 0:
            password = generate_password(length)
            password_output.delete(0, tk.END)
            password_output.insert(0, password)
        else:
            password_output.delete(0, tk.END)
            password_output.insert(0, "Length must be positive")
    except ValueError:
        password_output.delete(0, tk.END)
        password_output.insert(0, "Invalid Length")

# Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")

# Length label and entry
length_label = ttk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
length_entry = ttk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Generate button
generate_button = ttk.Button(window, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Password output label and entry
password_output_label = ttk.Label(window, text="Generated Password:")
password_output_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
password_output = ttk.Entry(window, width=30)
password_output.grid(row=2, column=1, padx=10, pady=10)

# Copy button
copy_button = ttk.Button(window, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()