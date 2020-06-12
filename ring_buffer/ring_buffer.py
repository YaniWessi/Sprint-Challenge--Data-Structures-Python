
# class Node:
#     def __init__(self, value=None):
#          # the value at this Linked list node
#         self.value = value


#     def get_value(self):
#         return self.value

# class Buffer:
#     def __init__(self):
#         # refrence to the head of the list
#         self.head = None
#         # refrence to the tail of the list
#         self.tail = None


#     def add_to_tail(self, value)

#          new_node = Node(value, None)

#          if not self.head:

#              self.head = new_node
#              self.tail = new_node

#          else:

#              self.tail.set_next(new_node)

#              self.tail = new_node

class Buffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = []

    def append(self, item):
        self.current += 1
        self.storage[self.current] = item

        if self.current == self.capacity:
            self.current

    def get(self):
        return self.storage
