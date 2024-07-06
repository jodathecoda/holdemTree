import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label
import re

# Read and parse the file
file_path = 'C:\\Users\\mvelchev\\Learning\\gto\\flops_play.txt'

tabs_data = {}
current_tab = None

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith("Tab_Name"):
            match = re.match(r'Tab_Name\s*=\s*"(.+)"', line)
            if match:
                current_tab = match.group(1)
                tabs_data[current_tab] = []
        elif line and current_tab:
            tabs_data[current_tab].append(line)

# Function to show the popup window
def show_popup(line, double_suited):
    popup = Toplevel()
    popup.title("Action Info")
    msg = f"Line: {line}\nDouble Suited: {'Yes' if double_suited else 'No'}"
    label = Label(popup, text=msg)
    label.pack(padx=10, pady=10)

# Main Tkinter application
root = tk.Tk()
root.title("Poker Flops Play")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

for tab_name, lines in tabs_data.items():
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=tab_name)

    double_suited = tk.BooleanVar()

    double_suited_check = tk.Checkbutton(frame, text="Double Suited", variable=double_suited)
    double_suited_check.grid(row=0, column=0, sticky='w', padx=5, pady=5)

    for index, line in enumerate(lines, start=1):
        button = tk.Button(frame, text=line, command=lambda l=line, ds=double_suited: show_popup(l, ds.get()))
        button.grid(row=index, column=0, sticky='ew', padx=5, pady=5)

        # Configure grid to ensure all buttons have the same width
        frame.grid_columnconfigure(0, weight=1)

# Configure root window to resize with content
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
