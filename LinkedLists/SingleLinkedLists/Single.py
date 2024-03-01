class ListNode:
    """
    Represents a node in a singly linked list.

    Attributes:
        val: The value stored in the node.
        next: Reference to the next node in the list.
    """
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    """
    Represents a singly linked list with basic operations.

    Methods:
        insertEnd(val): Inserts a new node with the given value at the end.
        remove(index): Removes the node at the specified index.
        print(): Prints the values of the linked list.
    """
    def __init__(self):
        # Initialize the list with a 'dummy' node (sentinel node)
        self.head = ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        """Inserts a new node at the end of the list."""
        self.tail.next = ListNode(val)
        self.tail = self.tail.next  # Update the tail pointer

    def remove(self, index):
        """Removes the node at the specified index."""
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        # Remove the node ahead of curr
        if curr:
            curr.next = curr.next.next

    def print(self):
        """Prints the values of the linked list."""
        curr = self.head.next
        while curr:
            print(curr.val, ' -> ')
            curr = curr.next
        print()

# Example usage
my_list = LinkedList()
my_list.insertEnd(10)
my_list.insertEnd(20)
my_list.insertEnd(30)
my_list.print()  # Output: 10 -> 20 -> 30 ->
my_list.remove(1)  # Remove the second node (20)
my_list.print()  # Output: 10 -> 30 ->
