class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)

class CircularLinkedList:
    def __init__(self, length):

        # temporarily keep track of new nodes
        newest = Node()
        
        # store a pointer to access one of the nodes in the linked list
        self.entry = newest

        # initialize all nodes to empty
        for i in range(length - 1):
            newest.next = Node()
            newest = newest.next

        # link newest node and oldest node together
        newest.next = self.entry

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
        self.storage = CircularLinkedList(5)
        
        self.oldestItemToRemove = None
        self.nextAvailableSpot = self.storage.entry

        # create a dictionary to store pointers to nodes
        self.lookup = dict()

        # current_node = self.storage.entry

        # for i in range(capacity):
        #     current_node = current_node.next
        #     self.newest = self.newest.next

    def append(self, item):
        if self.oldestItemToRemove:
            pass
        else:
            self.lookup[]

    def get(self):
        pass

ring = CircularLinkedList(5)
print(ring)

