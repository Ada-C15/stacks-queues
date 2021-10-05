class EmptyListError(Exception):
    pass

# Defines a node in the singly linked list
class Node:
    def __init__(self, value, next_node = None, previous_node = None):
        self.value = value
        self.next = next_node
        self.previous = previous_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class
        self.tail = None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        #  DON"T GET THIS HERE
        if self.head:
            self.head.previous = new_node
        self.head = new_node
        # if it's empty? 
        if not self.tail:
            self.tail = self.head

    def get_first(self):
        # if empty
        if not self.head:
            return None
        # otherwise
        return self.head.value

    def remove_first(self):
        if not self.head:
            raise EmptyListError("List is empty")

        # start assigning head (you'll remove this)
        value = self.head.value
        # point head to next node
        self.head = self.head.next

        # maybe removed last element!
        if self.head:
            # detach the head
            self.head.previous = None
        return value

    def empty(self):
        # if empty returns true, else false?
        return not self.head

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        # if empty, return false (cant find value)
        if not self.head:
            return False
        
        # if value is at the front
        if self.head.value == value:
            return True

        # search for it, start by assigning first head to a variable
        current = self.head
        # if it's not empty, check value if it's the same, return it , 
        while current:
            if current.value == value:
                return True
            # else, move to next value to check
            current = current.next
        # value isn't found in whole list, return false
        return False


    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def find_max(self):
        if not self.head:
            return None
        
        # start by assigning head to variable and a max value (head in this case)
        current = self.head
        max = current.value

        # while it's not empty, 
        while current:
            # if current max is less than the value that current is currently at
            if max < current.value:
                # you found a new max
                max = current.value
            # else, keep moving along the list
            current = current.next
        return max

    # method to return the min value in the linked list
    # returns the data value and not the node
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def find_min(self):
        if not self.head:
            return None

        current = self.head
        min = current.value
        while not current:
            if min > current.value:
                min = current.value
            current = current.next
        
        return min

    # method that returns the length of the singly linked list
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def length(self):
        # if empty, length is 0
        if not self.head:
            return 0
        # assign head to variable
        current = self.head
        length = 0 # start  length countercounter
        while current:
            # add one per element you move through in the list
            length += 1
            current = current.next
        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns nil if there are fewer nodes in the linked list than the index value
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        # index will always be < than length,  never >= so if length <= index, it means that...
        if self.length() <= index:
            return None

        #start by assigning the head to a variable
        current = self.head
        # index starts at 0
        count = 0
        while current:
            # check that given index matches where we are at, if so, return value at that count/index
            if count == index:
                return current.value
            # else move along and increase by one
            count += 1
            # move along
            current = current.next
        # if at the end the gien index isn't found, return none
        return None

    # method to print all the values in the linked list
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def visit(self):
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next
        
        print(", ".join(values))

    # method to delete the first node found with specified value
    # Time Complexity:  O(n) where n is the number of nodes
    # Space Complexity: O(1)
    def delete(self, value):
        # empty list
        if not self.head:
            return None
        
        current = self.head
        # if you found a value that matches value given
        # if value's right at the head
        if current.value == value:
            self.head = current.next
            if self.head:
                self.head.previous = None
            else:
                tail = None
            return None

        previous = current
        while current:
            if current.value == value:
                previous.next = current.next
                if current.next:
                    current.next.previous = previous
                else:
                    self.tail = current.previous
                    self.tail.next = None
                return None
            else:
                previous = current
            current = current.next

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity:  O(n) where n is the number of nodes
    # Space Complexity: O(1)
    def reverse(self):
        # list is empty
        if not self.head:
            return None

        
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            prev.previous = current

        self.head = prev


    # method that inserts a given value as a new last node in the linked list
    # Time Complexity:  O(n) where n is the number of nodes
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.add_first(value)
            return
    
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def remove_last(self):
        if not self.head:
            raise EmptyListError('List is empty')

        # assigning tail value to a variable
        value = self.tail.value
        # if one element in the list
        if self.head == self.tail:
            # make it none
            self.head = self.tail = None
        # otherwise make the tail point to the tail's previous element before 
        # removing it    
        else:
            self.tail = self.tail.previous
            # disappear the tail!
            self.tail.next = None
        # this is how pop works?
        return value

    # method that returns the value of the last node in the linked list
    # returns nil if the linked list is empty
    # Time Complexity:  O(n) where n is the number of nodes
    # Space Complexity: O(1)
    def get_last(self):
        if not self.head:
            return None

        return self.tail.value

    def __str__(self):
        values = []

        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next

        return ", ".join(values)

ll = LinkedList()
ll.add_first(5)
ll.add_first(25)
ll.add_last(1)
print(ll)
