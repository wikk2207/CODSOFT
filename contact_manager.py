import customtkinter as ctk
from tkinter import messagebox
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DATA_FILE = "contacts.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_contacts():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_contacts(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ----------------------- Main App -----------------------
app = ctk.CTk()
app.title("Chibi Contact Book")
app.geometry("600x550")

# ------------------ Header -------------------
title_label = ctk.CTkLabel(app, text="(｡♥‿♥｡) Contact Book", font=("Comic Sans MS", 24, "bold"), text_color="#FBEAFF")
title_label.pack(pady=20)

# ------------------ Entry Fields -------------------
entry_frame = ctk.CTkFrame(app, fg_color="#2B2B45")
entry_frame.pack(pady=10)

name_entry = ctk.CTkEntry(entry_frame, placeholder_text="Name", width=250, font=("Arial", 14))
name_entry.grid(row=0, column=0, padx=10, pady=10)

number_entry = ctk.CTkEntry(entry_frame, placeholder_text="Phone Number", width=250, font=("Arial", 14))
number_entry.grid(row=1, column=0, padx=10, pady=10)

nickname_entry = ctk.CTkEntry(entry_frame, placeholder_text="Nickname (opt)", width=250, font=("Arial", 14))
nickname_entry.grid(row=2, column=0, padx=10, pady=10)

# ------------------ Functions -------------------
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    nick = nickname_entry.get()
    if not name or not number:
        messagebox.showwarning("Oops!", "Name & Number are required.")
        return
    data = load_contacts()
    data.append({"name": name, "number": number, "nick": nick})
    save_contacts(data)
    messagebox.showinfo("Saved!", "Contact saved successfully!")
    name_entry.delete(0, 'end')
    number_entry.delete(0, 'end')
    nickname_entry.delete(0, 'end')

def show_contacts():
    data = load_contacts()
    output.delete("0.0", "end")
    if not data:
        output.insert("0.0", "No contacts yet (╥﹏╥)")
    else:
        for idx, contact in enumerate(data, start=1):
            nick = f" ({contact['nick']})" if contact['nick'] else ""
            output.insert("end", f"{idx}. {contact['name']}{nick} - {contact['number']}\n")

def search_contact():
    query = name_entry.get()
    if not query:
        messagebox.showinfo("Type Something", "Enter a name or number to search")
        return
    results = []
    for contact in load_contacts():
        if query.lower() in contact["name"].lower() or query in contact["number"]:
            results.append(contact)
    output.delete("0.0", "end")
    if results:
        for c in results:
            nick = f" ({c['nick']})" if c['nick'] else ""
            output.insert("end", f"{c['name']}{nick} - {c['number']}\n")
    else:
        output.insert("0.0", "No matches found! (；￣Д￣)")

def delete_contact():
    query = name_entry.get()
    if not query:
        messagebox.showinfo("Enter Name", "Enter the contact name to delete.")
        return
    data = load_contacts()
    updated = [c for c in data if c["name"].lower() != query.lower()]
    if len(updated) != len(data):
        save_contacts(updated)
        messagebox.showinfo("Deleted!", "Contact deleted successfully.")
        show_contacts()
    else:
        messagebox.showerror("Error", "No contact found with that name.")

def update_contact():
    query = name_entry.get()
    number = number_entry.get()
    nick = nickname_entry.get()
    if not query or not number:
        messagebox.showwarning("Missing", "Enter name and new number.")
        return
    data = load_contacts()
    for contact in data:
        if contact["name"].lower() == query.lower():
            contact["number"] = number
            contact["nick"] = nick
            save_contacts(data)
            messagebox.showinfo("Updated", "Contact updated successfully.")
            show_contacts()
            return
    messagebox.showerror("Not Found", "No contact found with that name.")

# ------------------ Buttons -------------------
button_frame = ctk.CTkFrame(app, fg_color="#1E1E2F")
button_frame.pack(pady=15)

ctk.CTkButton(button_frame, text="Add (｡♥‿♥｡)", width=120, command=add_contact).grid(row=0, column=0, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Show All (≧◡≦)", width=120, command=show_contacts).grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Search (＠＾◡＾)", width=120, command=search_contact).grid(row=0, column=2, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Update (^人^)", width=120, command=update_contact).grid(row=1, column=0, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Delete (╥﹏╥)", width=120, command=delete_contact, fg_color="red").grid(row=1, column=1, padx=10, pady=10)

# ------------------ Output Area -------------------
output = ctk.CTkTextbox(app, width=520, height=160, font=("Consolas", 14), text_color="#FFDADA", fg_color="#2A2A3B")
output.pack(pady=10)

app.mainloop()
