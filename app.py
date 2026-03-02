import tkinter as tk
from tkinter import messagebox
import json
import os

# File name for storage
FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return [] # Handle corrupted or missing file
    return []

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as f:
        json.dump(list(tasks), f)

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_complete():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        if "✔️" not in task:
            task_listbox.delete(index)
            task_listbox.insert(index, f"{task} ✔️")
            save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to mark complete.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Sree's Smart To-Do")
root.geometry("400x500")
root.configure(bg="#000080") # Navy Blue Background

# Title
label = tk.Label(root, text="My Tasks", font=("Arial", 18, "bold"), bg="#000080", fg="white")
label.pack(pady=10)

# Entry Box
task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#000080")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task, bg="white", fg="#000080", width=12)
add_btn.grid(row=0, column=0, padx=5)

complete_btn = tk.Button(btn_frame, text="Complete", command=mark_complete, bg="white", fg="#000080", width=12)
complete_btn.grid(row=0, column=1, padx=5)

# Listbox
task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10, bg="white", fg="#000080")
task_listbox.pack(pady=10, padx=20)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task, bg="#FF4444", fg="white", width=20)
delete_btn.pack(pady=10)

# Initial Load
for t in load_tasks():
    task_listbox.insert(tk.END, t)

root.mainloop()