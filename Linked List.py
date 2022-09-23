class Node:
    def __init__(self , data = None , next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data , self.head)
        self.head = node

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = "--->"
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr  = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


if __name__ == '__main__':
    root = LinkedList()
    root.insert_at_beginning(5)
    root.insert_at_beginning(15)
    root.insert_at_beginning(25)
    root.insert_at_beginning(35)
    print(root.get_length())
    root.print()
