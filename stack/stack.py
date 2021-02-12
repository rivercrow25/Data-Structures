"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import Node, LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.appen(value)
#         self.size += 1
#         return self.size

#     def pop(self):
#         x = None
#         if self.size > 0:
#             self.size -= 1
#             x = self.storage.pop(self.size)
#             return x
#         return x


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        return self.size

    def pop(self):
        x = None
        if self.size > 0:
            x = self.storage.remove_tail()
            self.size -= 1
            return x
        return x
