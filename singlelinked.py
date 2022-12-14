class Node:
    def __init__(self,data):
        self.data = data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def single_ll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            tem = self.head
            while tem:
                print(tem.data)
                tem = tem.ref

LL1 = LinkedList()
n1 = Node(10)
LL1.head=n1
n2 = Node(30)
n1.ref=n2
LL1.single_ll()

