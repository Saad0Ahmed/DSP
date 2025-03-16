class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_node(self, key):
        temp = self.head
        while temp is not None and temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
                temp = None
            return
        while temp is not None and temp.data != key:
            temp = temp.next
            if temp is None:
                return
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
                temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <--> " if temp.next else '')
            temp = temp.next
        print()
        
#example usage
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.display()
dll.delete_node(20)
dll.display()