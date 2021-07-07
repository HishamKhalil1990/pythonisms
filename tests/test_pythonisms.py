from pythonisms import *
import pytest

def test_for_loop(linked1):
    expected = [1,2,3,4,5,6]
    actual = []
    for num in linked1:
        actual.append(num)
    assert actual == expected

def test_list_comprehension(linked1):
    expected = [1,2,3,4,5,6]
    actual = [node for node in linked1]
    assert actual == expected

def test_convert_to_list(linked1):
    expected = [1,2,3,4,5,6]
    actual = list(linked1)
    assert actual == expected

def test_convert_returned():
    expected = "the returned value was 17"
    @convert_returned
    def add(x,y):
        return x+y
    actual = add(11,6)
    assert actual == expected

def test_validate_condition_true():
    expexted = "your name is hisham, and your age is 31"
    @validate_coditions
    def user(name,age):
        return(f"your name is {name}, and your age is {age}")
    actual = user("hisham",31)
    assert actual == expexted

def test_validate_condition_false():
    expexted = "passed arguments don't match"
    @validate_coditions
    def user(name,age):
        return(f"your name is {name}, and your age is {age}")
    actual = user("hisham","31")
    assert actual == expexted

def test_add_equality_true(linked2):
    linked_list1,linked_list2 = linked2
    assert linked_list1 == linked_list2

def test_add_equality_false(linked3):
    linked_list1,linked_list2 = linked3
    assert (linked_list1 == linked_list2)

def test_add_truthy():
    ll = Linked_List()
    ll.append(1)
    assert ll

@pytest.fixture
def linked1():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    return ll

@pytest.fixture
def linked2():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll2 = Linked_List()
    ll2.append(1)
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)
    ll2.append(5)
    ll2.append(6)
    return ll,ll2

@pytest.fixture
def linked3():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll2 = Linked_List()
    ll2.append(1)
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)
    ll.append(5)
    ll.append(7)
    return ll,ll2