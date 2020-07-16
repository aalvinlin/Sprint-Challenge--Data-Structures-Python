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

    def __str__(self):

        current_node = self.head

        string_representation = str(current_node.get_value())

        while current_node.next_node:

            current_node = current_node.next_node
            string_representation += " -> " + str(current_node.get_value())

        return string_representation

    def reverse_list(self, current, prev):
        # self.reverse_list_iterative(current, prev)
        self.reverse_list_recursive(current, prev)

    def reverse_list_iterative(self, current, prev):

        # return an empty list or an one-element list unchanged
        if not self.head or not self.head.next_node:
            return self.head

        # look at elements two at a time. Move the pointers for "current" and the next node around.
        while current.next_node:
            
            # the node after current will beocme the new head. Store in a variable
            new_head = current.next_node

            # current's next node will now become the node that is currently 2 elements down
            current.set_next(current.next_node.next_node)

            # link the node that will become the new head to the current head
            new_head.set_next(self.head)

            # update head pointer
            self.head = new_head

        return

    def reverse_list_recursive(self, current, prev):

        if not current.next_node:
            self.head = current
            return current
        else:

            reversed_sublist = reverse_list(current.next_node, current)

            return [self.reverse_list(current.next_node, None), current]

        pass

test = LinkedList()
test.add_to_head(1)
test.add_to_head(2)
test.add_to_head(3)
test.add_to_head(4)
test.add_to_head(5)

reverse = test.reverse_list(test.head, None)

# print(test)
# print(reverse)