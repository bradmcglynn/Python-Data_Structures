"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
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


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_SL_Node)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        if self._front is None:
            self._front = _SL_Node(value, None)
            self._rear = self._front
        
        else:
            current = self._front
            previous = None
            
            while current is not None and current._value <= value:
                previous = current
                current = current._next
                
            if current is None:
                previous._next = _SL_Node(value, None)
                self._rear = previous._next
            elif previous is None:
                self._front = _SL_Node(value, current)
            else:
                previous._next = _SL_Node(value, current)
            
        self._count += 1
        return

    def _remove(self, previous, current):
        """I MADE A HELPER METHOD
        Alright, so give this method previous node and current node
        The method will take current node out back and previous won't
        even know what happened to it. Ain't no good Samaritan here
        """
        if previous is None:
            self._front = current._next
            self._count -= 1
            if self._front is None:
                self._rear = None
        elif current is not None:
            previous._next = current._next
            self._count -= 1
            if previous._next is None:
                self._rear = previous
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        found = False
        index = -1
        if current is not None:
            index = 0
            while current is not None and current._value != key:
                previous = current
                current = current._next
                index += 1
            if current is not None and current._value == key:
                found = True
            if found == False:
                index = -1
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        p, c, _ = self._linear_search(key)
        if c is not None:
            value = c._value
            self._remove(p, c)
        else:
            value = None
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        value = self._front._value
        self._front = self._front._next
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """

        # your code here

        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, c, _ = self._linear_search(key)
        if c is None:
            value = None
        else:
            value = deepcopy(c._value)
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n
    
    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        if i < 0:
            i = self._count + i
        current = self._front
        while i != 0:
            current = current._next
            i -= 1
        value = deepcopy(current._value)
        return value
    
    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)
        return index != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        return deepcopy(self._rear._value)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"
        return deepcopy(self._front._value)

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        current = self._front
        number = 0
        while current is not None and current._value <= key:
            if current._value == key:
                number += 1
            current = current._next
        return number

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        c = self._front
        while c is not None:
            point = c._next
            prev = c
            while point is not None and point._value == c._value:
                self._remove(prev, point)
                point = prev._next
            c = c._next
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:
            i = args[0]

            if i < 0:
                # index is negative
                i = self._count + i
            j = 0

            while j < i:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front
        source2_node = source2._front
        
        while source1_node is not None:
            
            # move s2 node to a value equal to or greater than s1
            while source2_node is not None and source2_node._value < source1_node._value:
                source2_node = source2_node._next
#             _, current, _ = source2._linear_search(value)

            if source2_node is not None and source2_node._value == source1_node._value:
                # Value exists in both source lists.
                if self._front is None:
                    self._front = _SL_Node(deepcopy(source1_node._value), None)
                    self._count += 1
                    current_self = self._front
                else:
                    current_self._next = _SL_Node(deepcopy(source1_node._value), None)
                    self._count += 1
                    current_self = current_self._next
            
            # Increment 1
            if source1_node is not None:
                source1_node = source1_node._next
            # Continue to move to next non-duplicate entry
#             while source1_node is not None and source1_node._value <= current_self._value:
#                 source1_node = source1_node._next
            
        if self._front is not None:
            self._rear = current_self
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front
        source2_node = source2._front
        
        # All of these ifs are to set current_self. I might be an idiot
        if source1_node is not None and source2_node is not None:
            if source1_node._value <= source2_node._value:
                self._front = _SL_Node(deepcopy(source1_node._value), None)
                self._count += 1
                current_self = self._front    
                # look at next value
                source1_node = source1_node._next
                # if value is the same, keep going
                while source1_node is not None and source1_node._value == current_self._value:
                    source1_node = source1_node._next
            else:
                self._front = _SL_Node(deepcopy(source2_node._value), None)
                self._count += 1
                current_self = self._front        
                # look at next value
                source1_node = source2_node._next
                # if value is the same, keep going
                while source2_node is not None and source2_node._value == current_self._value:
                    source2_node = source2_node._next                        

        elif source1_node is not None:
            self._front = _SL_Node(deepcopy(source1_node._value), None)
            self._count += 1
            current_self = self._front    
            # look at next value
            source1_node = source1_node._next
            # if value is the same, keep going
            while source1_node is not None and source1_node._value == current_self._value:
                source1_node = source1_node._next
        
        elif source2_node is not None:
            self._front = _SL_Node(deepcopy(source2_node._value), None)
            self._count += 1
            current_self = self._front    
            # look at next value
            source2_node = source2_node._next
            # if value is the same, keep going
            while source2_node is not None and source2_node._value == current_self._value:
                source2_node = source2_node._next
        
        while source1_node is not None and source2_node is not None:
            
            if source1_node._value <= source2_node._value and source1_node._value != current_self._value:
                # add a node to self
                if self._front is None:
                    self._front = _SL_Node(deepcopy(source1_node._value), None)
                    self._count += 1
                    current_self = self._front
                else:
                    current_self._next = _SL_Node(deepcopy(source1_node._value), None)
                    self._count += 1
                    current_self = current_self._next
                # look at next value
                source1_node = source1_node._next
                # if value is the same, keep going
                while source1_node is not None and source1_node._value == current_self._value:
                    source1_node = source1_node._next
            
            elif source1_node._value > source2_node._value and source2_node._value != current_self._value:
                # add a node to self
                if self._front is None:
                    self._front = _SL_Node(deepcopy(source2_node._value), None)
                    self._count += 1
                    current_self = self._front
                else:
                    current_self._next = _SL_Node(deepcopy(source2_node._value), None)
                    self._count += 1
                    current_self = current_self._next
                # look at next value
                source1_node = source2_node._next
                # if value is the same, keep going
                while source2_node is not None and source2_node._value == current_self._value:
                    source2_node = source2_node._next
            
            # both values are already present in self, increment both
            else:
                source1_node = source1_node._next
                source2_node = source2_node._next
        
        while source1_node is not None:
            
            if source1_node._value != current_self._value:
                # add a node to self
                if self._front is None:
                    self._front = _SL_Node(deepcopy(source1_node._value), None)
                    self._count += 1
                    current_self = self._front
                else:
                    current_self._next = _SL_Node(deepcopy(source1_node._value), None)
                    self._count += 1
                    current_self = current_self._next
            
            # look at next value
            source1_node = source1_node._next

        while source2_node is not None:
            
            if source2_node._value != current_self._value:
                # add a node to self
                if self._front is None:
                    self._front = _SL_Node(deepcopy(source2_node._value), None)
                    self._count += 1
                    current_self = self._front
                else:
                    current_self._next = _SL_Node(deepcopy(source2_node._value), None)
                    self._count += 1
                    current_self = current_self._next
            
            # look at next value
            source2_node = source2_node._next

        return 
    
    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """

        # your code here

        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (iterative version)
        Use: b = l.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            target_node = other._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """
        return deepcopy(self)

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
#         one_t = True
#          
#         while source1._count > 0 and source2._count > 0:
#          
#             if one_t:
#                 self.insert(source1)
#                 one_t = not one_t
#             else:
#                 self._move_front_to_rear(source2)
#                 one_t = not one_t
#          
#         while source1._count > 0:
#             self._move_front_to_rear(source1)
#          
#         while source2._count > 0:
#             self._move_front_to_rear(source2)
#          
        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        # your code here

        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        # your code here

        return

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        # your code here

        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """

        # your code here

        return

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front
        while current is not None:
            yield current._value
            current = current._next
