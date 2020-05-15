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

    def reverse_list(self, node, prev):

        # return an empty list or an one-element list unchanged
        if not self.head or not self.head.next_node:
            return self.head

        print("not empty", self)

        current = node

        # look at elements two at a time
        # while current.next_node:
        while current.next_node and current.next_node.get_value():

            print("current node value:", current.get_value(), "next:", current.next_node.get_value())
            
            new_head = current.next_node

            print(self)

            current.next = current.next_node.next_node

            print(self)

            new_head.next_node = self.head

            print(self)

            self.head = new_head

            print(self)


            # # store a pointer to the next node
            # second = node.next_node

            # # reasssign current node's "next" pointer to the next element after this pair (third element)
            # node.set_next(second.next_node)

            # # reassign the second node's "next" pointer to point to the current element
            # second.set_next(node)

            # # update the head pointer for the list
            # self.head = second

            # # update node to point at the next node in the list for the next iteration
            # node = node.next_node

            print("current list:", self)

        return self.head

test = LinkedList()
test.add_to_head(1)
test.add_to_head(2)
test.add_to_head(3)
test.add_to_head(4)
test.add_to_head(5)

reverse = test.reverse_list(test.head, None)

print(test)
print(reverse)