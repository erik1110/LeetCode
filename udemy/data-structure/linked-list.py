class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            # 看 current_node 是不是最後一個，不是就繼續 next
            # 是最後一個，next 就連接上新的 new_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def pop(self):
        if not self.head:
            return
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.length = 0
            return temp
        else:
            current_node = self.head
            prev_node = None
            while current_node.next:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = None
            self.length -= 1
            return current_node

        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()
        
        
if __name__ == "__main__":
    myLinkedList = LinkedList()
    myLinkedList.push("Mike")
    myLinkedList.push("Ann")
    myLinkedList.push("Emily")
    myLinkedList.pop()
    myLinkedList.pop()
    myLinkedList.print_list()