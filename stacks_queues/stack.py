from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass
    # how does an exception class work?

class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns element
        """
        # why should this return None?
        return self.store.add_first(element)

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns element
        """
        if self.empty():
            raise StackEmptyException()
        return self.store.remove_first()

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if self.store.length() == 0:
            return True
        return False

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        stack_list = []
        for elem in self.store:
            stack_list.append(elem)
        return str(stack_list)
