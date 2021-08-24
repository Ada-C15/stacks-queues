# Stacks & Queues

In this exercise we will implement both a stack & a queue, and then use them in a variety of hands-on exercises.

## Learning Goals

By the end of this exercise you should be able to:

- Implement a stack & a queue using linked lists and arrays
- Write a Queue using a circular buffer
- Use a stack and a queue to solve common interview problems.

## Wave 1 - Implement a Stack

Using a Linked list (from a previous exercise) implement a Stack with the following methods:

- `push(value)` - Adds the value to the top of the stack
- `pop` - Removes and returns an element from the top of the stack
- `empty?` returns true if the stack is empty and false otherwise

## Wave 2 Implement a Queue

Using a circular buffer with an internal array starting at 20 elements, implement a Queue with the following methods:

- `enqueue(value)` - Adds the value to the back of the queue.
  - This method should raise a `QueueFullException` if the buffer size is exceeded (20 elements).
- `dequeue` - removes and returns a value from the front of the queue
- `empty?` returns true if the queue is empty and false otherwise

**Note**:  You are **required** to implement this Queue class using a circular buffer.  Do **not** use a linked list.

## Going Further

Currently the Queue should report a `QueueFullException` if more elements are added than can be stored in the queue.  To go further make the buffer resize if more elements are needed, but retain the circular buffer methodology.  You will need to adjust a test.

#### Additional Exercise

If you finish the previous waves, complete [breadth-first-search](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/) on the binary trees project using a Queue.  
