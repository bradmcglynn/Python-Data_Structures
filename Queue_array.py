"""
-------------------------------------------------------
Array version of the Queue ADT.
-------------------------------------------------------
Author:  Brad McGlynn
ID:      999999999
Email:   bmcglyn4@uwo.ca
Section: CP164 
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
from copy import deepcopy


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full. (Given the expandable nature
        of the Python list _values, the queue is never full.)
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"
        value = self._values.pop(0)
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"
        value = deepcopy(self._values[0])
        return value

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in queue:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value


    def is_identical(self, target):
        """
        ----------------
        Determines whether two queues are identical.
        Entries of self and target are compared and if all contents are identical
        and in the same order, returns True, otherwise returns False.
        Use: identical = source.is_identical(target)
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False otherwise.
                source and target are unchanged. (boolean)
        ---------------
        """
        identical = True
        if not len(self._values) == 0 and not len(target._values) == 0:
            empty = False
        else:
            empty = True
        temp1=[]
        temp2=[]
        count = 0
        while identical and not empty:
            temp1.append(self._values.pop(0))
            temp2.append(target._values.pop(0))
            if temp1[count]!= temp2[count]:
                identical = False
            if len(self._values) == 0 or len(target._values) == 0:
                empty = True
            count+=1
        if empty:
            if not (len(self._values) == 0 and len(target._values) == 0):
                identical = False
        #time to put them back as they were...
        while not len(self._values) == 0:
            temp1.append(self._values.pop(0))
        while not len(target._values) == 0:
            temp2.append(target._values.pop(0))
        while temp1:
            self._values.append(deepcopy(temp1.pop(0)))
        while temp2:
            target._values.append(deepcopy(temp2.pop(0)))
        return identical
    
    