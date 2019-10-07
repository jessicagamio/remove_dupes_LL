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

    def add_node_to_list(self, data):
        """add node to linked list"""

        node = set_node(data)

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
            if node_dict.get(curr.data,0):
                curr= curr.next
                prev=curr 

            else:
                node_dict[curr.data] += 1
                prev=curr
                curr=curr.next

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr= curr.next


ll=Linked_List()

ll.add_node_to_list('a')
ll.add_node_to_list('b')
ll.add_node_to_list('a')
ll.add_node_to_list('c')

ll.print_list()
ll.rem_dupes()
ll.print_list()