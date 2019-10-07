class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_data(self, data):
        node= Node(data)

    def add_node_to_list(self, node):
        if self.head == None:
            node = self.head
            self.tail == None
        elif self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail=node


    def rem_dupes(self)
        

a = Node('a')
a = Linked_List()

b = Node('b')
b = Linked_List()

a = Linked_List()

c = Node('c') 
c = Linked_List()


