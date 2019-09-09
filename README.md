# Stacks & Queues

In this exercise we will implement both a stack & a queue, and then use them in a variety of hands-on exercises.

Due:  **Monday Sept 9th**

## Learning Goals

By the end of this exercise you should be able to:

- Implement a stack & a queue using linked lists and arrays
- Write a Queue with a circular buffer
- Use a stack and a queue to solve common interview problems.

## Wave 1 - Implement a Stack

Using a Linked list (from a previous exercise) implement a Stack with the following methods:

- `push(value)` - Adds the value to the top of the stack
- `pop` - Removes and returns an element from the top of the stack
- `empty?` returns true if the stack is empty and false otherwise

## Wave 2 Implement a Queue

Using a circular buffer implement a Queue with the following methods:

- `enqueue(value)` - Adds the value to the back of the queue.
- `dequeue` - removes and returns a value from the front of the queue
- `empty?` returns true if the queue is empty and false otherwise

## Wave 3

Complete the methods in `lib/problems.rb` including:

### `balanced(string)`

Given a string containing opening and closing braces, check if it represents a balanced expression or not.

For example:

`{[{}{}]}`, and `{{}{}}` are balanced expressions.

`{()}[)`, and `{(})` are not balanced


## Optional Wave 4

### `evaluate_postfix(expression)`

For solving a mathematical expression we sometimes use postfix form.  For example:  `35+` in postfix evaluates to 3 + 5 = 8.  

Similarly `35+6*` = (3 + 5) * 6

Here also we have to use the stack data structure to solve the postfix expressions.

From the postfix expression, when some operands are found, push them in the stack. When some operator is found, two items are popped from the stack and the operation is performed in correct sequence. After that, the result is also pushed in the stack for future use. After completing the whole expression, the final result is also stored in the stack top.

**Example: Input and Output**

**Input:**
  Postfix expression: `53+62/*35*+`

**Output:**
  The result is: 39


#### Additional Exercise

If you finish the previous waves, complete [breadth-first-search](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/) on the binary trees project using a Queue.  
