class Queue

  def initialize
    # @store = ...
    raise NotImplementedError, "Not yet implemented"
  end

  def enqueue(element)
    raise NotImplementedError, "Not yet implemented"
  end

  def dequeue
    raise NotImplementedError, "Not yet implemented"
  end

  def front
    raise NotImplementedError, "Not yet implemented"
  end

  def size
    raise NotImplementedError, "Not yet implemented"
  end

  def empty?
    raise NotImplementedError, "Not yet implemented"
  end

  def to_s
    return @store.to_s
  end
end
