"""
-------------------------------------------------------
Linked version of the BST ADT.
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


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                node = None
        
            elif node._left is None:
                # node has no left child.
                node = node._right

            elif node._right is None:
                # node has no right child.
                node = node._left

            else:
                # Node has two children
                tempr = node._right
                templ = node._left
                node = self._delete_node_left(node._left)
                node._right = tempr
                node._left = templ

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
        repl_node = None
        if parent._right is not None:
            
            if parent._right._right is not None:
                repl_node = self._delete_node_left(parent._right)
            else:
                if parent._right._left is None:
                    repl_node = parent._right
                else:
                    repl_node = parent._right
                    parent._right = parent._right._left
#         elif parent._left is not None:
#             repl_node = parent
#             pass
        else:
            repl_node = parent
#             parent._right = None
        
        return repl_node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        present = False
        if self._root is not None:
            present = self._contains_aux(self._root, key)
        return present

    def _contains_aux(self, node, key):
        present = False
        if node is not None and key == node._value:
            present = True

        if not present and node._left is not None:
            present = self._contains_aux(node._left, key)
        if not present and node._right is not None:
            present = self._contains_aux(node._right, key)        

        return present

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """
        if self._root is not None:
            height = self._root._height
        else:
            height = 0
        
        return height

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another bst (BST)
        Returns:
            identical - True if this bst contains the same values
            in the same order as other, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        identical = False
        if self._count == other._count:
            identical = True
        
        if identical and self._root is not None and other._root is not None:
            identical = self.is_identical_aux(identical, self._root, other._root) 
        
        return identical

    def is_identical_aux(self, identical, current, other):
        "getting irritating"
        # FIX NONETYPE
        if current._value != other._value or (current._left is None != other._left is None) or (current._right is None != other._right is None):
            identical = False
        if identical:
            if current._left is not None:
                identical = self.is_identical_aux(identical, current._left, other._left)
            if current._right is not None and identical:
                identical = self.is_identical_aux(identical, current._right, other._right)        
        return identical

    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"
        current = self._root
        value = None
        while value is None and current is not None:
            if current._left is not None and current._left._value == key:
                value = deepcopy(current._value)
            elif current._right is not None and current._right._value == key:
                value = deepcopy(current._value)
            
            elif current._left is not None and current._right is not None:
                if key < current._value:
                    current = current._left
                else:
                    current = current._right

            elif current._left is not None:
                current = current._left
            elif current._right is not None:
                current = current._right

            else:
                current = None
        
        return value

    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        value = None

        if self._root is not None:
            value = self.parent_r_aux(self._root, key)
        return value

    def parent_r_aux(self, node, key):
        value = None
        if node is not None:
            if node._left is not None and key == node._left._value:
                value = deepcopy(node._value)
            elif node._right is not None and key == node._right._value:
                value = deepcopy(node._value)
            elif node._left is not None and node._right is not None:
                if key < node._value:
                    value = self.parent_r_aux(node._left, key)
                else:
                    value = self.parent_r_aux(node._right, key)
            elif node._left is not None:
                value = self.parent_r_aux(node._left, key)
            elif not value and node._right is not None:
                value = self.parent_r_aux(node._right, key)

        return value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here

    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        current = self._root
        value = None
        
        while value is None:
            if current._left is not None:
                current = current._left
            else:
                value = deepcopy(current._value)
        
        return value

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here

    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        count = 0
        
        if self._root is not None:
            count = self.leaf_count_aux(count, self._root)
        
        return count

    def leaf_count_aux(self, count, node):
        "Not a lot of fun, and not very efficient"
        
        if node._left is None and node._right is None:
            count += 1
        elif node._left is not None and node._right is not None:
            count = self.leaf_count_aux(count, node._left)
            count = self.leaf_count_aux(count, node._right)
        elif node._left is not None:
            count = self.leaf_count_aux(count, node._left)
        elif node._right is not None:
            count = self.leaf_count_aux(count, node._right)
        
        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        count = 0
        if self._root is not None:
            count = self.two_child_count_aux(count, self._root)
        
        return count

    def two_child_count_aux(self, count, node):
        
        if node._left is not None and node._right is not None:
            count += 1
            count = self.two_child_count_aux(count, node._left)
            count = self.two_child_count_aux(count, node._right)
        elif node._left is not None:
            count = self.two_child_count_aux(count, node._left)
        elif node._right is not None:
            count = self.two_child_count_aux(count, node._right)
        
        return count

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        count = 0
        if self._root is not None:
            count = self.one_child_count_aux(count, self._root)
        
        return count
    
    def one_child_count_aux(self, count, node):
        
        if node._left is not None and node._right is not None:
            count = self.one_child_count_aux(count, node._left)
            count = self.one_child_count_aux(count, node._right)
        elif node._left is not None:
            count += 1
            count = self.one_child_count_aux(count, node._left)
        elif node._right is not None:
            count += 1
            count = self.one_child_count_aux(count, node._right)
        
        return count

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        zero = 0  
        one = 0
        two = 0
        
        if self._root is not None:
            zero, one, two = self.node_counts_aux(zero, one, two, self._root)
        
        return zero, one, two
    
    def node_counts_aux(self, zero, one, two, node):
        
        if node._left is not None and node._right is not None:
            two += 1
            zero, one, two = self.node_counts_aux(zero, one, two, node._left)
            zero, one, two = self.node_counts_aux(zero, one, two, node._right)
        elif node._left is not None:
            one += 1
            zero, one, two = self.node_counts_aux(zero, one, two, node._left)
        elif node._right is not None:
            one += 1
            zero, one, two = self.node_counts_aux(zero, one, two, node._right)
        else:
            zero += 1
        
        return zero, one, two

    def total_depth(self):
        """
        ---------------------------------------------------------
        Returns the total depth of a bst.
        ---------------------------------------------------------
        Returns:
            the total depth count - i.e. the sum of all the node depths
            in the tree (int)
        ---------------------------------------------------------
        """
        total = 0
        
        if self._root is not None:
            self.inorder_aux(total, self._root)
        
        return total

    def total_depth_aux(self, total, node):
        "everything is fine"
        
        if node._left is not None:
            self.inorder_aux(total, node._left)
        total += node._height
        if node._right is not None:
            self.inorder_aux(total, node._right)
                
        return total

    def mirror(self):
        """
        ---------------------------------------------------------
        Creates a mirror version of a BST. All nodes are swapped with nodes on
        the other side the tree. Nodes may take the place of an empty spot.
        The resulting tree is a mirror image of the original tree. (Note that
        the mirrored tree is not a BST.) The original BST is unchanged.
        Use: tree = bst.mirror()
        ---------------------------------------------------------
        Returns:
            tree - a mirror version of subtree of node.
        ---------------------------------------------------------
        """

        # your code here

    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        
        balanced = self.is_balanced_aux(self._root)
        
        return balanced
    
    def is_balanced_aux(self, node):
        "Can we do it??! Maybe!"
        balanced = False
        if node is None:
            balanced = True
        
        else:
            # find the height of the nodes
            if node._left is not None:
                l_height = node._left._height
            else:
                l_height = 1
            if node._right is not None:
                r_height = node._right._height
            else:
                r_height = 1
            
            # check balance
            if l_height - r_height > -2 and l_height - r_height < 2:
                balanced = True
            
            # check child nodes for balance
            if balanced:
                balanced = self.is_balanced_aux(node._left)
            if balanced:
                balanced = self.is_balanced_aux(node._right)
        
        return balanced

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """

        # your code here

    def average_depth(self):
        """
        ---------------------------------------------------------
        Returns the average depth of a bst.
        ---------------------------------------------------------
        Returns:
            avg-depth - total depth count divided by the number of nodes
                in the tree (int)
        ---------------------------------------------------------
        """

        # your code here

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        a = []
        if self._root is None:
            valid = True
        else:
            valid = self._is_valid_aux(self._root)
            if valid:
                a = self.is_valid_inorder_aux(a, self._root)
                i = 0
                len_a = len(a)
                while valid and i + 1 < len_a:
                    if not a[i] < a[i + 1]:
                        valid = False
                    i += 1
        
        return valid

    def is_valid_inorder_aux(self, a, node):
        "everything is fine"
        
        if node._left is not None:
            self.inorder_aux(a, node._left)
        a.append(deepcopy(node._value))
        if node._right is not None:
            self.inorder_aux(a, node._right)
                
        return a

    def _is_valid_aux(self, node):
        "Determination, makes it happen"
        
        if node is None:
            valid = True
        else:
            # does node left or right have a larger height?
            if self._node_height(node._left) >= self._node_height(node._right):
                if self._node_height(node) != self._node_height(node._left) + 1:
                    valid = False
                else:
                    valid = True
            else:
                if self._node_height(node) != self._node_height(node._right) + 1:
                    valid = False
                else:
                    valid = True
            if valid and node._left is not None and node._right is not None and node._left._value < node._right._value:
                valid = self._is_valid_aux(node._left)
                if valid:
                    valid = self._is_valid_aux(node._right)
            elif valid and node._left is None and node._right is None:
                valid = True
            elif valid and node._left is not None:
                valid = self._is_valid_aux(node._left)
            elif valid and node._right is not None:
                valid = self._is_valid_aux(node._right)
            else:
                valid = False
        
        return valid
    
    def update(self, value, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Iterative algorithm.)
        --------------------------------------------------------- -
        """

        # your code here

    def update_r(self, key, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Recursive algorithm.)
        --------------------------------------------------------- -
        """

        # your code here

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        
        if self._root is not None:
            self.inorder_aux(a, self._root)
        
        return a

    def inorder_aux(self, a, node):
        "everything is fine"
        
        if node._left is not None:
            self.inorder_aux(a, node._left)
        a.append(deepcopy(node._value))
        if node._right is not None:
            self.inorder_aux(a, node._right)
                
        return a

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        if self._root is not None:
            self.preorder_aux(a, self._root)
        return a

    def preorder_aux(self, a, node):
        "Things seem alright"
        
        a.append(deepcopy(node._value))
        if node._left is not None:
            self.preorder_aux(a, node._left)
        if node._right is not None:
            self.preorder_aux(a, node._right)
                
        return a

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        
        if self._root is not None:
            self.postorder_aux(a, self._root)
        
        return a

    def postorder_aux(self, a, node):
        "Things are chipper, for now"

        if node._left is not None:
            self.postorder_aux(a, node._left)
        if node._right is not None:
            self.postorder_aux(a, node._right)
        a.append(deepcopy(node._value))
                
        return a

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        values = []
        
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                values.append(deepcopy(node._value))

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
            
        return values

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """
        return self._count

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
