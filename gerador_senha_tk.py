import random
import string
import tkinter as tk
from tkinter import messagebox

def validate_password(password, use_uppercase, use_lowercase, use_digits, use_symbols):
    has_upper = any(char.isupper() for char in password) if use_uppercase else True
    has_lower = any(char.islower() for char in password) if use_lowercase else True
    has_digit = any(char.isdigit() for char in password) if use_digits else True
    has_symbol = any(char in string.punctuation for char in password) if use_symbols else True
    valid_length = len(password) >= 6

    return all([has_upper, has_lower, has_digit, has_symbol, valid_length])

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True, max_attempts=1000):
    if length < 6:
        raise ValueError("O comprimento mínimo da senha deve ser 6.")

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    attempts = 0

    while True:
        attempts += 1
        if attempts > max_attempts:
            raise ValueError("Não foi possível gerar uma senha válida com as configurações fornecidas. Tente ajustar as opções de caracteres.")
        
        password = ''.join(random.choice(characters) for i in range(length))
        if validate_password(password, use_uppercase, use_lowercase, use_digits, use_symbols):
            return password

def generate_password_gui():
    try:
        length = int(length_entry.get())

        if length < 6:
            messagebox.showerror("Erro", "O comprimento da senha deve ser um número inteiro maior ou igual a 6.")
            return

        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        new_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        result_label.config(text=f"Senha gerada: {new_password}")
    except ValueError:
        messagebox.showerror("Erro", "O comprimento da senha deve ser um número inteiro.")

# Configuração da Interface Gráfica
root = tk.Tk()
root.title("Gerador de Senhas")

tk.Label(root, text="Comprimento da Senha (mínimo 6):").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Incluir letras maiúsculas", variable=uppercase_var).grid(row=1, column=0, columnspan=2)
tk.Checkbutton(root, text="Incluir letras minúsculas", variable=lowercase_var).grid(row=2, column=0, columnspan=2)
tk.Checkbutton(root, text="Incluir números", variable=digits_var).grid(row=3, column=0, columnspan=2)
tk.Checkbutton(root, text="Incluir símbolos", variable=symbols_var).grid(row=4, column=0, columnspan=2)

tk.Button(root, text="Gerar Senha", command=generate_password_gui).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
