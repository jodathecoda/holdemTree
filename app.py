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
def show_popup(line, double_suited, pot_type):
    popup = Toplevel()
    popup.title("Action Info")
    msg = f"Line: {line}\nDouble Suited: {'Yes' if double_suited else 'No'}\nPot Type: {pot_type}"
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
    pot_type = tk.StringVar(value="Limped Pot")

    double_suited_check = tk.Checkbutton(frame, text="Double Suited", variable=double_suited)
    double_suited_check.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=5)

    limped_pot_radio = tk.Radiobutton(frame, text="Limped Pot", variable=pot_type, value="Limped Pot")
    minraised_pot_radio = tk.Radiobutton(frame, text="MinRaised Pot", variable=pot_type, value="MinRaised Pot")

    limped_pot_radio.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    minraised_pot_radio.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    # Arrange buttons in two columns with no more than 16 buttons per column
    max_buttons_per_column = 16
    num_columns = 2

    for index, line in enumerate(lines):
        row = (index % max_buttons_per_column) + 2  # +2 to account for the checkbox and radio buttons in the first rows
        col = index // max_buttons_per_column
        button = tk.Button(frame, text=line, command=lambda l=line, ds=double_suited, pt=pot_type: show_popup(l, ds.get(), pt.get()))
        button.grid(row=row, column=col, sticky='ew', padx=5, pady=5)

        # Configure grid to ensure all buttons have the same width
        frame.grid_columnconfigure(col, weight=1)

# Configure root window to resize with content
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
