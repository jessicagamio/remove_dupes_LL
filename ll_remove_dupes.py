class Node(object):
    def __init__(self,data):
        """Initialize node"""
        self.data = data
        self.next = None

class Linked_List(object):
    def __init__(self):
        """initialize LL """
        self.head = None
        self.tail = None

    def set_node(self, data):
        """create node"""
        node= Node(data)
        return node

    def add_node_to_list(self, node):
        """add node to linked list"""
        if self.head == None:
            node = self.head
            self.tail == None
        elif self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail=node


    def rem_dupes(self):
        """remove duplicates from linked list"""
        prev= None
        curr= self.head
        node_dict = {}

        while curr:
            if node_dict.get(curr,0):
                curr= curr.next
                prev=curr 

            else:
                node_dict += 1
                prev=curr
                curr=curr.next

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr= curr.next



a = Linked_List()
node = a.set_node('a')
a.add_node_to_list(node)

b = Linked_List()
node = b.set_node('b')
b.add_node_to_list(node)

c = Linked_List()
node = c.set_node('c')
c.add_node_to_list(node)
