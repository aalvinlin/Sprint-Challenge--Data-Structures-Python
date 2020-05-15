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

        # even though rings don't have a start, maintain a start pointer for a consistent printing format
        self.print_start = newest

        # initialize all nodes to empty
        for i in range(length - 1):
            newest.next = Node()
            newest = newest.next

        # link newest node and oldest node together
        newest.next = self.entry

    def __str__(self):

        current_node = self.print_start

        string_representation = str(current_node.value)

        while current_node.next is not self.print_start:

            current_node = current_node.next

            # do not display empty nodes
            if current_node.value:
                string_representation += " -> " + str(current_node.value)

        # repeat the starting node to show circularity
        string_representation += " -> " + str(self.print_start)

        return string_representation

    def get_array_representation(self):

        current_node = self.print_start

        array_representation = []

        # add first element if it is not None
        if current_node.value:
            array_representation.append(current_node.value)

        while current_node.next is not self.print_start:

            current_node = current_node.next

            # do not display empty nodes
            if current_node.value:

                array_representation.append(current_node.value)

        return array_representation

class RingBufferAsCircularLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity        
        self.storage = CircularLinkedList(5)

    def __str__(self):
        return str(self.storage)
        
    def append(self, item):
        # store item in next available spot
        self.storage.entry.value = item

        # update pointer for next available spot
        self.storage.entry = self.storage.entry.next

    def get(self):
        return self.storage.get_array_representation()

class RingBuffer(RingBufferAsCircularLinkedList):
    def __init__(self, capacity):
        super().__init__(capacity)

# ring = RingBuffer(5)
# ring.append('a')
# ring.append('b')
# ring.append('c')
# ring.append('d')
# ring.append('e')
# ring.append('f')
# print(ring.get())

# ring.append('g')
# print(ring.get())

# ring.append('h')
# print(ring.get())

# ring.append('i')
# print(ring.get())

# ring.append('j')
# print(ring.get())

# ring.append('k')
# print(ring.get())

# ring.append('l')
# print(ring.get())


