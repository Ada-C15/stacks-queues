import pytest
from stacks_queues.queue import Queue, QueueFullException

# Fixture to start each test with a new Queue
@pytest.fixture()
def queue() -> Queue:
    return Queue()


def test_it_can_create_a_queue(queue):
    assert isinstance(queue, Queue)


def test_you_can_add_to_queue(queue):
    queue.enqueue(10)
    assert str(queue) == "[10]"

def test_you_can_add_multiple_items(queue):
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert str(queue) == "[10, 20, 30]"

def test_the_queue_starts_empty(queue):
    assert queue.empty

def test_dequeue_can_remove_an_item(queue):
    queue.enqueue(5)
    assert queue.dequeue() == 5
    assert queue.empty()

def test_elements_dequeued_in_fifo_order(queue):
    queue.enqueue(5)
    queue.enqueue(6)
    assert queue.dequeue() == 5
    assert queue.dequeue() == 6
    assert queue.empty()

def test_elements_maintained_in_proper_order(queue):
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(7)
    assert queue.dequeue() == 5
    assert str(queue) == "[3, 7]"
    assert not queue.empty()


def test_with_large_queue(queue):
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20

    for num in [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]:
        queue.enqueue(num)
    
    assert str(queue) == "[30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]"

    with pytest.raises(QueueFullException):
        queue.enqueue('This will break it')