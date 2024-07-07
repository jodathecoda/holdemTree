import tkinter as tk
from tkinter import Label, Toplevel

# Define the actions
op_check_actions = ['IP_Check', 'IP_Bet_1']
op_bet1_actions = ['IP_Call']
turn_cards = ['Turn1', 'Turn2', 'Turn3', 'Turn4', 'Turn5', 'Turn6', 'Turn7']

# Function to create tree nodes
class TreeNode:
    def __init__(self, master, name, details, depth=0):
        self.master = master
        self.name = name
        self.details = details
        self.depth = depth

        self.frame = tk.Frame(master)
        self.frame.grid(row=TreeNode.row_count, column=depth, sticky='w')

        self.button = tk.Button(self.frame, text=name, command=self.show_details)
        self.button.pack(side=tk.LEFT)

        TreeNode.row_count += 1

        self.children = []

    def show_details(self):
        detail_window = Toplevel()
        detail_window.title("Details")
        label = Label(detail_window, text=self.details, justify=tk.LEFT)
        label.pack()

    def add_child(self, child_node):
        self.children.append(child_node)

# Function to build the tree structure
def build_tree(master):
    root_node = TreeNode(master, "Flop", "Initial State", depth=0)
    
    # OP Check branch
    oop_node_check = TreeNode(master, 'OP_Check', 'OP_Check', depth=1)
    root_node.add_child(oop_node_check)
    
    ip_node_check = TreeNode(master, 'IP_Check', 'IP_Check', depth=2)
    oop_node_check.add_child(ip_node_check)
    
    turn1 = TreeNode(master, 'Turn1', 'Turn1', depth=3)
    ip_node_check.add_child(turn1)
    
    ip_node_bet1 = TreeNode(master, 'IP_Bet_1', 'IP_Bet_1', depth=2)
    oop_node_check.add_child(ip_node_bet1)
    
    oop_node_call = TreeNode(master, 'OP_Call', 'OP_Call', depth=3)
    ip_node_bet1.add_child(oop_node_call)
    
    turn2 = TreeNode(master, 'Turn2', 'Turn2', depth=4)
    oop_node_call.add_child(turn2)
    
    oop_node_raise3 = TreeNode(master, 'OP_Raise_3', 'OP_Raise_3', depth=3)
    ip_node_bet1.add_child(oop_node_raise3)
    
    ip_node_call2 = TreeNode(master, 'IP_Call', 'IP_Call', depth=4)
    oop_node_raise3.add_child(ip_node_call2)
    
    turn3 = TreeNode(master, 'Turn3', 'Turn3', depth=5)
    ip_node_call2.add_child(turn3)
    
    ip_node_raise7 = TreeNode(master, 'IP_Raise_7', 'IP_Raise_7', depth=4)
    oop_node_raise3.add_child(ip_node_raise7)
    
    oop_node_call3 = TreeNode(master, 'OP_Call', 'OP_Call', depth=5)
    ip_node_raise7.add_child(oop_node_call3)
    
    turn4 = TreeNode(master, 'Turn4', 'Turn4', depth=6)
    oop_node_call3.add_child(turn4)
    
    oop_node_allin16 = TreeNode(master, 'OP_Allin_16', 'OP_Allin_16', depth=5)
    ip_node_raise7.add_child(oop_node_allin16)
    
    # OP Bet 1 branch
    oop_node_bet1 = TreeNode(master, 'OP_Bet_1', 'OP_Bet_1', depth=1)
    root_node.add_child(oop_node_bet1)
    
    ip_node_call = TreeNode(master, 'IP_Call', 'IP_Call', depth=2)
    oop_node_bet1.add_child(ip_node_call)
    
    turn5 = TreeNode(master, 'Turn5', 'Turn5', depth=3)
    ip_node_call.add_child(turn5)
    
    oop_node_raise3_2 = TreeNode(master, 'OP_Raise_3', 'OP_Raise_3', depth=3)
    ip_node_call.add_child(oop_node_raise3_2)
    
    ip_node_call3_2 = TreeNode(master, 'IP_Call', 'IP_Call', depth=4)
    oop_node_raise3_2.add_child(ip_node_call3_2)
    
    turn6 = TreeNode(master, 'Turn6', 'Turn6', depth=5)
    ip_node_call3_2.add_child(turn6)
    
    ip_node_raise7_2 = TreeNode(master, 'IP_Raise_7', 'IP_Raise_7', depth=4)
    oop_node_raise3_2.add_child(ip_node_raise7_2)
    
    oop_node_call4 = TreeNode(master, 'OP_Call', 'OP_Call', depth=5)
    ip_node_raise7_2.add_child(oop_node_call4)
    
    turn7 = TreeNode(master, 'Turn7', 'Turn7', depth=6)
    oop_node_call4.add_child(turn7)
    
    oop_node_allin16_2 = TreeNode(master, 'OP_Allin_16', 'OP_Allin_16', depth=5)
    ip_node_raise7_2.add_child(oop_node_allin16_2)
    
    return root_node

# Initialize row count
TreeNode.row_count = 0

# Main part of the program
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Poker Actions Tree Visualization")

    tree_frame = tk.Frame(root)
    tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    build_tree(tree_frame)

    root.mainloop()
