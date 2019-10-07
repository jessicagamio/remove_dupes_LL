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



a = Linked_List()


b = Linked_List()


c = Linked_List()


