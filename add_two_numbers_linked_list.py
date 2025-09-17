class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def addTwoLists(first, second):
        prev = temp = None
        carry = 0
        res = None
        while first or second:
            fdata = first.data if first else 0
            sdata = second.data if second else 0
            total = carry + fdata + sdata
            carry = total // 10
            total = total % 10
            new_node = Node(total)
            if res is None:
                res = new_node
            else:
                temp.next = new_node
            temp = new_node
            if first:
                first = first.next
            if second:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)
        return res

# Example usage
first = LinkedList()
second = LinkedList()
first.push(6)
first.push(4)
first.push(9)
second.push(4)
second.push(8)
res = LinkedList.addTwoLists(first.head, second.head)
while res:
    print(res.data, end=" ")
    res = res.next
