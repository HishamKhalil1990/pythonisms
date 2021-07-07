import time

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
   
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __eq__(self,other):
        """
        return True or False if the node from list2 is equal node from list1 
        because i don't know which node from list 1 i will try to do it for all list 
        """
        current1=self.head 
        current2=other.head 
        flag = True

        while  current1 and current2 :
            if not(current1.value  == current2.value):
                flag = False
                break  
            current1 = current1.next
            current2 = current2.next
        return flag

    def __bool__(self):
        if self.head:
            return True
        return False

def calculate_time(func): 
    def wrapper(*args,**kwargs):
        starting_time = time.time()
        result = func(*args,**kwargs)
        ending_time = time.time()
        print (ending_time-starting_time)
        return result
    return wrapper

@calculate_time
def check_equality(linked_list1,linked_list2):
    return linked_list1 == linked_list2

def debug_code(func):
    def wrapper(*args, **kwargs):
        x = args
        y = kwargs
        print(f'inputs are : {x}, {y}')
        output = func(*args, **kwargs)
        print(f'output is : {output}')
        return output
    return wrapper

@debug_code
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def slow_down(func):
    def wrapper(*args,**kwargs):
        time.sleep(1)
        output = func(*args,**kwargs)
        return output
    return wrapper

@slow_down
def counter_down(n):
    print(n)
    if n != 0:
        counter_down(n-1) 

def convert_returned(func):
    def wrapper(*args,**kwargs):
        output = func(*args,**kwargs)
        return f"the returned value was {output}"
    return wrapper

@convert_returned
def add(x,y):
    return x+y

def validate_coditions(func):
    def wrapper(*args,**kwargs):
        conditions = [
        type(args[0]) == str,
        type(args[1]) == int
        ]
        if all(conditions):
            output = func(*args,**kwargs)
            return output
        else:
            return "passed arguments don't match"
    return wrapper

@validate_coditions
def user(name,age):
    print(f"your name is {name}, and your age is {age}")

if __name__ == "__main__":
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    for node in ll:
        print(node)
    print([node for node in ll])
    print(tuple(ll))
    ll2 = Linked_List()
    ll2.append(1)
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)
    ll2.append(5)
    ll2.append(7)
    ll3 = Linked_List()
    print(ll == ll2)
    assert ll
    assert not ll3
    check_equality(ll,ll2)
    factorial(6)
    counter_down(5)
    print(add(11,6))
    user("hisham",31)
    print(user("hisham","31"))