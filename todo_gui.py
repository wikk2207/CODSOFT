import tkinter as tk
from tkinter import messagebox, Scrollbar
import os
from datetime import datetime

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ashwini's To-Do Manager - CODSOFT")
        self.root.geometry("500x620")
        self.root.config(bg="#e0f2fe")

        # Header
        tk.Label(root, text="Ashwini's To-Do Manager", font=("Segoe UI", 22, "bold"),
                 bg="#e0f2fe", fg="#1e293b").pack(pady=10)

        today = datetime.today().strftime(" %A, %d %B %Y")
        tk.Label(root, text=today, font=("Segoe UI", 12, "italic"),
                 bg="#e0f2fe", fg="#334155").pack()

        # Task input
        self.task_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.task_var, font=("Segoe UI", 14),
                              width=30, bd=0, bg="#f8fafc", fg="#1e293b", insertbackground="#1e293b")
        self.entry.pack(pady=15)
        self.entry.focus()

        # Task list with scrollbar
        frame = tk.Frame(root, bg="#e0f2fe")
        frame.pack(pady=10)

        self.task_list = tk.Listbox(frame, font=("Segoe UI", 14), width=40, height=12,
                                    bg="#f1f5f9", fg="#0f172a", selectbackground="#bae6fd", activestyle="none")
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_list.yview)

        # Button layout
        btn_frame = tk.Frame(root, bg="#e0f2fe")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="➕ Add Task", width=15, command=self.add_task,
                  bg="#4ade80", fg="black", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="Toggle Done", width=15, command=self.toggle_task,
                  bg="#a78bfa", fg="white", font=("Segoe UI", 11, "bold")).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="Delete", width=15, command=self.delete_task,
                  bg="#f87171", fg="white", font=("Segoe UI", 11, "bold")).grid(row=0, column=2, padx=5)

        tk.Button(root, text="Save & Exit", width=48, command=self.save_and_exit,
                  bg="#60a5fa", fg="white", font=("Segoe UI", 11, "bold")).pack(pady=8)

        # Footer
        tk.Label(root, text="© 2025 Ashwini | #codsoft #internship",
                 font=("Segoe UI", 10), bg="#e0f2fe", fg="#64748b").pack(side=tk.BOTTOM, pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.task_list.insert(tk.END, f"⏳ {task}")
            self.task_var.set("")
        else:
            messagebox.showwarning("⚠️ Empty Field", "Please enter a task.")

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            self.task_list.delete(selected[0])
        else:
            messagebox.showinfo("⚠️Select Task", "Please select a task to delete.")

    def toggle_task(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            task = self.task_list.get(index)

            # Toggle icons
            if task.startswith("⏳"):
                updated = task.replace("⏳", "✅", 1)
            elif task.startswith("✅"):
                updated = task.replace("✅", "⏳", 1)
            else:
                updated = "⏳ " + task  # fallback for safety

            self.task_list.delete(index)
            self.task_list.insert(index, updated)
        else:
            messagebox.showinfo("ℹNo Selection", "Select a task to mark done or undo.")

    def save_and_exit(self):
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            for task in self.task_list.get(0, tk.END):
                f.write(task + "\n")
        print("App closed by Ashwini — All tasks saved ")
        self.root.destroy()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                for task in f:
                    cleaned = task.strip()
                    if cleaned:
                        self.task_list.insert(tk.END, cleaned)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
