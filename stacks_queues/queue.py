# Helpful resource:

# "Queue and Circular Queue Data Structure in Python for Beginners"
# https://www.youtube.com/watch?v=VFSUWEAFmy4

#======================================================
INITIAL_QUEUE_SIZE = 20 # change back to 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        self.buffer_size = INITIAL_QUEUE_SIZE # ~ capacity
        self.front = 0 # ~ head
        self.rear = 0 # ~ tail
        self.size = 0 # number of elements currently in the queue

    def isfull_helper(self):
        """ Returns True if queque is full
        """
        return self.size == self.buffer_size

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        # Check if queque is full using helper method:
        if (self.isfull_helper()): 
            # If full, raise error:
            raise QueueFullException

        # If queque is not full, it's safe to insert an element
        # The current tail index is also the index where we want to insert the element, 
        # since we're always adding to the back of the queue. So we need to store the 
        # element at the store position of the tail:
        self.store[self.rear] = element

        # Then, need to advance the tail index:
        self.rear = (self.rear + 1) % self.buffer_size

        # Also need to increment the size to account for the newly added element:
        self.size += 1


    # ❗️❗️❗️❗️ According to the tests, this method should return a value, not None. 
    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None 
        """
        # Check if queque is empty, and returns none if so:
        if (self.size == 0):
            raise QueueEmptyException
            
        value = self.store[self.front]
        self.front = (self.front + 1) % self.buffer_size

        # Then need to decrement the size to account for the element that was removed:
        self.size -= 1

        return value 


    def get_front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.size == 0:
            return None

        return self.store[self.front]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size 

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return (self.size == 0)

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        if self.size == 0:
            return "[]"

        store_string = "["
        for elem in range(self.front, (self.front + self.size)):
            store_string += (f"{self.store[elem]}, ")

        store_string = store_string[0:-2] # gets rid of the comma at the end
        store_string += "]"

        return store_string

#===========================DEBUGGING FUN=====================================

queue = Queue()
# print("🎸", queue.store)
# queue.enqueue(10)
# print("Adding 10: ", queue.store)
# queue.enqueue(20)
# print("Adding 20: ", queue.store)
# queue.enqueue(30)
# print("Adding 30: ", queue.store)
# print("🐸", queue.store)
# print("👽 Queue front: ", queue.get_front())
# print("Size: ", queue.size)
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# print("Dequeing")
# print("🌺", queue.store)
# print("Size: ", queue.size)
# print(queue.empty())

# queue.enqueue(5)
# queue.enqueue(3)
# queue.enqueue(7)
# print(queue.dequeue() == 5) # Should be True 
# print(str(queue) == "[3, 7]") # Should be True 
# print(str(queue))
# print(not queue.empty()) # Should be True 

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue() == 10) # Should be True 
print(queue.dequeue() == 20) # Should be True 

for num in [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]:
    queue.enqueue(num)

print(str(queue) == "[30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]") # Should be True 