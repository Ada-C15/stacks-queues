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

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        # try to remove references to last node in stack
        # if successful, return None
        try:
            return self.store.remove_last()
            
        # if there's a problem indicating an empty list,
        # raise a StackEmptyException 
        except:
            raise StackEmptyException

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        return self.store.empty()

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        string_form_like = []
        current = self.store.tail 

        while current:
            string_form_like.append(current.value)
            current = current.last 

        return string_form_like
