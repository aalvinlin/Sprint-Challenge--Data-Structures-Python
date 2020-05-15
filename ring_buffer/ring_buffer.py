class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)

class CircularLinkedList:
    def __init__(self, length):

        self.newest = Node()
        self.oldest = self.newest

        # initialize all nodes to empty
        for i in range(length - 1):
            self.newest.next = Node()
            self.newest = self.newest.next

        # link newest node and oldest node together
        self.newest.next = self.oldest

    def __str__(self):

        current_node = self.oldest

        string_representation = str(current_node.value)

        while current_node.next is not self.oldest:

            current_node = current_node.next

            # do not display empty nodes
            if current_node.value:
                string_representation += " -> " + str(current_node.value)

        return string_representation

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        
        self.buffer = CircularLinkedList(5)
        self.newest = self.buffer
        
        self.oldest = None

    def append(self, item):
        pass

    def get(self):
        pass

ring = CircularLinkedList(5)
print(ring)

