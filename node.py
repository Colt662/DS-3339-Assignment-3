# Implement your Node class here
class Node:
    '''
    A class representing a node for use in a singly linked list.
    Attributes:
        value (any): The value stored by the node
        next (Node or None): The next node in the list
    '''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}'