"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  Brad McGlynn
ID:      999999999
Email:   bmcglyn4@uwo.ca
Section: CP164 
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            self._front = _Deque_Node(value, None, None)
            self._rear = self._front
            
        else:
            self._front._prev = _Deque_Node(value, None, self._front)
            self._front = self._front._prev
            
        self._count += 1
        
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            self._front = _Deque_Node(value, None, None)
            self._rear = self._front
            
        else:
            self._rear._next = _Deque_Node(value, self._rear, None)
            self._rear = self._rear._next
        
        self._count += 1
        
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"
        
        value = self._front._value
        
        if self._front._next is None:
            self._front = None
            self._rear = None
        
        else:
            self._front._next._prev = None
            self._front = self._front._next
            
        self._count -= 1
        
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"
        
        value = self._rear._value
        
        if self._rear._prev is None:
            self._front = None
            self._rear = None
        
        else:
            self._rear._prev._next = None
            self._rear = self._rear._prev
            
        self._count -= 1
        
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"
        value = deepcopy(self._front._value)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"
        value = deepcopy(self._rear._value)
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r,
        r has taken the place of l and _front and _rear are updated
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        if l is not r:
            # Swap the parameter node pointers
            l._prev, r._prev, l._next, r._next = r._prev, l._prev, r._next, l._next

            # If nodes are adjacent, previous swaps make nodes point to
            # themselves
            if l._prev is l:
                l._prev = r
            elif l._next is l:
                l._next = r

            if r._prev is r:
                r._prev = l
            elif r._next is r:
                r._next = l

            # Update linked nodes
            # See if front and/or rear have changed
            if l._prev is None:
                # l is the front
                self._front = l
            else:
                l._prev._next = l

            if l._next is None:
                # l is the rear
                self._rear = l
            else:
                l._next._prev = l

            if r._prev is None:
                # r is the front
                self._front = r
            else:
                r._prev._next = r

            if r._next is None:
                # r is the rear
                self._rear = r
            else:
                r._next._prev = r
        return

#     def _swap(self, l, r):
#         """
#         -------------------------------------------------------
#         Swaps two nodes within a deque. l has taken the place of r, 
#         r has taken the place of l and _front and _rear are updated 
#         as appropriate. Data is not moved.
#         Use: self._swap(self, l, r):
#         -------------------------------------------------------
#         Parameters:
#             l - a pointer to a deque node (_Deque_Node)
#             r - a pointer to a deque node (_Deque_Node)
#         Returns:
#             None
#         -------------------------------------------------------
#         """
#         assert l is not None and r is not None, "nodes to swap cannot be None"
#         
#         # Don't do anything with a list smaller than 2, dummy
#         if self._count > 1:
#             
#             # If l is the front of the list
#             if l._prev == None:
#                 
#                 # If right is at the end
#                 if r._next == None:
#                     self._front = r
#                     r._next = l._next
#                     r._prev._next = l
#                     l._next = None
#                     
#                     self._rear = l
#                     l._prev = r._prev
#                     r._next._prev = r
#                     r._prev = None
#             
#                 # If right is somewhere in the middle
#                 else:
#                     # if right is next of left
#                     if l._next == r:
#                         r._next._prev = l
#                         self._front = r
#                         
#                         r._prev = l._prev
#                         l._next = r._next
#                         r._next = l
#                         l._prev = r  
#                     else:
#                         self._front = r
#                         temp = r._next
#                         r._next = l._next
#                         r._prev._next = l
#                         l._next = temp
#                         
#                         l._prev = r._prev
#                         l._prev._next = l
#                         l._next._prev = l 
#                         r._prev = None
#             
#             # If l is at the end of the list
#             elif l._next == None:
#                 
#                 # If r is at the front
#                 if r._prev == None:
#                     self._rear = r
#                     r._prev = l._prev
#                     l._next._prev = l
#                     l._prev = None
#                     
#                     self._front = l
#                     l._next = r._next
#                     l._prev._next = r
#                     r._next = None
#                 
#                 # If r in middle
#                 else:
#                     temp = r._next
#                     r._next = None
#                     l._next = temp
#                     
#                     self._rear = r
#                     temp = r._prev
#                     r._prev = l._prev
#                     l._next._prev = l
#                     l._prev = temp
#                     r._prev._next = r 
#                     l._prev._next = l
#              
#             # If r is at the front of the list
#             elif r._prev == None:
# 
#                 # If l is somewhere in the middle
#                 if l._next != None:
#                     self._front = l
#                     temp = l._next
#                     l._next = r._next
#                     l._prev._next = r
#                     r._next = temp
#                     
#                     r._prev = l._prev
#                     r._prev._next = r
#                     r._next._prev = r
#                     l._prev = None
#             
#             else:
#                 if l._next == r or r._next == l:
# 
#                     if r._next == l:
#                     
#                         l._next._prev = r
#                         r._prev._next = l
#                         
#                         l._prev = r._prev
#                         r._next = l._next
#                         l._next = r
#                         r._prev = l  
# 
#                     else:
#                         r._next._prev = l
#                         l._prev._next = r
#                         
#                         r._prev = l._prev
#                         l._next = r._next
#                         r._next = l
#                         l._prev = r  
#                         
#                 else:
#                     temp = r._next
#                     r._next = l._next
#                     l._next = temp
#                     
#                     temp = r._prev
#                     l._prev = r._prev
#                     r._prev = temp
#                     
#                     r._next._prev = r
#                     l._next._prev = l
#                     l._prev._next = l
#                     r._prev._next = r
#         return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
