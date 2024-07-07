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
#oop_actions = ['oopFlopCheck', 'oopFlopBet', 'oopFlopRaise','oopTurnCheck', 'oopTurnBet', 'oopTurnRaise', 'oopTurnDonk','oopRiverCheck', 'oopRiverBet', 'oopRiverRaise', 'oopRiverDonk']
#ip_actions = ['ipFlopCheck','ipFlopBet', 'ipFlopRaise','ipTurnCheck', 'ipTurnBet', 'ipTurnRaise','ipRiverCheck', 'ipRiverBet', 'ipRiverRaise']
#turn_cards = ['Turn Card 1', 'Turn Card 2']  # Placeholder for turn cards
#river_cards = ['River Card 1', 'River Card 2']  # Placeholder for river cards
OP1 = ['OP_Check', 'OP_Bet_1']
IP1_after_OP_Check = ['IP_Check', 'IP_Bet_1']
turn_cards = ['hot', 'cold', 'scary']

# Function to create tree nodes
class TreeNode:
    def __init__(self, master, name, details):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.button = tk.Button(self.frame, text=name, command=self.show_details)
        self.button.pack(side=tk.LEFT)

        self.name = name
        self.details = details
        self.children = []  # List to store child nodes

    def show_details(self):
        detail_window = Toplevel()
        detail_window.title("Details")
        label = Label(detail_window, text=self.details, justify=tk.LEFT)
        label.pack()

    def add_child(self, child_node):
        self.children.append(child_node)

# Function to build the tree structure
def build_tree(master):
    root_node = TreeNode(master, "Flop", "Initial State")
    
    oop_node_check = TreeNode(root_node.frame, 'OP_Check', f'OP_Check')
    root_node.add_child(oop_node_check)  # Add oop_node_check as a child of root_node
    
    if True:
        ip_node_check = TreeNode(oop_node_check.frame, 'IP_Check', f'IP_Check')
        oop_node_check.add_child(ip_node_check)  # Add ip_node_check as a child of oop_node_check
        
        ip_node_bet1 = TreeNode(oop_node_check.frame, 'IP_Bet_1', f'IP_Bet_1')
        oop_node_check.add_child(ip_node_bet1)  # Add ip_node_bet1 as a child of oop_node_check
    
    oop_node_bet1 = TreeNode(root_node.frame, 'OP_Bet_1', f'OP_Bet_1')
    root_node.add_child(oop_node_bet1)  # Add oop_node_bet1 as a child of root_node
    
    return root_node  # Return the root node for further use

# Main part of the program
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Poker Actions Tree Visualization")

    tree_frame = tk.Frame(root)
    tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    build_tree(tree_frame)

    root.mainloop()
