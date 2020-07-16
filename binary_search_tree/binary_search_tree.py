"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        x = None
        if self.size > 0:
            self.size -= 1
            x = self.storage.pop(0)
            return x
        return x


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(node)

        print(self.value)

        if self.right is not None:
            self.right.in_order_print(node)

        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, node):
        # pass
        que = Queue()
        que.enqueue(self)
        while que.size > 0:
            node = que.dequeue()
            print(node.value)

            if node.left is not None:
                que.enqueue(node.left)
            if node.right is not None:
                que.enqueue(node.right)

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()
        stack.push(self)

        while stack.size > 0:
            node = stack.pop()
            print(node.value)

            if node.left is not None:
                stack.push(node.left)

            if node.right is not None:
                stack.push(node.right)
        # Stretch Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft(node)
        if self.right is not None:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if self.left is not None:
            self.left.pre_order_dft(node)
        if self.right is not None:
            self.right.pre_order_dft(node)
        print(self.value)


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        return self.size

    def pop(self):
        x = None
        if self.size > 0:
            self.size -= 1
            x = self.storage.pop(self.size)
            return x
        return x
