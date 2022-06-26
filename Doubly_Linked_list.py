# Doubly Linked List

# Creating a node in doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Creating a class of doubly linked list


class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def traversal_forward(self):
        if self.head is None:
            print("The Doubly linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next

    def traversal_backward(self):
        print()
        if self.head is None:
            print("The doubly linked list is empty")
        a = self.head
        while a.next is not None:
            a = a.next
        while a is not None:
            print(a.data, end=" ")
            a = a.prev

    def insertion_at_beginning(self, data):
        print()
        ni = Node(data)
        a = self.head
        a.prev = ni
        ni.next = a
        self.head = ni

    def insertion_at_end(self,data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        ne.prev = a

    def inerstion_at_specific_positon(self , position , data):
        print()
        nis = Node(data)
        a = self.head
        for i in range(1,position - 1):
            a = a.next
        nis.prev = a
        nis.next = a.next
        a.next.prev = nis
        a.next = nis

    def deletion_at_beginning(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None
        self.head.prev = None

    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    def deletion_at_specific_position(self , position):
        print()
        a = self.head.next
        prev = self.head
        for i in range(1, position - 1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next.prev = prev
        a.next = None
        a.prev = None






# Giving values and calling the functions
n1 = Node(5)
dll = Doublylinkedlist()
dll.head = n1
n2 = Node(10)
n1.next = n2
n2.prev = n1
n3 = Node(15)
n2.next = n3
n3.prev = n2
n4 = Node(20)
n3.next = n4
n4.prev = n3
dll.traversal_forward()
dll.traversal_backward()
dll.insertion_at_beginning(0)
dll.traversal_forward()
dll.insertion_at_end(25)
dll.traversal_forward()
dll.inerstion_at_specific_positon(3,12.5)
dll.traversal_forward()
dll.deletion_at_beginning()
dll.traversal_forward()
dll.deletion_at_end()
dll.traversal_forward()
dll.deletion_at_specific_position(3)
dll.traversal_forward()




