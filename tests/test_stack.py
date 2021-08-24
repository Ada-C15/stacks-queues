import pytest
from stacks_queues.stack import Stack, StackEmptyException


# Fixture to start each test with a new Stack
@pytest.fixture()
def stack() -> Stack:
    return Stack()

def test_stack_can_be_instantiated(stack):
    assert isinstance(stack, Stack)

def test_can_push_onto_empty_stack_and_pop(stack):
    stack.push(10)
    assert stack.pop() == 10

def test_multiple_items_pushed_onto_stack(stack):
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10

def test_new_stacks_are_empty(stack):
    assert stack.empty()

def test_stack_is_empty_after_all_elements_popped(stack):
    stack.push(5)
    stack.push(15)
    assert stack.pop() == 15
    assert stack.pop() == 5
    assert stack.empty()

def test_items_removed_in_lifo_order(stack):
    stack.push(5)
    stack.push(3)
    stack.push(7)

    assert stack.pop() == 7
    assert stack.pop() == 3
    assert stack.pop() == 5
    assert stack.empty()
