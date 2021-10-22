from stacks_queues.linked_list import LinkedList


class StackEmptyException(Exception):
    pass


class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        self.store.add_last(element)
        return None

    def pop(self):
        if not self.store.head:
            raise StackEmptyException

        return self.store.remove_last()

    def empty(self):
        if not self.store.head:
            return True
        else:
            return False
        """ Returns True if the Stack is empty
            And False otherwise
        """

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        pass
