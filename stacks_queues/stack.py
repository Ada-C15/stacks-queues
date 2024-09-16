from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
        """
        self.store.add_first(element)
        return None

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if self.empty():
            raise StackEmptyException("The Stack is empty")
        return self.store.remove_first()
    
    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        return self.store.length() == 0

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        my_list =  self.store
        return str(my_list)
