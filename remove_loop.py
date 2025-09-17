class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def detectAndRemoveLoop(self):
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                self.removeLoop(slow)
                return True
        return False

    def removeLoop(self, loop_node):
        ptr1 = self.head
        while True:
            ptr2 = loop_node
            while ptr2.next != loop_node and ptr2.next != ptr1:
                ptr2 = ptr2.next
            if ptr2.next == ptr1:
                break
            ptr1 = ptr1.next
        ptr2.next = None

# Example usage
ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.head.next.next.next = ll.head
ll.detectAndRemoveLoop()
