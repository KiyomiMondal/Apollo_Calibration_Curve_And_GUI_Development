import tkinter as tk

root = tk.Tk()
root.title("Film Dosimetry Calculator")
root.geometry("900x600")

root.mainloop()
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Film Dosimetry Calculator")
root.geometry("900x600")

folder_path = tk.StringVar()

def select_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

tk.Label(
    root,
    text="Film Dosimetry Calculator",
    font=("Arial", 16, "bold")
).pack(pady=20)

tk.Button(
    root,
    text="Select Folder",
    command=select_folder,
    width=20
).pack(pady=10)

tk.Label(
    root,
    textvariable=folder_path
).pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Film Dosimetry Calculator")
root.geometry("900x600")

folder_path = tk.StringVar()

def select_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

def process_folder():

    if folder_path.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )
        return

    import os
    import json
    import numpy as np
    from PIL import Image

    # Load calibration
    with open("calibration.json", "r") as f:
        cal = json.load(f)

    a = cal["a"]
    b = cal["b"]
    c = cal["c"]

    results = []

    tif_files = [
        f for f in os.listdir(folder_path.get())
        if f.lower().endswith(".tif")
    ]

    for file in tif_files:

        full_path = os.path.join(
            folder_path.get(),
            file
        )

        img = np.array(Image.open(full_path))

        h, w = img.shape[:2]

        roi = img[
            h//2-100:h//2+100,
            w//2-100:w//2+100
        ]

        pixel = roi[:, :, 0].mean()

        dose = b / (pixel - a) - c

        results.append(
            f"{file}  -->  {dose:.2f} cGy"
        )

    messagebox.showinfo(
        "Dose Results",
        "\n".join(results)
    )
title = tk.Label(
    root,
    text="Film Dosimetry Calculator",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

tk.Button(
    root,
    text="Select Folder",
    command=select_folder,
    width=20
).pack(pady=10)

tk.Label(
    root,
    textvariable=folder_path,
    wraplength=800
).pack(pady=20)

tk.Button(
    root,
    text="Process Folder",
    command=process_folder,
    width=20
).pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import json
import numpy as np
from PIL import Image

# ---------------------------
# Main Window
# ---------------------------

root = tk.Tk()
root.title("Film Dosimetry Calculator")
root.geometry("900x600")

folder_path = tk.StringVar()

# ---------------------------
# Select Folder
# ---------------------------

def select_folder():
    folder = filedialog.askdirectory()

    if folder:
        folder_path.set(folder)

# ---------------------------
# Process Folder
# ---------------------------

def process_folder():

    if folder_path.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )
        return

    # Clear old results
    for row in tree.get_children():
        tree.delete(row)

    # Load calibration
    with open("calibration.json", "r") as f:
        cal = json.load(f)

    a = cal["a"]
    b = cal["b"]
    c = cal["c"]

    tif_files = [
        f for f in os.listdir(folder_path.get())
        if f.lower().endswith(".tif")
    ]

    for file in tif_files:

        full_path = os.path.join(
            folder_path.get(),
            file
        )

        img = np.array(Image.open(full_path))

        h, w = img.shape[:2]

        roi = img[
            h//2-100:h//2+100,
            w//2-100:w//2+100
        ]

        pixel = roi[:, :, 0].mean()

        dose = b / (pixel - a) - c

        tree.insert(
            "",
            "end",
            values=(
                file,
                f"{pixel:.2f}",
                f"{dose:.2f}"
            )
        )

def export_csv():

    import pandas as pd

    rows = []

    for item in tree.get_children():

        rows.append(
            tree.item(item)["values"]
        )

    if len(rows) == 0:

        messagebox.showwarning(
            "Warning",
            "No results to export."
        )

        return

    df = pd.DataFrame(
        rows,
        columns=[
            "File Name",
            "Mean Pixel",
            "Predicted Dose (cGy)"
        ]
    )

    df.to_csv(
        "dose_results.csv",
        index=False
    )

    messagebox.showinfo(
        "Success",
        "dose_results.csv saved successfully"
    )

export_btn = tk.Button(
    root,
    text="Export CSV",
    command=export_csv,
    width=20
)

export_btn.pack(pady=10)
# ---------------------------
# Title
# ---------------------------

title = tk.Label(
    root,
    text="Film Dosimetry Calculator",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)

# ---------------------------
# Select Folder Button
# ---------------------------

select_btn = tk.Button(
    root,
    text="Select Folder",
    command=select_folder,
    width=20
)

select_btn.pack(pady=10)

# ---------------------------
# Folder Label
# ---------------------------

folder_label = tk.Label(
    root,
    textvariable=folder_path,
    wraplength=800
)

folder_label.pack(pady=10)

# ---------------------------
# Process Button
# ---------------------------

process_btn = tk.Button(
    root,
    text="Process Folder",
    command=process_folder,
    width=20
)

process_btn.pack(pady=10)

# ---------------------------
# Results Table
# ---------------------------

columns = (
    "File",
    "Pixel",
    "Dose"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

tree.heading(
    "File",
    text="File Name"
)

tree.heading(
    "Pixel",
    text="Mean Pixel"
)

tree.heading(
    "Dose",
    text="Predicted Dose (cGy)"
)

tree.column(
    "File",
    width=250
)

tree.column(
    "Pixel",
    width=150
)

tree.column(
    "Dose",
    width=200
)

tree.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

root.mainloop()
