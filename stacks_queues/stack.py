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
        self.store.add_last(element)
        return None

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        # if stack is empty -> raise StackEmptyException (is there anything in this class??)
        if self.store.length() == 0:
            raise StackEmptyException
        else:
            return self.store.remove_last()

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if self.store.length() == 0:
            return True

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        # starting w/ top of stack -> bottom of stack --> need to reverse
        self.store.reverse()
        return self.store.__str__()
