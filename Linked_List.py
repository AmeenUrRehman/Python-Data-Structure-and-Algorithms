#Linked list all operations
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Singlelist:
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print("The singlylist is empty we can do much about it !!!")
        else:
            a = self.head
            while a is not None:
                print(a.data , end=" ")
                a = a.next
# Insertion of node at beginning
    def inerstion_by_beginning(self , data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb

# Insertion of node at end
    def insertion_by_end(self , data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

# Insertion of node at the specific position

    def insertion_by_postion(self , position , data):
        print()
        np = Node(data)
        a = self.head
        for i in range(1 , position - 1):
            a = a.next
        np.next = a.next
        a.next = np

# Deletion of node from the beginning

    def deletion_from_beginnng(self):
        print()
        a = self.head  #0
        self.head = a.next
        a.next = None

# Deletion of node from the end

    def deletion_from_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

# Deletion of node at the specific position

    def deletion_from_specific_position(self , position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1 , position - 1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None

# Giving values to the node and calling the functions

n1 = Node(5)
sll = Singlelist()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4


sll.traversal()

sll.inerstion_by_beginning(0)
sll.traversal()

sll.insertion_by_end(25)
sll.traversal()

sll.insertion_by_postion(3, 12.5)
sll.traversal()

sll.deletion_from_beginnng()
sll.traversal()

sll.deletion_from_end()
sll.traversal()

sll.deletion_from_specific_position(2)
sll.traversal()
