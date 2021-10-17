from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        self.store = LinkedList()

    # sets new element to the head of the linked list by calling add_first method. Since self.store is an instance of LinkedList class we can call class methods on it
    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
        """
        if isinstance(element, list):
            for index in element:
                self.store.add_first(index)
            
        else:
            self.store.add_first(element)
        return None


    
    
    # self.head.next is set to self.head of linked list
    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        self.store.remove_first()
        
        return None



    # if self.head == None return True 
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
        pass
