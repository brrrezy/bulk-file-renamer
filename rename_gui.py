import os
import tkinter as tk
from tkinter import filedialog, messagebox


def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_selected)


def rename_files():
    path = path_entry.get().strip()
    prefix = prefix_entry.get().strip()

    if not os.path.exists(path):
        messagebox.showerror("Error", "Invalid path!")
        return

    if not prefix:
        messagebox.showerror("Error", "Prefix cannot be empty!")
        return

    file_list = os.listdir(path)

    if len(file_list) == 0:
        messagebox.showinfo("Info", "No files found in this folder.")
        return

    count = 1
    for filename in file_list:
        old_path = os.path.join(path, filename)

        if os.path.isfile(old_path):
            suffix = str(count).zfill(3)
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}_{suffix}{ext}"
            new_path = os.path.join(path, new_name)
            os.rename(old_path, new_path)
            count += 1

    messagebox.showinfo("Success", f"{count - 1} files successfully renamed!")


# ---- GUI Setup ----
root = tk.Tk()
root.title("Bulk File Renamer")
root.geometry("500x250")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Bulk File Renamer", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Path Section
path_frame = tk.Frame(root)
path_frame.pack(pady=5)

tk.Label(path_frame, text="Folder Path:").pack(side=tk.LEFT, padx=5)

path_entry = tk.Entry(path_frame, width=40)
path_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(path_frame, text="Browse", command=browse_folder)
browse_button.pack(side=tk.LEFT)

# Prefix Section
prefix_frame = tk.Frame(root)
prefix_frame.pack(pady=10)

tk.Label(prefix_frame, text="Prefix:").pack(side=tk.LEFT, padx=5)

prefix_entry = tk.Entry(prefix_frame, width=30)
prefix_entry.pack(side=tk.LEFT)

# Rename Button
rename_button = tk.Button(
    root, text="Rename Files", width=20, height=2, command=rename_files
)
rename_button.pack(pady=20)

root.mainloop()
