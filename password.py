import customtkinter as ctk
import random
import string
import pyperclip

# Setup theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Generate password logic
def generate_password():
    length = int(slider.get())
    char_pool = ""

    if lowercase_var.get():
        char_pool += string.ascii_lowercase
    if uppercase_var.get():
        char_pool += string.ascii_uppercase
    if digits_var.get():
        char_pool += string.digits
    if symbols_var.get():
        char_pool += string.punctuation

    if not char_pool:
        password_label.configure(text="❌ Select at least one character type!", text_color="red")
        return

    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_label.configure(text=password, text_color="#00ffcc")

def copy_password():
    pyperclip.copy(password_label.cget("text"))
    password_label.configure(text="✅ Password copied!", text_color="lightgreen")

# App window
app = ctk.CTk()
app.geometry("500x400")
app.title("🔐 Advanced Password Generator")

title = ctk.CTkLabel(app, text="🔐 Secure Password Generator", font=("Helvetica", 22, "bold"))
title.pack(pady=20)

slider = ctk.CTkSlider(app, from_=6, to=32, number_of_steps=26, width=300)
slider.set(12)
slider.pack(pady=10)

slider_label = ctk.CTkLabel(app, text="Select Password Length", font=("Arial", 14))
slider_label.pack(pady=5)

# Checkboxes for customization
lowercase_var = ctk.BooleanVar(value=True)
uppercase_var = ctk.BooleanVar(value=True)
digits_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=False)

frame = ctk.CTkFrame(app)
frame.pack(pady=10)

ctk.CTkCheckBox(frame, text="Lowercase", variable=lowercase_var).grid(row=0, column=0, padx=10)
ctk.CTkCheckBox(frame, text="Uppercase", variable=uppercase_var).grid(row=0, column=1, padx=10)
ctk.CTkCheckBox(frame, text="Digits", variable=digits_var).grid(row=1, column=0, padx=10)
ctk.CTkCheckBox(frame, text="Symbols", variable=symbols_var).grid(row=1, column=1, padx=10)

# Button
generate_button = ctk.CTkButton(app, text="✨ Generate Password", command=generate_password, hover_color="#1f6aa5")
generate_button.pack(pady=15)

# Password output
password_label = ctk.CTkLabel(app, text="", font=("Courier", 16, "bold"))
password_label.pack(pady=10)

# Copy button
copy_btn = ctk.CTkButton(app, text="📋 Copy Password", command=copy_password, fg_color="#333")
copy_btn.pack()

app.mainloop()
