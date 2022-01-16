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
        # this sets the top of my stack is the head of link list with this method
        self.store.add_first(element)
        return
        

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if not self.store.head:
            raise StackEmptyException("Stack is empty")

        return self.store.remove_first()

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if not self.store.head:
            return True
        else:
            return False
        #  same as
        # return not self.store.head
        

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        if not self.store.head:
            return None

        # return  str(self.store)
        return self.store.__str__()
        
    
    def top(self):
        """ returns top of the stack without changing the stack, using public methods only
        """ 
        
        if not self.store.head:
            return None
        
        return self.store.head

    def reverse(self):
        if not self.store.head:
            return
        
        self.store.reverse()