class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list_iterative(self, node, prev):

        # look at elements two at a time
        while node.next:
            
            # store a pointer to the current next node
            second = node.next

            # reasssign current node's "next" pointer to the next element after this pair (third element)
            self.set_next(node, second.next)

            # reassign the second node's "next" pointer to point to the current element
            self.set_next(second, node)

            # update the head pointer for the list
            self.head = second

        return self.head
