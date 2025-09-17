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

    def detectLoop(self):
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Example usage
ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(10)
ll.head.next.next.next.next = ll.head
print(ll.detectLoop())
