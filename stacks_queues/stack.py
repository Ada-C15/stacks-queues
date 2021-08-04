from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        self.store.add_first(element)

    def pop(self):
        return self.store.remove_first()

    def empty(self):
        return self.store.empty()

    def __str__(self):
      return str(self.store)
