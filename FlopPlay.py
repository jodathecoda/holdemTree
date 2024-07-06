import json
import pandas as pd
import tkinter as tk
from tkinter import Label, Toplevel

# Load the CSV file
file_path = 'C:\\Users\\mvelchev\\Learning\\summary.csv'
df = pd.read_csv(file_path)

# Assuming the CSV has columns for actions and cards, we need to preprocess the data accordingly.
# For simplicity, I'll use placeholder values for OOP and IP actions.

# Example structure for the tree:
# Root -> OOP Actions -> Turn Cards -> IP Actions -> River Cards

# Define the actions and cards (placeholders)
oop_actions = ['oopFlopCheck', 'oopFlopBet', 'oopFlopRaise','oopTurnCheck', 'oopTurnBet', 'oopTurnRaise', 'oopTurnDonk','oopRiverCheck', 'oopRiverBet', 'oopRiverRaise', 'oopRiverDonk']
ip_actions = ['ipFlopCheck','ipFlopBet', 'ipFlopRaise','ipTurnCheck', 'ipTurnBet', 'ipTurnRaise','ipRiverCheck', 'ipRiverBet', 'ipRiverRaise']
turn_cards = ['Turn Card 1', 'Turn Card 2']  # Placeholder for turn cards
river_cards = ['River Card 1', 'River Card 2']  # Placeholder for river cards

# Function to create tree nodes
class TreeNode:
    def __init__(self, master, name, details):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.button = tk.Button(self.frame, text=name, command=self.show_details)
        self.button.pack(side=tk.LEFT)

        self.name = name
        self.details = details

    def show_details(self):
        detail_window = Toplevel()
        detail_window.title("Details")
        label = Label(detail_window, text=self.details, justify=tk.LEFT)
        label.pack()

# Function to build the tree structure
def build_tree(master):
    root_node = TreeNode(master, "Root", "Initial State")

    for oop_action in oop_actions:
        oop_node = TreeNode(root_node.frame, oop_action, f"Details for {oop_action}")

        for turn_card in turn_cards:
            turn_node = TreeNode(oop_node.frame, turn_card, f"Details for {turn_card}")

            for ip_action in ip_actions:
                ip_node = TreeNode(turn_node.frame, ip_action, f"Details for {ip_action}")

                for river_card in river_cards:
                    river_node = TreeNode(ip_node.frame, river_card, f"Details for {river_card}")

# Main part of the program
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Poker Actions Tree Visualization")

    tree_frame = tk.Frame(root)
    tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    build_tree(tree_frame)

    root.mainloop()
