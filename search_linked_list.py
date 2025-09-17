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

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

# Example usage
ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
print(ll.search(20))  # True
print(ll.search(40))  # False
