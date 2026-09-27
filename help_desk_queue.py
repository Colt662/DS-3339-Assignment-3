# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    '''
        A class representing a queue of Nodes.
        Attributes:
            front (Node or None): The node at the front of the queue.
            rear (Node or None): The node on the back of the queue.
        Methods:
            enqueue(value): Adds the provided value to the end of the Queue.
            dequeue(): Removes and returns the value at the front of the Queue.
            peek(): Returns the first value in the Queue without removing it.
            print_queue(): Prints out all the values currently in the Queue.
    '''

    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        new_node = Node(value)

        if self.rear != None:
            self.rear.next = new_node
            self.rear = new_node

        else:
            self.rear = new_node
            self.front = new_node

    def dequeue(self):
        if self.front != None:
            old_front = self.front
            self.front = self.front.next
            return old_front.value

        else:
            return None

    def peek(self):
        if self.front != None:
            return self.front.value

        else:
            return None

    def print_queue(self):
        if self.front != None:
            current_node = self.front
            while current_node != None:
                print(f' - {current_node.value}')
                current_node = current_node.next

        else:
            print("Queue is Empty")


def run_help_desk():
    # Create an instance of the Queue class
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            pass # delete this line


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            pass # delete this line


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
