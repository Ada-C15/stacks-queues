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
            returns None
        """
        #self.store will never be None 
        if self.store.empty():
            raise StackEmptyException("Stack is empty")
            return None
            
        return self.store.remove_first()



    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if self.store.length() == 0:
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        return self.store.__str__() 

    def top(self):
        #returns the top of the stack without changing the stack
        #using only public stack methods
        #1. Pop an element off the stack and save it to temp variable
        #2 then push it back onto the stack
        #return temp
        
        temp = self.store.get_first()
        self.store.add_first(temp)
        return temp


    def reverse(self,str):
        #method which takes a strinf as an argument. Returns the reversed string
        #using stack

        n = len(str)
        reversedStr = ""

        #push characters onto the stack
        for i in range(0, n, 1):
            self.store.add_first(str[i])
        
        #pop them off the stack and save to reversedStr
        while not self.store.empty():
            reversedStr += self.store.remove_first()
        
        return reversedStr


        
str = "Paul"
new_stack = Stack()
reversed_string = new_stack.reverse(str)
print(reversed_string)
        
        
