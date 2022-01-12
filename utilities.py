"""
-------------------------------------------------------
data_structures utilities
-------------------------------------------------------
Author:  Brad McGlynn
ID:      999999999
Email:   bmcglyn4@uwo.ca
Section: CP164 
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
# Imports
# from Stack_array import Stack
#from Queue_array import Queue
#from Queue_circular import Queue
#from Priority_Queue_array import Priority_Queue
from List_array import List
#from List_linked import List
#from Movie import Movie
# Constants


# Functions

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        stack.push(source.pop())
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    if source:
        stack = Stack()
        if stack.is_empty():
            print("Stack exists and is empty, which means .is_empty worked.")
        while source:
            stack.push(source.pop())
            print(stack.peek(), "is the top of the stack, which means .push and .peek have worked.")
        if not stack.is_empty():
            print("Stack exists and is not empty, which means .is_empty was effective at that as well.")
        while not stack.is_empty():
            print(stack.peek(), "is the top of the stack, which means .peek has worked.")
            source.append(stack.pop())
            
            print(source[-1], "is the next value to be popped and then appended to the stack. If this value has changed, then .pop has worked.")
        
    else:
        print("Source has no data")
    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        queue.insert(source.pop(0))
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        pq.insert(source.pop(0))    
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return
    
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    if q.is_empty():
        print("Queue exists and is empty, which means is_empty can tell when the queue is empty.")
    if len(q)==0:
        print("len correctly identified that len of an existing but empty queue object is 0.")
    print("\nAbout to begin popping from given list.")
    while a:
        print("About to pop a[0]:", a[0], "and put it into the queue")
        q.insert(a.pop(0))
    print("The length of the queue is", len(q), "which means that len works with queues that are not empty.")
    print("\nInsert and peek worked if", q.peek(), "is the value that was first popped from a.")
    if not q.is_empty():
        print("If you can see this, the queue is not empty, AND .is_empty could tell!")
    print("\nAbout to start removing from the queue.")
    while not q.is_empty():
        print("About to remove", q.peek(), "from the queue.")
        print("We just removed", q.remove(), "from the queue but we didn't put it anywhere. Oops!")
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    if pq.is_empty():
        print("Queue exists and is empty, which means is_empty can tell when the queue is empty.")
    print("\nAbout to begin popping from given list.")
    while a:
        print("About to pop a[0]:", a[0], "and put it into the queue")
        pq.insert(a.pop(0))
    
    print("\nInsert and peek worked if", pq.peek(), "is the value that was first popped from a.")
    if not pq.is_empty():
        print("If you can see this, the queue is not empty, AND .is_empty could tell!")
    print("\nAbout to start removing from the queue.")
    while not pq.is_empty():
        print("About to remove", pq.peek(), "from the queue.")
        print("We just removed", pq.remove(), "from the queue but we didn't put it anywhere. Oops!")

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source)>0:
        llist.append(source.pop(0))
    return
    

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
#         print("Because list is not empty(expect True)", not llist.is_empty())
#         print("popping", llist.peek())
        target.append(llist.pop(0))    
    return

def array_to_sorted_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (Sorted_List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source)>0:
        llist.insert(source.pop(0))
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    print("List is empty - Expects True:", lst.is_empty())
    print("Source Data is", source)
    print("Moving source data into List object using array to list.")
    array_to_list(lst, source)
    lst.append(lst.pop())
    print("List is empty - Expects False:", lst.is_empty())
    for el in lst:
        print("{}".format(el), end=" ")
    print("")
    print("This shows that append works.")
    print("Will use data at position 0 as key. Peeking:", lst.peek())
    if isinstance(lst._values[0], Movie):
        print("We have a class on our hands! Removing non-essential key data.")
        key = lst.peek()
        key.director = None
        key.rating = None
        key.genres = None
    else:
        key = lst.peek()
    print("The location of", key, "is at index:", lst.index(key))
    print("The full data of", key, "(using .find) is:", lst.find(key))
    print("The largest value in the list is", lst.max(), "while the smallest is", lst.min())
    print("The number of times", key, "appears in list is", lst.count(key))
    big_i = lst.index(lst.max())
    print("Will insert key:", key, "at position:", big_i)
    lst.insert(big_i, key)
    print("The item at location", big_i, "is", lst._values[big_i])
    small_i = lst.index(lst.min())
    print("Will now remove the smallest value:", lst.min(), "at position", small_i)
    lst.remove(lst.min())
    print("The item at", small_i, "was removed and the following moved into its place:", lst._values[small_i])
    
    
    
    

    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    return


