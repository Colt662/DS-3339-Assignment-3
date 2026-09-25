# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    '''
        A class representing a stack of nodes.
        Attributes:
            top (Node or None): The node on the top of the stack.
        Methods:
            push(value): Adds a new Node with the provided value to the top of the stack.
            pop(): Removes the Node at the top of the stack and returns the value, or None if Stack is empty.
            peek(): Returns the value of the Node on the top without removing it, or returns None if Stack is empty.
            print_stack(): Prints out the current stack contents.
    '''

    def __init__(self):
        self.top = None


    def push(self, value):
        old_top = self.top
        self.top = Node(value)
        self.top.next = old_top


    def pop(self):
        if self.top != None:
            old_top = self.top
            self.top = self.top.next
            return old_top.value
        
        else:
            return None


    def peek(self):
        if self.top != None:
            return self.top.value
        
        else:
            return None


    def print_stack(self):
        if self.top == None:
            print(" - Empty Stack")
            return
        
        else:
            current_node = self.top
            while current_node != None:
                print(f'- {current_node.value}')
                current_node = current_node.next



def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()
    
    choice = ""
    while choice != "6":
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")
        
        print("")#extra line for spacing

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack()
            print(f'Action performed: {action}')
            

        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = undo_stack.pop()
            if action != None:
                redo_stack.push(action)
                print(f'Undid Action: {action}')

            else:
                print("No Actions to Undo")
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            action = redo_stack.pop()
            if action != None:
                undo_stack.push(action)
                print(f'Redid Action: {action}')

            else:
                print("No Actions to Redo")


        elif choice == "4":
            # Print the undo stack
            print("Undo Stack:")
            undo_stack.print_stack()
            
            
        elif choice == "5":
            # Print the redo stack
            print("Redo Stack:")
            redo_stack.print_stack()
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()