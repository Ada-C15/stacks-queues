# Defines a node in the singly linked list
class Node
  attr_reader :data # allow external entities to read value but not write
  attr_accessor :next, :previous # allow external entities to read or write next node

  def initialize(value, next_node = nil, previous_node = nil)
    @data = value
    @next = next_node
    @previous = previous_node
  end
end

# Defines the singly linked list
class LinkedList
    def initialize
      @head = nil # keep the head private. Not accessible outside this class
      @tail = nil
    end

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity O(1)
    def add_first(value)
      new_node = Node.new(value)
      new_node.next = @head

      @head.previous = new_node unless @head.nil?
      @head = new_node
      if @tail.nil?
        @tail = @head
      end
    end

    def remove_first()
      raise ArgumentError, "Empty" if self.empty?

      value = @head.data
      @head = @head.next
      @head.previous = nil unless @head.nil?
      return value
    end

    def empty?
      return @head.nil?
    end

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(value)
      return false if @head.nil?
      return true if @head.data = value
      current = @head
      until current.data.nil?
        return true if current.data = value
        current = current.next
      end
    end

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def find_max
      return nil if @head.nil?
      current = @head
      max = current.data
      until current.nil?
        max = current.data if current.data > max
        current = current.next
      end
      return max
    end

    # method to return the min value in the linked list
    # returns the data value and not the node
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def find_min
      return nil if @head.nil?
      current = @head
      min = current.data
      until current.nil?
        if current.data < min
          min = current.data 
        end
        current = current.next
      end
      return min
    end


    # method that returns the length of the singly linked list
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def length
      return 0 if @head.nil?
      length = 0
      current = @head
      until current.nil?
        current = current.next
        length += 1
      end
      return length
      
    end

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns nil if there are fewer nodes in the linked list than the index value
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def get_at_index(index)
      return nil if length <= index
      current = @head
      count = 0
      until current.nil?
        return current.data if count == index
        current = current.next
        count += 1
      end
    end

    # method to print all the values in the linked list
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def visit
      current = @head
      until current.nil?
        puts current.data
        current = current.next
      end
    end

    # method to delete the first node found with specified value
    # Time Complexity:  O(n) where n is the number of nodes
    # Space Complexity: O(1)
    def delete(value)
      return if @head.nil?
      current = @head

      if current.data == value
        @head = current.next
        @head.previous = nil unless @head.nil?
        return
      end

      prev = current
      until current.nil?
        if current.data == value
          prev.next = current.next
          current.next.previous = prev unless current.next.nil?
          @tail = prev if @tail == current
        else
          prev = current
        end
        current = current.next
      end
    end

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity:  O(n) where n is the number of nodes
    # Space Complexity: O(1)
    def reverse
      return nil if @head.nil?
      prev = nil
      current = @head
      until current.nil?
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        prev.previous = current

      end

      @head = prev

    end


    ## Advanced Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def find_middle_value
      return nil if @head.nil?
      current = @head
      if length % 2 == 0
        return nil
      else
        middle_index = length / 2
      end
      index = 0
      until current.nil?
        return current.data if index == middle_index
        current = current.next
        index += 1
      end

    end

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(n)
      return nil if @head.nil?
      current = @head
      index = 0
      until current.nil?
        if index == length - n - 1
          return current.data
        end
        index += 1
        current = current.next
      end
    end

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def has_cycle
      return nil if @head.nil?
      slow_p = @head
      fast_p = @head
      while slow_p != nil && fast_p != nil and fast_p.next != nil
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p
          return true
        end
        return false
      end
    end


    # Additional Exercises 
    # returns the value in the first node
    # returns nil if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first
      return nil if @head.nil?
      return @head.data
    end

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity:  O(n) where n is the number of nodes
    # Space Complexity: O(1)
    def add_last(value)
      new_node = Node.new(value)
      if @head.nil?
        self.add_first(value)
        return
      end
      @tail.next = new_node
      new_node.previous = @tail
      @tail = new_node
    end

    def remove_last()
      value = @tail.data
      if @head == @tail
        @head = @tail = nil
      else
        @tail = @tail.previous
        @tail.next = nil
      end

      return value
    end

    # method that returns the value of the last node in the linked list
    # returns nil if the linked list is empty
    # Time Complexity:  O(n) where n is the number of nodes
    # Space Complexity: O(1)
    def get_last
      return nil if @head.nil?
      return @tail.data
    end

    # method to insert a new node with specific data value, assuming the linked
    # list is sorted in ascending order
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def insert_ascending(value)
      new_node = Node.new(value)
      add_first(value) if @head.nil?
      current = @head
      if current.data > new_node.data
        temp = @head
        @head = new_node
        temp.previous = @head
        new_node.next = temp
      end

      until current.nil?
        if current.data <= value && current.next.data > value
          temp = current.next
          current.next = new_node
          new_node.next = temp
          new_node.previous = current
          temp.previous = new_node
          return
        end
        current = current.next
      end
    end

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle
      return if @head == nil # don't do anything if the linked list is empty

      # navigate to last node
      current = @head
      while current.next != nil
          current = current.next
      end

      current.next = @head # make the last node link to first node
    end

    def to_s
      list = []

      current = @head
      until current.nil?
        list << current.data
        current = current.next
      end

      return list.to_s
    end
end
