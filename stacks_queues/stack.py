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

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns the removed element
        """
        try:
            return self.store.remove_first()
        except:
            raise StackEmptyException("Stack is empty.")

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
        return self.store.visit()
