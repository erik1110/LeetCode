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
 
    def shift(self):
        if not self.head:
            return
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.length = 0
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp

    def unshift(self, value):
        if not self.head:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1

    def insertAt(self, index, value):
        if index > self.length or index < 0 :
            raise Exception("Index 錯誤")
        elif index == 0:
            self.unshift(value)
        elif index == self.length:
            self.push(value)
        else:
            current_node = self.head
            new_node = Node(value)
            for i in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    def removedAt(self, index):
        if index > self.length or index < 0 :
            raise Exception("Index 錯誤")
        elif index == 0:
            self.shift()
        elif index == self.length:
            self.pop()
        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            temp = current_node.next
            current_node.next = current_node.next.next
            self.length -= 1
            return temp

    def get(self, index):
        if index > self.length or index < 0 :
            raise Exception("Index 錯誤")
        else:
            current_node = self.head
            count = 0
            while current_node:
                if count == index:
                    return current_node.value
                current_node = current_node.next
                count += 1

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
    myLinkedList.print_list()
    print(myLinkedList.get(2))
