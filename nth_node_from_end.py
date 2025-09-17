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

    def nthFromEnd(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        count = 0
        while count < n:
            if ref_ptr is None:
                return None
            ref_ptr = ref_ptr.next
            count += 1
        while ref_ptr:
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        return main_ptr.data if main_ptr else None

# Example usage
ll = LinkedList()
for i in range(1, 6):
    ll.push(i)
print(ll.nthFromEnd(2))
