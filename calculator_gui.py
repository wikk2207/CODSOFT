import customtkinter as ctk

# Set appearance mode
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")  # built-in theme with nice contrast

# Main App Window
app = ctk.CTk()
app.geometry("380x500")
app.title(" Calculator ")

# Entry display
display = ctk.CTkEntry(app, font=("Comic Sans MS", 24), width=340, height=60, corner_radius=15, justify='right', text_color="black")
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Function to handle input
def click(btn_text):
    current = display.get()
    if btn_text == "=":
        try:
            result = str(eval(current))
            display.delete(0, ctk.END)
            display.insert(0, result)
        except:
            display.delete(0, ctk.END)
            display.insert(0, "Error")
    elif btn_text == "C":
        display.delete(0, ctk.END)
    elif btn_text == "DEL":
        display.delete(len(current)-1, ctk.END)
    else:
        display.insert(ctk.END, btn_text)

# Button layout
buttons = [
    ["7", "8", "9", "DEL"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "-"],
    [".", "0", "/", "*"],
    ["C", "=", "Theme"]
]

# Pastel button colors (more visible)
pastel_colors = {
    "bg": "#A3D2CA",        # Mint
    "hover": "#92C9C0",     # Darker Mint
    "accent": "#FFB4B4",    # Peach
    "hover_accent": "#FFA4A4",
    "special": "#B5B2FF",   # Lavender
    "hover_special": "#9F9CFF"
}

# Toggle theme
def toggle_theme():
    current = ctk.get_appearance_mode()
    ctk.set_appearance_mode("dark" if current == "light" else "light")

# Generate buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "Theme":
            btn = ctk.CTkButton(app, text=text, font=("Comic Sans MS", 18, "bold"), width=80, height=60,
                                corner_radius=20, fg_color=pastel_colors["special"],
                                hover_color=pastel_colors["hover_special"], text_color="black",
                                command=toggle_theme)
        else:
            color = pastel_colors["accent"] if text in ["C", "=", "DEL"] else pastel_colors["bg"]
            hover = pastel_colors["hover_accent"] if text in ["C", "=", "DEL"] else pastel_colors["hover"]
            btn = ctk.CTkButton(app, text=text, font=("Comic Sans MS", 18, "bold"), width=80, height=60,
                                corner_radius=20, fg_color=color, hover_color=hover, text_color="black",
                                command=lambda t=text: click(t))
        btn.grid(row=i + 1, column=j, padx=5, pady=5)

# Run App
app.mainloop()
