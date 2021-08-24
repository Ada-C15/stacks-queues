import pytest
from stacks_queues.linked_list import LinkedList

# This is used by the instructor to verify the LinkedList class works.
# Students's can ignore this file.

# Fixture to start each test with a new LinkedList
@pytest.fixture()
def list() -> LinkedList:
    return LinkedList()


def test_list_can_be_initialized(list):
    assert isinstance(list, LinkedList)

def test_get_first_returns_none_for_empty_list(list):
    assert list.get_first() == None

def test_add_first_adds_to_start_of_list(list):
    list.add_first(3)
    assert list.get_first() == 3

    list.add_first(4)
    assert list.get_first() == 4

    list.add_first('pasta')
    assert list.get_first() == 'pasta'


def test_search_returns_false_for_empty_list(list):
    assert list.search(3) == False


def test_search_returns_false_for_items_not_in_list(list):
    list.add_first(3)
    list.add_first(4)
    assert list.search(5) == False

def test_search_returns_true_for_items_in_front_of_list(list):
    list.add_first(3)
    list.add_first(4)
    assert list.search(4) == True


def test_search_returns_true_for_items_in_back_of_list(list):
    list.add_first('pasta')
    list.add_first(3)
    list.add_first(4)
    assert list.search('pasta') == True


def test_search_returns_true_for_items_in_middle_of_list(list):
    list.add_first(3)
    list.add_first(4)
    list.add_first(5)
    list.add_first(6)
    assert list.search(5) == True

def test_length_returns_0_for_empty_list(list):
    assert list.length() == 0

def test_length_returns_1_for_list_with_1_element(list):
    list.add_first(3)
    assert list.length() == 1

def test_length_returns_2_for_list_with_2_elements(list):
    list.add_first(3)
    list.add_first(4)
    assert list.length() == 2

def test_length_increases_in_value_with_each_add_first(list):
    count = 0

    while count < 5:
        list.add_first(count)
        count += 1
        assert list.length() == count

def test_get_at_index_with_empty_list_is_none(list):
    assert list.get_at_index(3) == None

def test_get_at_index(list):

    list.add_first(1)
    list.add_first(2)
    list.add_first(3)
    list.add_first(4)

    assert list.get_at_index(0) == 4
    assert list.get_at_index(1) == 3
    assert list.get_at_index(2) == 2
    assert list.get_at_index(3) == 1

def test_get_last_on_empty_list_returns_none(list):
    assert list.get_last() == None

def test_get_last_returns_the_last_element_of_a_list(list):
    list.add_first(5)
    assert list.get_last() == 5

    list.add_first(4)
    assert list.get_last() == 5

def test_add_last_on_empty_list(list):
    list.add_last(1)
    assert list.get_at_index(0) == 1

def test_add_last_increases_length_and_new_item_appears_at_back_of_list(list):
    assert list.length() == 0

    list.add_last(5)
    assert list.length() == 1
    assert list.get_last() == 5
    assert list.get_first() == 5

    list.add_last(4)
    assert list.length() == 2
    assert list.get_last() == 4

    list.add_last(3)
    assert list.length() == 3
    assert list.get_last() == 3

    list.add_last(2)
    assert list.length() == 4
    assert list.get_last() == 2

    list.add_last(1)
    assert list.length() == 5
    assert list.get_last() == 1
    assert list.get_first() == 5


def test_find_max_on_empty_list_should_return_none(list):
    assert list.find_max() == None

def test_find_max_on_list_where_max_is_first_item(list):
    list.add_first(1)
    list.add_first(2)
    list.add_first(3)
    list.add_first(4)
    list.add_first(5)

    assert list.find_max() == 5

def test_find_max_on_list_where_max_is_last_item(list):
    list.add_first(27)
    list.add_first(4)
    list.add_first(3)
    list.add_first(2)
    list.add_first(1)

    assert list.find_max() == 27

def test_find_max_on_list_where_max_is_middle_item(list):
    list.add_first(1)
    list.add_first(2)
    list.add_first(27)
    list.add_first(4)
    list.add_first(5)

    assert list.find_max() == 27

def test_delete_on_empty_list_returns_none(list):
    assert list.delete(2) == None

def test_delete_can_remove_first_element_of_list(list):
    list.add_first(5)
    list.add_first(4)
    list.add_first(3)
    list.delete(3)
    assert list.get_first() == 4
    assert list.length() == 2
    assert list.get_last() == 5

def test_delete_can_remove_last_element_of_list(list):
    list.add_first(5)
    list.add_first(4)
    list.add_first(3)
    list.delete(5)
    assert list.get_first() == 3
    assert list.length() == 2
    assert list.get_last() == 4

def test_delete_can_remove_middle_element_of_list(list):
    list.add_first(5)
    list.add_first(4)
    list.add_first(3)
    list.delete(4)
    assert list.get_first() == 3
    assert list.length() == 2
    assert list.get_last() == 5
