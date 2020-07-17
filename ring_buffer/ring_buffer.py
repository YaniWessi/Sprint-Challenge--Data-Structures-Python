
# class Node:
#     def __init__(self, value=None):
#          # the value at this Linked list node
#         self.value = value
# just a comment to push

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

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = []

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        else:
            # [a, b, c, d] new item is e
            # self.storage[0] = e
            # item is e and is going to replace a. a is at index 0 and is the oldest so we need to replace that with e thenewest
            self.storage[self.current] = item
            self.current += 1

            if self.current == self.capacity:
                self.current = 0

    def get(self):
        return self.storage
